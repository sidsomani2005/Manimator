import vertexai
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv


load_dotenv()

vertexai.init(project=os.getenv("PROJECT_ID"), location="us-central1")



def load_guidelines():
    with open("manim_docs.md", "r") as f:
        guidelines = f.read()
    return guidelines


def manimator(data: str):
    

    system_instruction = """
    You are an assistant that generates Manim Python code to create animations with synchronized voiceovers. Use updated Manim libraries and features to create engaging visual content for educational purposes.

    **Your Task:**

    - **Input:** You will receive a JSON object with three fields: 'title', 'images', and 'steps'
    - The 'title' field is a high level description or overarching topic of what the prompt is asking for. (e.g., if the prompt/explanation describes adding 2 sets of fruits, say 3 green apples to 5 red apples, the title would be 'addition')
    - The `images` field is a dictionary where the keys are names of daily objects (e.g., 'apple', 'banana') and the values are links to images stored in GCP buckets.
    - The 'steps' field is a dictionary where the keys are the specific steps to generate code on, and the corresponding value is a transcript in speech  format for a one-person voiceover with timestamps explaining a concept. Objects from the `images` dictionary used in the text are denoted by `_*object_name*_`. 
    - A sample JSON file that the code needs to be generated on is as follows: 
    {
        'title' : "Subtraction",
        'images' : 
        {
            'cookie': "https://storage.googleapis.com/mani_image_buckets/cookie.png"
        },
        'steps' : 
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

    
    - **Output:** Generate Manim code that:
    - Creates animations that illustrate each step described in each of the key values of the 'steps' field. So in the JSON file for the 'steps' field, create the animation code based on what the steps are.
    - The code generated should provide an animation that sequentially depicts each step in chronological order. e.g., the animation must flow sequentially from step 1 to step 2, and so on. The animations should reflect the correct steps of steps as they appear in the dictionary.
    - Incorporates the images provided in the `images` dictionary whenever they are mentioned in the text.
    - If a image link is not provided, or is 'manim', this means that the code can be generates directly from the manim library - MEANING THAT THE CODE FOR THIS SHAPE WILL NEED TO BE WRITTEN. (e.g, 'images' : { 'apple' : 'manim' } means that the image for an apple NEEDS TO BE WRITTEN IN MANIM CODE BY THE MODEL ITSELF)
    - If the speech values for the 'steps' dictionary are null, then do nothing for the voice over for that step.
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


    **Manim Code Guidelines**
    - **Function Existence:** Verify that every function and class used in the generated code exists in the Manim library. If a step requires a function not present in the latest version, replace it with a valid alternative.
    - **VGroup:** VGroup DOES NOT EXIST - DO NOT USE THIS FUNCTION ALWAYS REPLAE WITH ALTERNATIVES THAT ACTUALLY EXIST IN THE MANIM LIBRARY
    - **Syntax Accuracy:** Ensure that the generated Python code is syntactically correct.
    - **Images:** The images in the JSON field 'images' must be either 'manim' or google cloud storage links. If they are 'manim', you must generate manim code to provide an alternative animation/shape that can represent the intended image.
    - **Variable Definitions:** All variables must be defined before they are used in animations.
    - **Comments:** Include inline comments for clarity, explaining what each part of the code does without excessive verbosity.
    - **Voiceover Integration:** Ensure that voiceovers are synchronized with the animation steps using Manim's VoiceOver feature.


    """

    model = GenerativeModel(
        model_name="gemini-1.5-pro", system_instruction=system_instruction
    )

    guidelines = load_guidelines()
    response = model.generate_content([data, guidelines])
    return response.text



if __name__ == "__main__":
    data ="""
    {
            'title' : "Subtraction",
            'images' : 
            {
                'cookie': "https://storage.googleapis.com/mani_image_buckets/cookie.png"
            },
            'steps' : 
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
    print(manimator(data))




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