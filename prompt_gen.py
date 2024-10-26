import vertexai
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv

load_dotenv()

vertexai.init(project=os.getenv("PROJECT_ID"), location="us-central1")

system_instruction = """
You are an assistant that generates a JSON response consisting of 'images' and 'text' fields to explain a concept provided in the user prompt in as simple a way as possible with as many details as possible.
You should explain the concept like you would to a 12 year old.

- The 'images' field is a dictionary with keys being names of daily objects used in the explanation (e.g., 'apple', 'banana') and values being None.
- The 'text' field is a transcript in an SRT format for a one-person voiceover with timestamps explaining the concept. 

Your task is to take the user's prompt and generate a JSON response as per the format above, using simple daily objects in the explanation.
"""

model = GenerativeModel(model_name="gemini-1.5-flash",  system_instruction=system_instruction)

response = model.generate_content(
    "Explain addition to me"
)

print(response.text)