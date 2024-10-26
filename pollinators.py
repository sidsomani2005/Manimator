import json
import requests
import os
from google.cloud import storage

def generate_image_with_pollinations(object_name):
    prompt = f"Create a {object_name} in a clipart style with a white background. The {object_name} should have an animated, cartoon-like appearance featuring clear, bold lines and vibrant colors. Ensure the design is simple, playful, and resembles traditional clipart illustrations."
    width = 512
    height = 512
    seed = 42
    model = 'flux'
    image_url = f"https://pollinations.ai/p/{prompt}?width={width}&height={height}&seed={seed}&model={model}"
    return image_url

def download_image(image_url, object_name):
    response = requests.get(image_url)
    temp_file = f"/tmp/{object_name}.png"
    with open(temp_file, 'wb') as file:
        file.write(response.content)
    return temp_file

def remove_background_with_remove_bg(image_path):
    """Removes background using remove.bg API."""
    with open(image_path, 'rb') as image_file:
        response = requests.post(
            'https://api.remove.bg/v1.0/removebg',
            files={'image_file': image_file},
            data={'size': 'auto'},
            headers={'X-Api-Key': "ctrgJN5nvYBKMB4DAZU1NKqt"}
        )
    
    if response.status_code == 200:
        output_file = image_path.replace(".png", "_no_bg.png")
        with open(output_file, 'wb') as out_file:
            out_file.write(response.content)
        return output_file
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None

def upload_image_to_gcs(bucket_name, object_name, image_path):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{object_name}.png")
    
    # Upload the image
    blob.upload_from_filename(image_path)
    
    # Remove the temporary file
    os.remove(image_path)
    
    # Return the URL of the uploaded object (public URL depends on bucket permissions)
    public_url = f"https://storage.googleapis.com/{bucket_name}/{object_name}.png"
    
    return public_url

def check_if_image_exists(bucket_name, object_name):
    """Check if an image already exists in GCS."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{object_name}.png")
    return blob.exists()

def process_json_and_generate_images(json_data, bucket_name):
    for category in json_data['images']:
        if json_data['images'][category] is None:
            if check_if_image_exists(bucket_name, category):
                # If the image exists, use the existing link
                public_url = f"https://storage.googleapis.com/{bucket_name}/{category}.png"
                print(f"Found existing image for '{category}'. Using existing link.")
                json_data['images'][category] = public_url
            else:
                # Generate image URL
                image_url = generate_image_with_pollinations(category)
                
                # Download the image
                temp_file = download_image(image_url, category)
                
                # Remove the background using remove.bg API
                temp_file_no_bg = remove_background_with_remove_bg(temp_file)
                
                if temp_file_no_bg is not None:
                    # Upload image to GCS and get public URL
                    public_url = upload_image_to_gcs(bucket_name, category, temp_file_no_bg)
                    
                    # Update JSON with the public URL
                    json_data['images'][category] = public_url
        else:
            print(f"Image for '{category}' is already present in JSON.")
    
    return json_data

# End-to-end process
def process_image_json(input_json, bucket_name):
    # Step 1: Read the input JSON file
   
    json_data = input_json
    
    # Extract only the "images" dictionary from the input
    images_data = {"images": json_data.get("images", {})}

    print("Input images data:")
    print(json.dumps(images_data, indent=2))
    print()

    # Step 2: Process the JSON, generate images, and update with GCP links
    updated_json = process_json_and_generate_images(images_data, bucket_name)
    print("Updated images data:")
    output = json.dumps(updated_json, indent=2)
    print()

    print(f"Updated JSON written to: {output}")

# Example usage
# input_json_path = 'input.json'
# output_json_path = 'output.json'
bucket_name = 'mani_image_buckets'

# Example input JSON (as per your example)
sample_input = """{
    "images": {
        "apple": null,
        "banana": null
    },
    "text": "00:00:00,000 --> 00:00:05,000\\nImagine you have 2 apples. \\n\\n00:00:05,000 --> 00:00:10,000\\nSomeone gives you 3 more apples. \\n\\n..."
}"""


# Run the end-to-end process
process_image_json(json.loads(sample_input), bucket_name)
