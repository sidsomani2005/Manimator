import vertexai
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv
import json

load_dotenv()

vertexai.init(project=os.getenv("PROJECT_ID"), location="us-central1")


def steps_agent(prompt: str):
    system_instruction = """
    You are an assistant that generates a JSON response consisting of 'title, 'images' and 'steps' fields to explain a concept provided in the user prompt using an animation designed to be as simple as possible. 
    You will ONLY use objects in daily life to make the animation. Your animation should be as simple as possible and be understood by a 12 year old.
    Your output will have these fields:

    - The 'title' field is a short title of the concept you are making the animation for.
    - The 'images' field is a dictionary with keys being names of daily object used in the animation (e.g., 'football', 'apple') and values being null.
    - The 'steps' field is a dictionary with keys being each step you take to make animation.
    Each step must be given clearly and be as detailed as possible. EVERYTIME YOU MOVE/PLACE A OBJECT YOU MUST SPECIFY COORDINATES AND VALUES.
    Make the steps as if you were to draw this animation on paper.
    The values of this dictionary are null.

    Here is a sample of what you would output if the prompt was "explain addition":
    { 
        'title' : "Addition",
        'images' : 
        { 
            'apple' : null,
        },
        'steps' :
        {
            'Step 1: Initialize a canvas of size 800x600 pixels.' : null,
            'Step 2: Set the size of each apple to 50x50 pixels.' : null,
            'Step 3: Add Apple 1 at coordinates (100, 300).' : null,
            'Step 4: Add Apple 2 at coordinates (200, 300).' : null,
            'Step 5: Apply a fade-in effect lasting 0.5 seconds for each apple.' : null,
            'Step 6: Add a plus sign at coordinates (250, 300) with a size of 50x50 pixels.' : null,
            'Step 7: Display Apple 3 at coordinates (800, 300), Apple 4 at (900, 300), and Apple 5 at (1000, 300).' : null,
            'Step 8: Move Apple 3 from (800, 300) to (350, 300) over 0.7 seconds.' : null,
            'Step 9: Move Apple 4 from (900, 300) to (450, 300) over 0.7 seconds.' : null,
            'Step 10: Move Apple 5 from (1000, 300) to (550, 300) over 0.7 seconds.' : null,
            'Step 11: Apply a scale-in effect to the plus sign over 0.3 seconds.' : null,
            'Step 12: Apply an ease-in effect to the movement of the apples.' : null,
            'Step 13: Move Apple 1 to (100, 300) and Apple 2 to (200, 300).' : null,
            'Step 14: Move Apple 3 to (300, 300), Apple 4 to (400, 300), and Apple 5 to (500, 300).' : null,
            'Step 15: Animate the apples moving over 1 second with an ease-out effect and a bounce effect.' : null,
            'Step 16: Add a text box displaying "2 + 3 = 5" at coordinates (350, 100).' : null,
            'Step 17: Set the font size to 48px bold for the text.' : null,
        }

    }
    """
    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )


    response = model.generate_content(prompt)
    return response.text


def steps_agent(prompt: str):
    system_instruction = """
    You are an assistant that generates a JSON response consisting of 'title, 'images' and 'steps' fields to explain a concept provided in the user prompt using an animation designed to be as simple as possible. 
    You will ONLY use objects in daily life to make the animation. Your animation should be as simple as possible and be understood by a 12 year old.
    Your output will have these fields:

    - The 'title' field is a short title of the concept you are making the animation for.
    - The 'images' field is a dictionary with keys being names of daily object used in the animation (e.g., 'football', 'apple') and values being null.
    - The 'steps' field is a dictionary with keys being each step you take to make animation.
    Each step must be given clearly and be as detailed as possible. EVERYTIME YOU MOVE/PLACE A OBJECT YOU MUST SPECIFY COORDINATES AND VALUES.
    Make the steps as if you were to draw this animation on paper.
    The values of this dictionary are null.

    Here is a sample of what you would output if the prompt was "explain addition":
    { 
        'title' : "Addition",
        'images' : 
        { 
            'apple' : null,
        },
        'steps' :
        {
            'Step 1: Initialize a canvas of size 800x600 pixels.' : null,
            'Step 2: Set the size of each apple to 50x50 pixels.' : null,
            'Step 3: Add Apple 1 at coordinates (100, 300).' : null,
            'Step 4: Add Apple 2 at coordinates (200, 300).' : null,
            'Step 5: Apply a fade-in effect lasting 0.5 seconds for each apple.' : null,
            'Step 6: Add a plus sign at coordinates (250, 300) with a size of 50x50 pixels.' : null,
            'Step 7: Display Apple 3 at coordinates (800, 300), Apple 4 at (900, 300), and Apple 5 at (1000, 300).' : null,
            'Step 8: Move Apple 3 from (800, 300) to (350, 300) over 0.7 seconds.' : null,
            'Step 9: Move Apple 4 from (900, 300) to (450, 300) over 0.7 seconds.' : null,
            'Step 10: Move Apple 5 from (1000, 300) to (550, 300) over 0.7 seconds.' : null,
            'Step 11: Apply a scale-in effect to the plus sign over 0.3 seconds.' : null,
            'Step 12: Apply an ease-in effect to the movement of the apples.' : null,
            'Step 13: Move Apple 1 to (100, 300) and Apple 2 to (200, 300).' : null,
            'Step 14: Move Apple 3 to (300, 300), Apple 4 to (400, 300), and Apple 5 to (500, 300).' : null,
            'Step 15: Animate the apples moving over 1 second with an ease-out effect and a bounce effect.' : null,
            'Step 16: Add a text box displaying "2 + 3 = 5" at coordinates (350, 100).' : null,
            'Step 17: Set the font size to 48px bold for the text.' : null,
        }

    }
    """
    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )


    response = model.generate_content(prompt)
    return response.text



if __name__ == "__main__":
    print(steps_agent("Explain EigenValues"))




# def checking_agent(video: str, subject: str, code: str):
#     video_file = Part.from_uri(
#     uri=video,
#     mime_type="video/mp4",
#     )
#     system_instruction = """
#     You are an assistant that checks a video explaing a key concept called"""+  subject +""". 
#     You are given the video and the manim code to generate the video. Your job is to correct the manim code so the video
#     is correct and as intended. You must make sure that the concept is explained properly. You will only return manim code 
#     in the same format it was given to you. Dont explain anything just return the code.
#     """
#     contents = [video_file, "The video is attached and here is the code used to generate the video:" + code]
#     model = GenerativeModel(
#         model_name="gemini-1.5-pro", system_instruction=system_instruction
#     )

#     response = model.generate_content(contents)
#     return response.text