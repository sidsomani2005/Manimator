import json
from google.cloud import storage
import vertexai
from vertexai.preview.vision_models import ImageGenerationModel
import os

# Initialize Vertex AI
vertexai.init(project="mani-439723", location="us-central1")

def generate_image_with_imagen(object_name):
    model = ImageGenerationModel.from_pretrained("imagen-3.0-generate-001")
    prompt = f"Create a simple, flat icon of a single {object_name} in the style of Flaticon. The icon should have clean lines, minimal details, and a solid fill color. Ensure the background is completely transparent. The image should be suitable for use as a small app icon or website graphic."
    images = model.generate_images(
        prompt=prompt,
        number_of_images=1,
        aspect_ratio="1:1",
        safety_filter_level="block_some"
    )
    return images[0]

def upload_image_to_gcs(bucket_name, object_name, image):
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"{object_name}.png")
    
    # Save the image to a temporary file
    temp_file = f"/tmp/{object_name}.png"
    image.save(temp_file)
    
    # Upload the image
    blob.upload_from_filename(temp_file)
    
    # Make the blob publicly accessible
    blob.make_public()
    
    # Remove the temporary file
    os.remove(temp_file)
    
    return blob.public_url

def process_json_and_generate_images(json_data, bucket_name):
    for category, value in json_data['images'].items():
        if value is None:
            # Generate image
            generated_image = generate_image_with_imagen(category)
            
            # Upload image to GCS and get public URL
            public_url = upload_image_to_gcs(bucket_name, category, generated_image)
            
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
        "apple": None, "orange": None, "banana": None}
}
with open(input_json_path, 'w') as file:
    json.dump(sample_input, file, indent=2)

# Run the end-to-end process
process_image_json(input_json_path, output_json_path, bucket_name)