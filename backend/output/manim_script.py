from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService
import requests
import os


class Subtraction(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Step 1: Initialize a canvas of size 800x600 pixels.
        self.camera.background_color = WHITE  # Set background color to white

        with self.voiceover(text="Let's explore subtraction.") as tracker:
            self.wait(tracker.duration)

        # Step 2: Set the size of each cookie to 40x40 pixels.
        cookie_size = 0.5

        # Step 3: Download the image from the URL
        url = "https://storage.googleapis.com/mani_image_buckets/cookie.png"
        image_path = "cookie.png"

        # Check if the image is already downloaded to avoid redundant downloads
        if not os.path.exists(image_path):
            response = requests.get(url)
            with open(image_path, "wb") as file:
                file.write(response.content)

        with self.voiceover(
            text="Imagine you have a plate with 5 cookies on it."
        ) as tracker:
            self.wait(tracker.duration)

        # Step 4: Add 5 cookies horizontally
        cookies = Group(
            *[ImageMobject(image_path).scale(cookie_size) for _ in range(5)]
        ).arrange(RIGHT, buff=1)
        cookies.move_to(DOWN)

        with self.voiceover(
            text="Each cookie represents one item in our total count."
        ) as tracker:
            self.play(FadeIn(cookies), run_time=tracker.duration)

        # Step 5: Continue with the rest of the animation
        minus_sign = Text("-").scale(2).move_to(2 * RIGHT)

        with self.voiceover(
            text="Now, let’s say you eat 2 of these cookies."
        ) as tracker:
            self.play(FadeIn(minus_sign), run_time=tracker.duration)

        number_5 = Text("5", font_size=48, weight=BOLD).next_to(cookies, UP, buff=1.5)

        with self.voiceover(
            text="As each cookie is removed, our total number of cookies decreases."
        ) as tracker:
            self.play(FadeIn(number_5), run_time=tracker.duration)

        number_2 = Text("2", font_size=48, weight=BOLD).next_to(
            minus_sign, UP, buff=1.5
        )

        with self.voiceover(
            text="After removing 2 cookies, let’s count how many are left."
        ) as tracker:
            self.play(FadeIn(number_2), run_time=tracker.duration)

        # Step 8: Remove 2 cookies
        with self.voiceover(text="We began with 5 cookies and removed 2.") as tracker:
            self.play(
                cookies[-1].animate.shift(UP * 3).set_opacity(0),
                cookies[-2].animate.shift(UP * 3).set_opacity(0),
                run_time=tracker.duration,
            )

        with self.voiceover(
            text="Now, there are 3 cookies left on the plate."
        ) as tracker:
            self.play(ApplyMethod(minus_sign.scale, 1.2), run_time=tracker.duration)

        equals_sign = Text("=").scale(2).move_to(2 * RIGHT).shift(DOWN)

        with self.voiceover(text="This shows that 5 minus 2 equals 3") as tracker:
            self.play(FadeIn(equals_sign), run_time=tracker.duration)

        number_3 = Text("3", font_size=48, weight=BOLD).next_to(
            equals_sign, UP, buff=1.5
        )

        with self.voiceover(text="You now have 3 cookies left!") as tracker:
            self.play(FadeIn(number_3), run_time=tracker.duration)

        self.wait()

        # Optional: Clean up the downloaded image file after rendering
        if os.path.exists(image_path):
            os.remove(image_path)
