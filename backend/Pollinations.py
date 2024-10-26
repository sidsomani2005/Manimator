import json
import requests
import os
from google.cloud import storage

def generate_image_with_pollinations(object_name):
    prompt = f"Create a {object_name} in a clipart style with a white background. The [object] should have an animated, cartoon-like appearance featuring clear, bold lines and vibrant colors. Ensure the design is simple, playful, and resemble traditional clipart illustrations."
    width = 512
    height = 512
    seed = 42  # You can randomize this for different results each time
    model = 'flux'
    image_url = f"https://pollinations.ai/p/{prompt}?width={width}&height={height}&seed={seed}&model={model}"
    return image_url

def download_image(image_url, object_name):
    response = requests.get(image_url)
    temp_file = f"/tmp/{object_name}.png"
    with open(temp_file, 'wb') as file:
        file.write(response.content)
    return temp_file

def upload_image_to_gcs(bucket_name, object_name, image_path):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{object_name}.png")
    
    # Upload the image
    blob.upload_from_filename(image_path)
    
    # Make the blob publicly accessible
    blob.make_public()
    
    # Remove the temporary file
    os.remove(image_path)
    
    return blob.public_url

def process_json_and_generate_images(json_data, bucket_name):
    for category, value in json_data['images'].items():
        if value is None:
            # Generate image URL
            image_url = generate_image_with_pollinations(category)
            
            # Download the image
            temp_file = download_image(image_url, category)
            
            # Upload image to GCS and get public URL
            public_url = upload_image_to_gcs(bucket_name, category, temp_file)
            
            # Update JSON with the public URL
            json_data['images'][category] = public_url
    
    return json_data

# End-to-end process
def process_image_json(input_json_path, output_json_path, bucket_name):
    # Step 1: Read the input JSON file
    with open(input_json_path, 'r') as file:
        json_data = json.load(file)
    
    print("Input JSON data:")
    print(json.dumps(json_data, indent=2))
    print()

    # Step 2: Process the JSON, generate images, and update with GCP links
    updated_json = process_json_and_generate_images(json_data, bucket_name)
    print("Updated JSON data:")
    print(json.dumps(updated_json, indent=2))
    print()

    # Step 3: Write the updated JSON to the output file
    with open(output_json_path, 'w') as file:
        json.dump(updated_json, file, indent=2)
    
    print(f"Updated JSON written to: {output_json_path}")

# Example usage
input_json_path = 'input.json'
output_json_path = 'output.json'
bucket_name = 'mani_image_buckets'

# Create a sample input JSON file
sample_input = {
    "images": {
        "apple": None, "orange": None, "banana": None
    }
}
with open(input_json_path, 'w') as file:
    json.dump(sample_input, file, indent=2)

# Run the end-to-end process
process_image_json(input_json_path, output_json_path, bucket_name)