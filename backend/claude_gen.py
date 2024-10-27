import vertexai
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv
import json
from imagen import main
import requests

load_dotenv()
import copy
from anthropic import AnthropicVertex
import anthropic


vertexai.init(project=os.getenv("PROJECT_ID"), location="us-central1")
client = anthropic.Anthropic(api_key=os.getenv("ANTHROPIC_API"))


def steps_agent(prompt: str):
    system_instruction = """

        
    You are an assistant that generates SPECIFIC instructions for an animation that explains a particular concept and returns JSON response consisting of "titles", "images", "srt", and "info" fields.

    - The "title" field is a short title of the concept you are making the animation for. (eg Addition, Subtraction, EigenValues) Be super concise and direct.
    - The "images" field is a dictionary with keys being names of objects used in the explanation and values being null.
    - The "info" field is a dictionary with keys being the timestamps for the voiceover and values being steps on how to draw and animate the concept being explained at that timestamp. Adhere to mathematical logic and physics. 
      If there are no concepts being explained at a timestamp, then the value should be an empty string. USE AS MANY STEPS AS YOU NEED. 
    - The "srt" field is a transcript in an SRT format for a one-person voiceover with timestamps explaining the concept.

   
      

    Your task is to take the user's prompt and generate a JSON response as per the format above.
    When it comes to deciding the images, if you believe the overall task is complicated assign all the values as "Manim", else use daily objects and keep the value as null.

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
    MAKE SURE YOU OUTPUT A VALID JSON

    """

    message = (
        client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=1024,
            system=system_instruction,
            messages=[{"role": "user", "content": prompt}],
        ),
    )

    return message[0].content[0].text


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
        1) If you find any key in the images dictionary that SAID as a mathematical shape (arrow, circle, square) replace their value with "Manim". DO NOT ADD ANY IMAGES TO THE DICTIONARY
        2) After all checks for the image dictionary are completed you will go to the info dictionary and see where the any of the objects which are keys in the images dictionary are being used. Once found replace them with *_<objectkey>_* where objectkey is the actual key from the images dictionary.

    You will then return the updated json.

    """
    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )

    response = model.generate_content(prompt)
    return response.text


def load_references():
    with open("reference_db.md", "r") as f:
        references = f.read()
    return references


def manimator(data: str):
    system_instruction = """
    You are professional at Manim (0.18.1) a python library used to make animations. 
    You have the entire manim library at your disposal. Feel free to check the internet manim documentation: https://docs.manim.community/en/stable/ for any confusion you might have.

    **Your Task:**

    - **Input:** You will receive a JSON object with three fields: 'title', 'images', and 'steps'
    - The 'title' field is a short title of the concept you are making the animation for. (eg Addition, Subtraction, EigenValues) Be super concise and direct.
    - The 'images' field is a dictionary with keys being names of daily object used in the explanation (e.g., 'apple', 'banana') and values are either the GCP link to the image or the word "Manim".
    - The 'srt' field is a transcript in an SRT format for a one-person voiceover with timestamps explaining the concept. 
    - The 'info' field is a dictionary with keys being the timestamps from the generated SRT file and values being detailed steps on how to draw and animate the concept being explained at that timestamp. For example, when explaining projectile motion,
      there could be a step to draw a ball at the top of the screen and animate it moving downwards in a parabolic path. In your steps, use the images that were generated above. Adhere to mathematical logic and physics. If there are no concepts being explained at a timestamp, then the value should be an empty string.
    - A sample JSON file input would look like: 
    {
        "title": "<Title present>",
        "images": {
            "<Any Item>": null
            <more as present>,
        },
        "srt": {
        <given srt>
        },
        "info":{
            "<timestamp1>":<Action>,
            <more as present>,
        }
        
    }
    
    - **Output:** Generate Manim code that:
    - Generate Manim code that performs A SIMPLE animation detailed in info with a voiceover from the srt.
    - The code generated should provide an animation that sequentially depicts each step in chronological order. 
    - Incorporates the images provided in the `images` dictionary whenever they are mentioned in the text. You must SCALE THEM RELATIVELY SINCE THEY ARE ALL OF THE SAME SIZE.
    - If a image link is not provided, or is 'Manim', this means that the code can be generates directly from the manim library - MEANING THAT THE CODE FOR THIS SHAPE WILL NEED TO BE WRITTEN. (e.g, 'images' : { 'apple' : 'manim' } means that the image for an apple NEEDS TO BE WRITTEN IN MANIM CODE BY THE MODEL ITSELF)
    - When an object denoted by `_*object_name*_` appears in the transcript, display the corresponding image using the provided GCP bucket link.
    - Synchronizes the animations with the voiceover using Manim's VoiceOver feature.
   

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


    **CRITICAL GUIDELINES: MUST FOLLOW**
    - **DO NOT USE VGROUP**
    - **USE THE LATEST MANIM VERSION**
    - **TRY AND MINIMIZE REPITITION IN YOUR SPEECH**
    - **DO NOT USE EMOJIS OR SPECIAL UNICODE OR ASCII CHARACTERS**
    - **EVERYTHING MUST BE COMPATIBLE WITH UTF-8 ENCODING**
    - **MAKE SURE THE CODE WORKS**
    - **DO NOT USE ANY IMAGES OTHER THAN THE ONES IN THE IMAGE DICTIONARY PROVIDED**
    - **DO NOT ADD ANY AUDIO OTHER THAN THE VOICEOVER**
    - **Color Code:** ENSURE THAT THE BACKGROUND IS ALWAYS WHITW AND THE TEXT IS ALWAYS BLACK.
    - **Sequence of image/text:** ensure that the text is of slightly smaller font size ALWAYS and NEVER overlaps with the other images. THIS IS EXTREMELY IMPORTANT - ESPECIALLY THE OVERLAP ISSUE.
    - **Object Sizing:** SCALE EACH IMAGE RELATIVELY SINCE THEY ARE OF THE SAME SIZE.
    - **Object Placement:** Make sure each object is placed properly relative to other objects and nothing overlaps.
    - **Mathematical Equations:** if mathematical or arithmetic equations are being written in text, POSITION THEM AWAY FROM OTHER OBJECTS AND KEEP THEM IN ONE HORIZONTAL LINE - ENSURE THAT THEY DONT TRAIL OFF THE END OF THE CANVAS.

   
    """

    message = (
        client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=3000,
            system=system_instruction,
            messages=[{"role": "user", "content": data}],
        ),
    )
    return message[0].content[0].text


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
    system_instruction_previous = """
    You are professional at Manim (0.18.1) a python library used to make animations. 
    You have the entire manim library at your disposal. Feel free to check the internet manim documentation: https://docs.manim.community/en/stable/ for any confusion you might have.

    **Your Task:**

    - **Input:** You will receive a JSON object with three fields: 'title', 'images', and 'steps'
    - The 'title' field is a short title of the concept you are making the animation for. (eg Addition, Subtraction, EigenValues) Be super concise and direct.
    - The 'images' field is a dictionary with keys being names of daily object used in the explanation (e.g., 'apple', 'banana') and values are either the GCP link to the image or the word "Manim".
    - The 'srt' field is a transcript in an SRT format for a one-person voiceover with timestamps explaining the concept. 
    - The 'info' field is a dictionary with keys being the timestamps from the generated SRT file and values being detailed steps on how to draw and animate the concept being explained at that timestamp. For example, when explaining projectile motion,
      there could be a step to draw a ball at the top of the screen and animate it moving downwards in a parabolic path. In your steps, use the images that were generated above. Adhere to mathematical logic and physics. If there are no concepts being explained at a timestamp, then the value should be an empty string.
    - A sample JSON file input would look like: 
    {
        "title": "<Title present>",
        "images": {
            "<Any Item>": null
            <more as present>,
        },
        "srt": {
        <given srt>
        },
        "info":{
            "<timestamp1>":<Action>,
            <more as present>,
        }
        
    }
    
    - **Output:** Generate Manim code that:
    - Generate Manim code that performs A SIMPLE animation detailed in info with a voiceover from the srt.
    - The code generated should provide an animation that sequentially depicts each step in chronological order. 
    - Incorporates the images provided in the `images` dictionary whenever they are mentioned in the text. You must SCALE THEM RELATIVELY SINCE THEY ARE ALL OF THE SAME SIZE.
    - If a image link is not provided, or is 'Manim', this means that the code can be generates directly from the manim library - MEANING THAT THE CODE FOR THIS SHAPE WILL NEED TO BE WRITTEN. (e.g, 'images' : { 'apple' : 'manim' } means that the image for an apple NEEDS TO BE WRITTEN IN MANIM CODE BY THE MODEL ITSELF)
    - When an object denoted by `_*object_name*_` appears in the transcript, display the corresponding image using the provided GCP bucket link.
    - Synchronizes the animations with the voiceover using Manim's VoiceOver feature.
   

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


    **CRITICAL GUIDELINES: MUST FOLLOW**
    - **DO NOT USE VGROUP**
    - **USE THE LATEST MANIM VERSION**
    - **TRY AND MINIMIZE REPITITION IN YOUR SPEECH**
    - **DO NOT USE EMOJIS OR SPECIAL UNICODE OR ASCII CHARACTERS**
    - **EVERYTHING MUST BE COMPATIBLE WITH UTF-8 ENCODING**
    - **MAKE SURE THE CODE WORKS**
    - **DO NOT USE ANY IMAGES OTHER THAN THE ONES IN THE IMAGE DICTIONARY PROVIDED**
    - **DO NOT ADD ANY AUDIO OTHER THAN THE VOICEOVER**
    - **Color Code:** ENSURE THAT THE BACKGROUND IS ALWAYS WHITW AND THE TEXT IS ALWAYS BLACK.
    - **Sequence of image/text:** ensure that the text is of slightly smaller font size ALWAYS and NEVER overlaps with the other images. THIS IS EXTREMELY IMPORTANT - ESPECIALLY THE OVERLAP ISSUE.
    - **Object Sizing:** SCALE EACH IMAGE RELATIVELY SINCE THEY ARE OF THE SAME SIZE.
    - **Object Placement:** Make sure each object is placed properly relative to other objects and nothing overlaps.
    - **Mathematical Equations:** if mathematical or arithmetic equations are being written in text, POSITION THEM AWAY FROM OTHER OBJECTS AND KEEP THEM IN ONE HORIZONTAL LINE - ENSURE THAT THEY DONT TRAIL OFF THE END OF THE CANVAS.

   
    """
    system_instruction = (
        (
            """
    You are a checking agent that checks Manim python code with errors which is meant to explain the concept of """
            + subject
            + """ through an animation.
    You are given the manim code used to generate the video and an error associated with the code. Your job is to correct the manim code so the video
    is generated and as intended without any errors. You must make sure that the concept is explained properly with an appropriate voiceover. 
    Also make sure all elements are in the screen.
    You will only return manim code. Do not explain anything. Only return the code.
    These were the instructions given to the model that generated the code. Follow the guidelines given to it:\n
    """
        )
        + system_instruction_previous
    )
    content = (
        """This is the code:\n\n""" + code + """\n\nThis is the error:\n\n""" + err
    )

    message = (
        client.messages.create(
            model="claude-3-5-sonnet-20241022",
            max_tokens=3000,
            system=system_instruction,
            messages=[{"role": "user", "content": content}],
        ),
    )

    return message[0].content[0].text


def download_images(metadata: str):
    metadata = json.loads(remove_code_block_markers(metadata))
    images = metadata["images"]
    for key in images:
        if images[key] is not None and images[key] != "Manim":
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
                print(f"Failed to download image from {url}")
    metadata = json.dumps(metadata)
    return metadata


def final_flow(prompt):
    try:
        initial_check = steps_agent(prompt)
        step_json = json.loads(initial_check)
        clone_json = copy.deepcopy(step_json)
        del clone_json["srt"]
        del clone_json["title"]
        changed_images = steps_checking_agent(json.dumps(clone_json, indent=2))
        changed_images = remove_code_block_markers(changed_images, "json")
        changed_json = json.loads(changed_images)
        step_json["images"] = changed_json["images"]
        step_json["info"] = changed_json["info"]
        next_check = main(step_json)
        final_metadata = download_images(next_check)
        code = manimator(final_metadata)
        print("Code generated successfully")
        print(code, final_metadata)
    except Exception as e:
        print(f"Error generating video: {e}")
        print("Retrying...")
        return final_flow(prompt)

    return (final_metadata, code)
