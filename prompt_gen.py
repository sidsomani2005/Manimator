import vertexai
from vertexai.generative_models import GenerativeModel
import os
from dotenv import load_dotenv

load_dotenv()

vertexai.init(project=os.getenv("PROJECT_ID"), location="us-central1")


def main_prompt(prompt: str):
    system_instruction = """
    You are an assistant that generates a JSON response consisting of 'images' and 'text' fields to explain a concept provided in the user prompt in as simple a way as possible with as many details as possible.
    You should explain the concept like you would to a 12 year old.

    - The 'images' field is a dictionary with keys being names of daily object used in the explanation (e.g., 'apple', 'banana') and values being None.
    - The 'text' field is a transcript in an SRT format for a one-person voiceover with timestamps explaining the concept. Everytime you use an object which is stored in images it must start with _* and end with *_.

    Your task is to take the user's prompt and generate a JSON response as per the format above, using simple daily objects in the explanation.
    """
    model = GenerativeModel(
        model_name="gemini-1.5-flash", system_instruction=system_instruction
    )

    response = model.generate_content(prompt)
    return response.text


def manimator(data: str):
    system_instruction = """
    You are an assistant that generates Manim Python code to create animations with synchronized voiceovers. Use updated Manim libraries and features to create engaging visual content for educational purposes.

    **Your Task:**

    - **Input:** You will receive a JSON object with two fields: `images` and `text`.
    - The `images` field is a dictionary where the keys are names of daily objects (e.g., 'apple', 'banana') and the values are links to images stored in GCP buckets.
    - The `text` field is a transcript in SRT format for a one-person voiceover with timestamps explaining a concept. Objects from the `images` dictionary used in the text are denoted by `_*object_name*_`.

    - **Output:** Generate Manim code that:
    - Creates animations illustrating the concepts described in the `text` field.
    - Incorporates the images provided in the `images` dictionary whenever they are mentioned in the text.
    - When an object denoted by `_*object_name*_` appears in the transcript, display the corresponding image using the provided GCP bucket link.
    - Synchronizes the animations with the voiceover using Manim's VoiceOver feature.

    **Guidelines:**

    1. **Manim Scene Structure:**
    - Define a `Scene` class that contains all the animations.
    - Use appropriate Manim modules and classes to create visual elements (for example: `ImageMobject`, `Text`, `SVGMobject`, but it does not have to be these exact elements).

    2. **VoiceOver Integration:**
    - Utilize Manim's `self.record_voiceover` features to add the voiceover script.
    - Ensure the timings in the SRT transcript are synchronized with the animations.

    3. **Handling Images:**
    - For each object in the `images` dictionary:
    - Load the image using the provided GCP bucket link with an element similar to `ImageMobject('path_or_url_to_image')`.
    - Ensure you have access to download or fetch the image from the GCP bucket.
    - Include any necessary code or comments for handling authentication if required (e.g., using service account credentials).

    4. **Animating Text and Objects:**
    - Display text on the screen when appropriate, using the `Text` or `Tex` classes.
    - Animate the objects mentioned in the transcript at the correct timestamps.
    - Use simple animations (e.g., `FadeIn`, `MoveTo`, `Rotate`) to engage a 12-year-old audience.
    - If the transcript mentions text in the format of "_*example*_", make sure to display the text as "example" in the voiceover.

    5. **Positioning Text and Objects:**
    - Be mindful about where the images and text are being rendered.
    - The images and text should never display on top of each other and should be clearly visible to the viewer
    - Keep all elements within the scene boundries at all times.

    6. **Code Formatting:**
    - Provide well-formatted and commented Python code.
    - Include necessary `import` statements and ensure the code is executable in a Manim environment.
    - Comment on any placeholders where credentials or additional setup might be needed.

    7. **Example Usage:**
    - If the transcript mentions "_*apple*_", display the apple image loaded from the GCP bucket at that point in the animation.
    - Use the timestamps to align animations with the voiceover.

    8. **Important Things to Do Before Responding:**
    - Review the code you have generated at least 3 times to ensure it runs without any errors.
    - During your review, guarantee that there are no elements outside of the page and that no elements' positions overlap.
    - Ensure that all animations and illustrations are drawn right-side up and move in a direction that makes sense in the context of the explanation.

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


if __name__ == "__main__":
    print(manimator(main_prompt("explain projectile motion")))
