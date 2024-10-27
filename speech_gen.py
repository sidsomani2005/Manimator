import vertexai
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv
import json
from imagen import main
load_dotenv()

vertexai.init(project=os.getenv("PROJECT_ID"), location="us-central1")


def steps_agent(prompt: str):
    system_instruction = """
    You are a master animator that generates a JSON response consisting of 'title, 'images' and 'steps' fields to explain a concept provided in the user prompt using an animation designed to be as simple as possible. 
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
        "title": "Addition",
        "images": {
            "apple": null
        },
        "steps": {
            "Step 1: Initialize a canvas of size 800x600 pixels.": null,
            "Step 2: Set the size of each apple to 50x50 pixels.": null,
            "Step 3: Add Apple 1 at coordinates (100, 300).": null,
            "Step 4: Add Apple 2 at coordinates (200, 300).": null,
            "Step 5: Apply a fade-in effect lasting 0.5 seconds for each apple.": null,
            "Step 6: Add a plus sign at coordinates (250, 300) with a size of 50x50 pixels.": null,
            "Step 7: Display Apple 3 at coordinates (800, 300), Apple 4 at (900, 300), and Apple 5 at (1000, 300).": null,
            "Step 8: Move Apple 3 from (800, 300) to (350, 300) over 0.7 seconds.": null,
            "Step 9: Move Apple 4 from (900, 300) to (450, 300) over 0.7 seconds.": null,
            "Step 10: Move Apple 5 from (1000, 300) to (550, 300) over 0.7 seconds.": null,
            "Step 11: Apply a scale-in effect to the plus sign over 0.3 seconds.": null,
            "Step 12: Apply an ease-in effect to the movement of the apples.": null,
            "Step 13: Move Apple 1 to (100, 300) and Apple 2 to (200, 300).": null,
            "Step 14: Move Apple 3 to (300, 300), Apple 4 to (400, 300), and Apple 5 to (500, 300).": null,
            "Step 15: Animate the apples moving over 1 second with an ease-out effect and a bounce effect.": null,
            "Step 16: Add a text box displaying \"2 + 3 = 5\" at coordinates (350, 100).": null,
            "Step 17: Set the font size to 48px bold for the text.": null
        }
    }

    """

    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )


    response = model.generate_content(prompt)
    return response.text

def steps_checking_agent(prompt: str):
    system_instruction = """
    You are super reader that checks the work of another agent. You will be given a json input of the form below and output a similar JSON with some changes: 
    { 
        "title": "Addition",
        "images": { 
            "apple": null
        },
        "steps": {
            "Step 1: Initialize a canvas of size 800x600 pixels.": null,
            "Step 2: Set the size of each apple to 50x50 pixels.": null,
            "Step 3: Add Apple 1 at coordinates (100, 300).": null,
            "Step 4: Add Apple 2 at coordinates (200, 300).": null,
            "Step 5: Apply a fade-in effect lasting 0.5 seconds for each apple.": null,
            "Step 6: Add a plus sign at coordinates (250, 300) with a size of 50x50 pixels.": null,
            "Step 7: Display Apple 3 at coordinates (800, 300), Apple 4 at (900, 300), and Apple 5 at (1000, 300).": null,
            "Step 8: Move Apple 3 from (800, 300) to (350, 300) over 0.7 seconds.": null,
            "Step 9: Move Apple 4 from (900, 300) to (450, 300) over 0.7 seconds.": null,
            "Step 10: Move Apple 5 from (1000, 300) to (550, 300) over 0.7 seconds.": null,
            "Step 11: Apply a scale-in effect to the plus sign over 0.3 seconds.": null,
            "Step 12: Apply an ease-in effect to the movement of the apples.": null,
            "Step 13: Move Apple 1 to (100, 300) and Apple 2 to (200, 300).": null,
            "Step 14: Move Apple 3 to (300, 300), Apple 4 to (400, 300), and Apple 5 to (500, 300).": null,
            "Step 15: Animate the apples moving over 1 second with an ease-out effect and a bounce effect.": null,
            "Step 16: Add a text box displaying \"2 + 3 = 5\" at coordinates (350, 100).": null,
            "Step 17: Set the font size to 48px bold for the text.": null
        }
    }


    Your job is to check the images and steps dictionaries in the following order:
        1) If you find any key in the images dictionary that SAID as a mathematical shape (arrow, circle, square) replace their value with "Manim" 
        2) After all checks for the image dictionary are completed you will go to the steps and see where the any of the objects which are keys in the images dictionary are being used. Once found replace them with *_<objectkey>_* where objectkey is the actual key from the images dictionary.


    For the example above your output would be: 
    {
        "title": "Addition",
        "images": {
            "apple": null
        },
        "steps": {
            "Step 1: Initialize a canvas of size 800x600 pixels.": null,
            "Step 2: Set the size of each apple to 50x50 pixels.": null,
            "Step 3: Add *_apple_* 1 at coordinates (100, 300).": null,
            "Step 4: Add *_apple_* 2 at coordinates (200, 300).": null,
            "Step 5: Apply a fade-in effect lasting 0.5 seconds for each *_apple_*.": null,
            "Step 6: Add a plus sign at coordinates (250, 300) with a size of 50x50 pixels.": null,
            "Step 7: Display *_apple_* 3 at coordinates (800, 300), *_apple_* 4 at (900, 300), and *_apple_* 5 at (1000, 300).": null,
            "Step 8: Move *_apple_* 3 from (800, 300) to (350, 300) over 0.7 seconds.": null,
            "Step 9: Move *_apple_* 4 from (900, 300) to (450, 300) over 0.7 seconds.": null,
            "Step 10: Move *_apple_* 5 from (1000, 300) to (550, 300) over 0.7 seconds.": null,
            "Step 11: Apply a scale-in effect to the plus sign over 0.3 seconds.": null,
            "Step 12: Apply an ease-in effect to the movement of the *_apple_*.": null,
            "Step 13: Move *_apple_* 1 to (100, 300) and *_apple_* 2 to (200, 300).": null,
            "Step 14: Move *_apple_* 3 to (300, 300), *_apple_* 4 to (400, 300), and *_apple_* 5 to (500, 300).": null,
            "Step 15: Animate the *_apple_*s moving over 1 second with an ease-out effect and a bounce effect.": null,
            "Step 16: Add a text box displaying \"2 + 3 = 5\" at coordinates (350, 100).": null,
            "Step 17: Set the font size to 48px bold for the text.": null
        }
    }

    """
    model = GenerativeModel(
        model_name="gemini-1.5-flash", system_instruction=system_instruction
    )


    response = model.generate_content(prompt)
    return response.text


def audio_agent(prompt: str):
    
    system_instruction = """
    You are master trascriber assistant that generates beautiful and extremely cohesive and clear speech transcripts based on the steps provided:

    **Your Task:**

    - **Input:** You will receive a JSON object with three fields: 'title', 'images', and 'steps'
    - The 'title' field is a high level description or overarching topic of what the prompt is asking for. (e.g., if the prompt/explanation describes adding 2 sets of fruits, say 3 green apples to 5 red apples, the title would be 'addition')
    - The `images` field is a dictionary where the keys are names of daily objects (e.g., 'apple', 'banana'). DO NOT WORRY ABOUT THIS DICTIONARY.
    - The 'steps' field is a dictionary where the keys are the specific steps to generate speech transcriptions on. HOWEVER, THE VALUES CORRESPONDING TO EACH STEP WILL BE NULL. THESE VALUES ARE WHAT YOU NEED TO FILL WITH SPEECH TRANSCRIPTIONS (REFER TO OUTPUT GUIDELINES)
    - Here is a sample of what the input would be for you to generate speech additions:
        {
            "title": "Subtraction",
            "images": {
                "cookie": "https://storage.googleapis.com/path_to_cookie_image.png"
            },
            "steps" : 
            {
                "Step 1: Initialize a canvas of size 800x600 pixels." : null
                "Step 2: Set the size of each cookie to 40x40 pixels." : null
                "Step 3: Add 5 cookies horizontally, starting at coordinates (100, 300) with 50 pixel spacing between each cookie." : null
                "Step 4: Apply a fade-in effect lasting 0.5 seconds for all five cookies." : null
                "Step 5: Add a minus sign at coordinates (450, 300) with a size of 50x50 pixels." : null
                "Step 6: Add the number '5' at coordinates (300, 200) with a font size of 48px bold." : null
                "Step 7: Add the number '2' at coordinates (550, 200) with a font size of 48px bold." : null
                "Step 8: Move 2 cookies starting from the rightmost cookie upwards from (300, 300) to (300, 100) one after the other with 0.5 seconds delay between each cookie and a fade-out effect over 0.3 seconds.": null
                "Step 9: Apply a scale-in effect to the minus sign over 0.3 seconds." : null
                "Step 10: Add an equals sign at coordinates (450, 200) with a size of 50x50 pixels and apply a fade-in effect over 0.5 seconds." : null
                "Step 11: Add the number '3' at coordinates (450, 100) with a font size of 48px bold and apply a fade-in effect over 0.5 seconds." : null
            }
        }


    **Output**: 
    - Each step (key) in the 'steps' field has a corresponding value. This value is a transcript in speech format for a one-person voiceover with timestamps explaining a concept. Objects from the `images` dictionary used in the text are denoted by `_*object_name*_`. 
    - The output should be a JSON response that is the same as the input but includes the speech transcriptions for each respective step.


    Your JSON output will have these fields:
    - The 'title' field is a short title of the concept you are making the animation for (given in the input).
    - The 'images' field is a dictionary with keys being names of daily object used in the animation (e.g., 'football', 'apple') and values being null (given in the input).
    - The 'steps' field is a dictionary with keys being each step you take to make animation (given in the input) and the corresponding speech transcriptions (intended output).
    
    GUIDELINES FOR SPEECH OUTPUT GENERATION:
    - Based on the title, which is the overarching concept of the explanation, build a framework/reference for the larger topic of the speech transcriptions in totality.
    - When generating the SPEECH transcriptions, ensure that they are for each step in the 'steps' key field, and correspond and flow logically.
    - When generating the SPEECH transcriptions, ensure that it does NOT mention pixels, or coordinates. THESE TRANSCRIPTIONS MUST EXPLAIN CONCEPTS AND TOPICS AT A HIGH LEVEL.
    - Focus on generating SPEECH transcriptions that synthesizes each steps based on the provided title and explains the steps in a conceptual manner and in a way that is being asked for and is very easy to comprehend and understand.


    Here is a sample output:
    {
        "title" : "Subtraction",
        "images" : 
        {
            "cookie": "https://storage.googleapis.com/path_to_cookie_image.png"
        },
        "steps" : 
        {
            "Step 1: Initialize a canvas of size 800x600 pixels." : "Let's explore subtraction.",
            "Step 2: Set the size of each cookie to 40x40 pixels." : "Imagine you have a plate with 5 cookies on it.",
            "Step 3: Add 5 cookies horizontally, starting at coordinates (100, 300) with 50 pixel spacing between each cookie." : "Each cookie represents one item in our total count.",
            "Step 4: Apply a fade-in effect lasting 0.5 seconds for all five cookies." : "Now, let’s say you eat 2 of these cookies. .",
            "Step 5: Add a minus sign at coordinates (450, 300) with a size of 50x50 pixels." : "We’ll start by taking away 2 cookies from the plate..",
            "Step 6: Add the number '5' at coordinates (300, 200) with a font size of 48px bold." : "As each cookie is removed, our total number of cookies decreases.",
            "Step 7: Add the number '2' at coordinates (550, 200) with a font size of 48px bold." : "After removing 2 cookies, let’s count how many are left.",
            "Step 8: Move 2 cookies starting from the rightmost cookie upwards from (300, 300) to (300, 100) one after the other with 0.5 seconds delay between each cookie and a fade-out effect over 0.3 seconds.": "We began with 5 cookies and removed 2.",
            "Step 9: Apply a scale-in effect to the minus sign over 0.3 seconds." : "Now, there are 3 cookies left on the plate. ",
            "Step 10: Add an equals sign at coordinates (450, 200) with a size of 50x50 pixels and apply a fade-in effect over 0.5 seconds." : "This shows that 5 minus 2 equals 3",
            "Step 11: Add the number '3' at coordinates (450, 100) with a font size of 48px bold and apply a fade-in effect over 0.5 seconds." : "You now have 3 cookies left!"
        }
    } 

    """
    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )


    response = model.generate_content(prompt)
    return response.text



def remove_code_block_markers(text, language='json'):
    """
    Removes Markdown code block markers from the given text.

    Args:
        text (str): The input string containing Markdown code block.
        language (str): The language specifier after the opening backticks.

    Returns:
        str: The cleaned string without code block markers.
    """
    lines = text.strip().split('\n')
    
    if lines and lines[0].startswith(f'```{language}'):
        lines = lines[1:] 
    else:
        print("Warning: The input does not start with the expected code block marker.")
    
    if lines and lines[-1].strip() == '```':
        lines = lines[:-1] 
    else:
        print("Warning: The input does not end with the expected code block marker.")
    
    cleaned_text = '\n'.join(lines)
    return cleaned_text


def final_flow(prompt):
    initial_check = steps_agent(prompt)
    print(initial_check)
    next_check = steps_checking_agent(initial_check)
    print(next_check)
    next_check = remove_code_block_markers(next_check, "json")
    next_check = main(next_check)
    print(next_check)
    return (audio_agent(next_check))

if __name__ == "__main__":
    print(final_flow("division"))



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