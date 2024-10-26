import os
import google.generativeai as genai

genai.configure(api_key='AIzaSyCNxWAds-uGnftFHKkgi7FdnK2u3x-Fne8')

imagen = genai.ImageGenerationModel("imagen-3.0-generate-001")
object_name = "apple"
result = imagen.generate_images(

    prompt=f"Create a {object_name} in a clipart style with a white background featuring a animated cartoon appearance with clear, bold lines and solid colors.",
    number_of_images=1,
    safety_filter_level="block_only_high",
    person_generation="allow_adult",
    aspect_ratio="1:1",
    negative_prompt="Any shadows at all",
)

for image in result.images:
  print(image)

# The output should look similar to this:
# <vertexai.preview.vision_models.GeneratedImage object at 0x78f3396ef370>
# <vertexai.preview.vision_models.GeneratedImage object at 0x78f3396ef700>
# <vertexai.preview.vision_models.GeneratedImage object at 0x78f33953c2b0>
# <vertexai.preview.vision_models.GeneratedImage object at 0x78f33953c280>

for image in result.images:
  # Open and display the image using your local operating system.
  image._pil_image.show()