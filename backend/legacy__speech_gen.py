import vertexai
from vertexai.generative_models import GenerativeModel, Part
import os
from dotenv import load_dotenv
import json
import requests
from imagen import main


load_dotenv()
import copy

vertexai.init(project=os.getenv("PROJECT_ID"), location="us-central1")


def steps_agent(prompt: str):
    system_instruction = """

        
    You are an assistant that generates a JSON response consisting of 'titles', 'images', 'srt', and 'info' fields to explain a concept provided in the user prompt in as simple a way as possible with as many details as possible.
    You should explain the concept like you would to a 12 year old.

    - The 'title' field is a short title of the concept you are making the animation for. (eg Addition, Subtraction, EigenValues) Be super concise and direct.
    - The 'images' field is a dictionary with keys being names of daily object used in the explanation (e.g., 'apple', 'banana') and values being null.
    - The 'srt' field is a transcript in an SRT format for a one-person voiceover with timestamps explaining the concept. 
    - The 'info' field is a dictionary with keys being the timestamps from the generated SRT file and values being detailed steps on how to draw and animate the concept being explained at that timestamp. For example, when explaining projectile motion,
      there could be a step to draw a ball at the top of the screen and animate it moving downwards in a parabolic path. In your steps, use the images that were generated above. Adhere to mathematical logic and physics. If there are no concepts being explained at a timestamp, then the value should be an empty string.

    Your task is to take the user's prompt and generate a JSON response as per the format above, using simple daily objects in the explanation.


    Here is a sample of the format you should output in:
    {
        "title": "<Add Title>",
        "images": {
            "<Any Item>": null
            <more as needed>,
        },
        "srt": {
        <Add SRT>
        },
        "info":{
            "<timestamp1>":<Action>,
            <more as needed>,
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
        "images": {
            "<Any Item>": null
            <more as present>,
        },
        "info":{
            "<timestamp1>":<Action>,
            <more as present>,
        }
        
    }


    Your job is to check the images and info dictionaries in the following order:
        1) If you find any key in the images dictionary that SAID as a mathematical shape (arrow, circle, square) replace their value with "Manim" 
        2) After all checks for the image dictionary are completed you will go to the info dictionary and see where the any of the objects which are keys in the images dictionary are being used. Once found replace them with *_<objectkey>_* where objectkey is the actual key from the images dictionary.

    You will then return the updated json.

    """
    model = GenerativeModel(
        model_name="gemini-1.5-flash", system_instruction=system_instruction
    )

    response = model.generate_content(prompt)
    return response.text


def manimator(data: str):

    system_instruction = """
    You are professional at Manim version (0.18.0) a python library used to make animations. 
    You have the entire manim library at your disposal. Feel free to check the internet for any confusion you might have.

    - **Input:** You will receive a JSON object with three fields: 'title', 'images', and 'steps'
        - The 'title' field is a short title of the concept you are making the animation for. (eg Addition, Subtraction, EigenValues) Be super concise and direct.
        - The 'images' field is a dictionary with keys being names of daily object used in the explanation (e.g., 'apple', 'banana') and values being null.
        - The 'srt' field is a transcript in an SRT format for a one-person voiceover with timestamps explaining the concept. 
        - The 'info' field is a dictionary with keys being the timestamps from the generated SRT file and values being detailed steps on how to draw and animate the concept being explained at that timestamp. For example, when explaining projectile motion,
        there could be a step to draw a ball at the top of the screen and animate it moving downwards in a parabolic path. In your steps, use the images that were generated above. Adhere to mathematical logic and physics. If there are no concepts being explained at a timestamp, then the value should be an empty string.

    - A sample JSON file that the code needs to be generated on is as follows: 
   {
        "title": "<Add Title>",
        "images": {
            "<Any Item>": null
            <more as needed>,
        },
        "srt": {
        <Add SRT>
        },
        "info":{
            "<timestamp1>":<Action>,
            <more as needed>,
        }
        
    }
    **Your Task:**
    Generate Manim code that performs the animation detailed in info with a voiceover from the srt:
    - The code generated should provide an animation that sequentially depicts each step in chronological order. 
    - Incorporates the images provided in the `images` dictionary whenever they are mentioned in the text.
    - If a image link is not provided, or is 'Manim', this means that the code can be generates directly from the manim library - MEANING THAT THE CODE FOR THIS SHAPE WILL NEED TO BE WRITTEN. (e.g, 'images' : { 'apple' : 'Manim' } means that the image for an apple NEEDS TO BE WRITTEN IN MANIM CODE BY THE MODEL ITSELF)
    - When an object denoted by `_*object_name*_` appears in the transcript, display the corresponding image using the provided GCP bucket link.
    - Synchronizes the animations with the voiceover using Manim's VoiceOver feature.

    **Manim Code Guidelines**
    - **Object Placemennt:** Verify all objects are being placed appropriately and as intended.
    - **Function Existence:** Verify that every function and class used in the generated code exists in the Manim library. If a step requires a function not present in the latest version, replace it with a valid alternative.
    - **Syntax Accuracy:** Ensure that the generated Python code is syntactically correct.
    - **Images:** The images in the JSON field 'images' must be either 'Manim' or google cloud storage links. If they are 'Manim', you must generate manim code to provide an alternative animation/shape that can represent the intended image.
    - **Variable Definitions:** All variables must be defined before they are used in animations.
    - **Voiceover Integration:** Ensure that voiceovers are synchronized with the animation steps using Manim's VoiceOver feature.

    **Output Format:**

    - Provide the complete Manim Python code as plain text.
    - Do not include any explanations outside the code.
    - Do not include any stray characters.
    - Output in the format of a Python script that can be run in a Manim environment directly without any modifications.
    - An example is given below:
        from manim import *
        from manim_voiceover import VoiceoverScene
        from manim_voiceover.services.gtts import GTTSService

        class GTTSExample(VoiceoverScene):
            def construct(self):
                self.set_speech_service(GTTSService(lang="en", tld="com"))

                circle = Circle()
                square = Square().shift(2 * RIGHT)

                with self.voiceover(text="This circle is drawn as I speak.") as tracker:
                    self.play(Create(circle), run_time=tracker.duration)

                with self.voiceover(text="Let's shift it to the left 2 units.") as tracker:
                    self.play(circle.animate.shift(2 * LEFT), run_time=tracker.duration)

                with self.voiceover(text="Now, let's transform it into a square.") as tracker:
                    self.play(Transform(circle, square), run_time=tracker.duration)

                with self.voiceover(text="Thank you for watching."):
                    self.play(Uncreate(circle))

                self.wait()


   


    """

    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )

    response = model.generate_content(data)
    return response.text


def remove_code_block_markers(text, language="json"):
    """
    Removes Markdown code block markers from the given text.

    Args:
        text (str): The input string containing Markdown code block.
        language (str): The language specifier after the opening backticks.

    Returns:
        str: The cleaned string without code block markers.
    """
    lines = text.strip().split("\n")

    if lines and lines[0].startswith(f"```{language}"):
        lines = lines[1:]
    else:
        print("Warning: The input does not start with the expected code block marker.")

    if lines and lines[-1].strip() == "```":
        lines = lines[:-1]
    else:
        print("Warning: The input does not end with the expected code block marker.")

    cleaned_text = "\n".join(lines)
    return cleaned_text


def error_checking_agent(
    subject: str,
    code: str,
    err: str,
):
    system_instruction = (
        """
    You are a checking agent that checks Manim python code with errors which is meant to explain the concept of """
        + subject
        + """ through an animation.
    You are given the manim code used to generate the video and an error associated with the code. Your job is to correct the manim code so the video
    is generated and as intended without any errors. You must make sure that the concept is explained properly with an appropriate voiceover. 
    Also make sure all elements are in the screen.
    You will only return manim code. Do not explain anything. Only return the code.
    """
    )
    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )

    content = (
        """This is the code:\n\n""" + code + """\n\nThis is the error:\n\n""" + err
    )

    response = model.generate_content(content)
    return response.text


def video_checking_agent(video: str, code: str, metadata):
    video_file = Part.from_uri(
        uri=video,
        mime_type="video/mp4",
    )
    system_instruction = (
        """
    You are a quality assurance agent that reviews Manim python code and the video it generates. The video is meant to explain the concept of """
        + metadata["title"]
        + """.
    You have to make sure the concept is explained properly through the video.
    If the video has any elements that are being drawn on top of each other or are not clearly visiible, your job is the correct the Manim python code. 
    If you believe the video has no issues, you can return the exact same code without any changes.
    You are given the Manim code that was used to generate the video, the video that was generated, and a json containing the following fields:
    - The 'title' field is a short title of the concept you are making the animation for.
    - The 'images' field is a dictionary with keys being names of daily object used in the animation (e.g., 'football', 'apple') and values are the relative path to the images.
    - The 'srt' field is a string containing the speech transcriptions for each respective step and the timestamps for the voiceover.
    - The 'info' field is the most important field you should pay attention to. It contains about exactly how to animate the elements. Try to adhere to what it says and make sure all elements are visible in the screen.
    You must make sure that the concept is explained properly.
    You will only return python Manim code. Do not explain anything. Only return the revised code file.
    """
    )
    contents = [
        video_file,
        "The video is attached and here is the code used to generate the video:" + code,
    ]
    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )

    response = model.generate_content(contents)
    return response.text


def download_images(metadata: str):
    metadata = json.loads(remove_code_block_markers(metadata))
    images = metadata["images"]
    for key in images:
        if images[key] is not None:
            url = images[key]
            os.makedirs("./backend/output", exist_ok=True)
            image_name = url.split("/")[-1]
            image_path = os.path.join("./backend/output", image_name)
            response = requests.get(url)
            if response.status_code == 200:
                with open(image_path, "wb") as file:
                    file.write(response.content)
                print(f"Image saved to {image_path}")
                metadata["images"][key] = f"./{image_name}"
            else:
                print(f"Failed to download image. Status code: {response.status_code}")
    metadata = json.dumps(metadata)
    return metadata


def final_flow(prompt, callback=None):
    try:
        if callback:
            callback("Planning the video...")
        initial_check = steps_agent(prompt)
        next_check = remove_code_block_markers(initial_check, "json")
        step_json = json.loads(next_check)
        clone_json = copy.deepcopy(step_json)
        del clone_json["srt"]
        del clone_json["title"]
        if callback:
            callback("Reviewing the plan and generating voiceover...")
        changed_images = steps_checking_agent(json.dumps(clone_json, indent=2))
        changed_images = remove_code_block_markers(changed_images, "json")
        changed_json = json.loads(changed_images)
        step_json["images"] = changed_json["images"]
        step_json["info"] = changed_json["info"]
        if callback:
            callback("Generating images using ImageGen3...")
        next_check = main(step_json)
        print(next_check)
        if callback:
            callback("Downloading images...")
        final_metadata = download_images(next_check)
        print(final_metadata)
        if callback:
            callback("Generating Manim code...")
        code = manimator(final_metadata)
    except Exception as e:
        print(f"Error generating video: {e}")
        print("Retrying...")
        return final_flow(prompt)
    if callback:
        callback("Source code generated successfully.")
    return (final_metadata, code)


# if __name__ == "__main__":
#     print(final_flow("multiplication"))


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


# def audio_agent(prompt: str):

#     system_instruction = """
#     You are master trascriber assistant that generates beautiful and extremely cohesive and clear speech transcripts based on the steps provided:

#     **Your Task:**

#     - **Input:** You will receive a JSON object with three fields: 'title', 'images', and 'steps'
#     - The 'title' field is a high level description or overarching topic of what the prompt is asking for. (e.g., if the prompt/explanation describes adding 2 sets of fruits, say 3 green apples to 5 red apples, the title would be 'addition')
#     - The `images` field is a dictionary where the keys are names of daily objects (e.g., 'apple', 'banana'). DO NOT WORRY ABOUT THIS DICTIONARY.
#     - The 'steps' field is a dictionary where the keys are the specific steps to generate speech transcriptions on. HOWEVER, THE VALUES CORRESPONDING TO EACH STEP WILL BE NULL. THESE VALUES ARE WHAT YOU NEED TO FILL WITH SPEECH TRANSCRIPTIONS (REFER TO OUTPUT GUIDELINES)
#     - Here is a sample of what the input would be for you to generate speech additions:
#         {
#             "title": "Subtraction",
#             "images": {
#                 "cookie": "https://storage.googleapis.com/path_to_cookie_image.png"
#             },
#             "steps" :
#             {
#                 "Step 1: Initialize a canvas of size 800x600 pixels." : null
#                 "Step 2: Set the size of each cookie to 40x40 pixels." : null
#                 "Step 3: Add 5 cookies horizontally, starting at coordinates (100, 300) with 50 pixel spacing between each cookie." : null
#                 "Step 4: Apply a fade-in effect lasting 0.5 seconds for all five cookies." : null
#                 "Step 5: Add a minus sign at coordinates (450, 300) with a size of 50x50 pixels." : null
#                 "Step 6: Add the number '5' at coordinates (300, 200) with a font size of 48px bold." : null
#                 "Step 7: Add the number '2' at coordinates (550, 200) with a font size of 48px bold." : null
#                 "Step 8: Move 2 cookies starting from the rightmost cookie upwards from (300, 300) to (300, 100) one after the other with 0.5 seconds delay between each cookie and a fade-out effect over 0.3 seconds.": null
#                 "Step 9: Apply a scale-in effect to the minus sign over 0.3 seconds." : null
#                 "Step 10: Add an equals sign at coordinates (450, 200) with a size of 50x50 pixels and apply a fade-in effect over 0.5 seconds." : null
#                 "Step 11: Add the number '3' at coordinates (450, 100) with a font size of 48px bold and apply a fade-in effect over 0.5 seconds." : null
#             }
#         }


#     **Output**:
#     - Each step (key) in the 'steps' field has a corresponding value. This value is a transcript in speech format for a one-person voiceover with timestamps explaining a concept. Objects from the `images` dictionary used in the text are denoted by `_*object_name*_`.
#     - The output should be a JSON response that is the same as the input but includes the speech transcriptions for each respective step.


#     Your JSON output will have these fields:
#     - The 'title' field is a short title of the concept you are making the animation for (given in the input).
#     - The 'images' field is a dictionary with keys being names of daily object used in the animation (e.g., 'football', 'apple') and values being null (given in the input).
#     - The 'steps' field is a dictionary with keys being each step you take to make animation (given in the input) and the corresponding speech transcriptions (intended output).

#     GUIDELINES FOR SPEECH OUTPUT GENERATION:
#     - Based on the title, which is the overarching concept of the explanation, build a framework/reference for the larger topic of the speech transcriptions in totality.
#     - When generating the SPEECH transcriptions, ensure that they are for each step in the 'steps' key field, and correspond and flow logically.
#     - When generating the SPEECH transcriptions, ensure that it does NOT mention pixels, or coordinates. THESE TRANSCRIPTIONS MUST EXPLAIN CONCEPTS AND TOPICS AT A HIGH LEVEL.
#     - Focus on generating SPEECH transcriptions that synthesizes each steps based on the provided title and explains the steps in a conceptual manner and in a way that is being asked for and is very easy to comprehend and understand.


#     Here is a sample output:
#     {
#         "title" : "Subtraction",
#         "images" :
#         {
#             "cookie": "https://storage.googleapis.com/path_to_cookie_image.png"
#         },
#         "steps" :
#         {
#             "Step 1: Initialize a canvas of size 800x600 pixels." : "Let's explore subtraction.",
#             "Step 2: Set the size of each cookie to 40x40 pixels." : "Imagine you have a plate with 5 cookies on it.",
#             "Step 3: Add 5 cookies horizontally, starting at coordinates (100, 300) with 50 pixel spacing between each cookie." : "Each cookie represents one item in our total count.",
#             "Step 4: Apply a fade-in effect lasting 0.5 seconds for all five cookies." : "Now, let’s say you eat 2 of these cookies. .",
#             "Step 5: Add a minus sign at coordinates (450, 300) with a size of 50x50 pixels." : "We’ll start by taking away 2 cookies from the plate..",
#             "Step 6: Add the number '5' at coordinates (300, 200) with a font size of 48px bold." : "As each cookie is removed, our total number of cookies decreases.",
#             "Step 7: Add the number '2' at coordinates (550, 200) with a font size of 48px bold." : "After removing 2 cookies, let’s count how many are left.",
#             "Step 8: Move 2 cookies starting from the rightmost cookie upwards from (300, 300) to (300, 100) one after the other with 0.5 seconds delay between each cookie and a fade-out effect over 0.3 seconds.": "We began with 5 cookies and removed 2.",
#             "Step 9: Apply a scale-in effect to the minus sign over 0.3 seconds." : "Now, there are 3 cookies left on the plate. ",
#             "Step 10: Add an equals sign at coordinates (450, 200) with a size of 50x50 pixels and apply a fade-in effect over 0.5 seconds." : "This shows that 5 minus 2 equals 3",
#             "Step 11: Add the number '3' at coordinates (450, 100) with a font size of 48px bold and apply a fade-in effect over 0.5 seconds." : "You now have 3 cookies left!"
#         }
#     }

#     """
#     model = GenerativeModel(
#         model_name="gemini-1.5-pro", system_instruction=system_instruction
#     )


#     response = model.generate_content(prompt)
#     return response.text
