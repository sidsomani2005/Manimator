import json
import requests
import os
from google.cloud import storage
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

# Configure the Generative AI API with your API key
genai.configure(api_key=os.getenv('IMAGEN_API'))

def generate_image_with_imagen(object_name):
    """
    Generates an image using Imagen 3 based on the provided object name.
    """
    prompt = (
        f"Create a {object_name} in a clipart style with a white background. "
        f"The {object_name} should have an animated, cartoon-like appearance featuring "
        f"clear, bold lines and vibrant colors. Ensure the design is simple, playful, "
        f"and resembles traditional clipart illustrations."
    )
    
    try:
        # Initialize the Imagen model
        imagen = genai.ImageGenerationModel("imagen-3.0-generate-001")
        
        # Generate the image
        result = imagen.generate_images(
            prompt=prompt,
            number_of_images=1,
            safety_filter_level="block_only_high",
            person_generation="allow_adult",
            aspect_ratio="1:1",  
            negative_prompt="",   
        )
        
        # Check if any images were returned
        if not result.images:
            print(f"No images were returned by Imagen for '{object_name}'. Please check the prompt or try again.")
            return None
        
        # Extract the PIL image from the result
        image = result.images[0]._pil_image
        
        # Save the image to a temporary file
        temp_file = f"/tmp/{object_name}.png"
        image.save(temp_file)
        
        print(f"Generated image for '{object_name}' using Imagen 3.")
        return temp_file
    
    except Exception as e:
        print(f"Error generating image for '{object_name}': {e}")
        return None
def remove_background_with_remove_bg(image_path):
    """
    Removes the background from the image using the remove.bg API.
    """
    REMOVE_BG_API_KEY = os.getenv("BG_REMOVE_API")  # Replace with your actual API key

    with open(image_path, 'rb') as image_file:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': image_file},
            data={'size': 'auto'},
            headers={'X-Api-Key': REMOVE_BG_API_KEY}
        )
    
    if response.status_code == 200:
        output_file = image_path.replace(".png", "_no_bg.png")
        with open(output_file, 'wb') as out_file:
            out_file.write(response.content)
        print(f"Background removed for '{image_path}'.")
        return output_file
    else:
        print(f"Error removing background for '{image_path}': {response.status_code}, {response.text}")
        return None

def upload_image_to_gcs(bucket_name, object_name, image_path):
    """
    Uploads the image to Google Cloud Storage and returns the public URL.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(f"{object_name}.png")
        
        blob.upload_from_filename(image_path)
        
        os.remove(image_path)  # Clean up the local file
        
        public_url = f"https://storage.googleapis.com/{bucket_name}/{object_name}.png"
        print(f"Uploaded '{object_name}.png' to GCS bucket '{bucket_name}'.")
        
        return public_url
    except Exception as e:
        print(f"Error uploading '{object_name}.png' to GCS: {e}")
        return None

def check_if_image_exists(bucket_name, object_name):
    """
    Checks if the image already exists in the specified GCS bucket.
    """
    try:
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(f"{object_name}.png")
        exists = blob.exists()
        if exists:
            print(f"Image '{object_name}.png' already exists in bucket '{bucket_name}'.")
        return exists
    except Exception as e:
        print(f"Error checking existence of '{object_name}.png' in GCS: {e}")
        return False

def process_json_and_generate_images(json_data, bucket_name):
    """
    Processes the JSON data to generate images for each category.
    """
    for category, url in json_data['images'].items():
        if url is None:
            if check_if_image_exists(bucket_name, category):
                public_url = f"https://storage.googleapis.com/{bucket_name}/{category}.png"
                print(f"Using existing image URL for '{category}'.")
                json_data['images'][category] = public_url
            else:
                temp_file = generate_image_with_imagen(category)
                
                if temp_file:
                    temp_file_no_bg = remove_background_with_remove_bg(temp_file)
                    
                    if temp_file_no_bg:
                        public_url = upload_image_to_gcs(bucket_name, category, temp_file_no_bg)
                        
                        if public_url:
                            json_data['images'][category] = public_url
        else:
            print(f"Image for '{category}' is already present in JSON.")
    
    return json_data

def process_image_json(input_json, bucket_name):
    """
    Orchestrates the image processing workflow.
    """
    json_data = input_json
    
    images_data = {"images": json_data.get("images", {})}

    print("Input images data:")
    print(json.dumps(images_data, indent=2))
    print()

    updated_json = process_json_and_generate_images(images_data, bucket_name)
    print("Updated images data:")
    output = json.dumps(updated_json, indent=2)
    print(output)

    return updated_json



def main(sample_input):
    bucket_name = 'mani_image_buckets'
    
    input_json = sample_input
    updated_json = process_image_json(input_json, bucket_name)
    
    input_json["images"] = updated_json["images"]
    return json.dumps(input_json, indent=2)
    
    
