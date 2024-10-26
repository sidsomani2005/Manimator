from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class Subtraction(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        # Step 1: Initialize a canvas of size 800x600 pixels.
        self.camera.background_color = WHITE  # Set background color to white
        # "Let's explore subtraction."
        with self.voiceover(text="Let's explore subtraction."):
            self.wait(1)
        
        # Step 2: Set the size of each cookie to 40x40 pixels.
        cookie_size = 0.5
        # "Imagine you have a plate with 5 cookies on it."
        with self.voiceover(text="Imagine you have a plate with 5 cookies on it."):
            self.wait(1)

        # Step 3: Add 5 cookies horizontally, starting at coordinates (100, 300) with 50 pixel spacing between each cookie.
        cookies = VGroup(*[ImageMobject("banana.png").scale(cookie_size) for _ in range(5)])\
            .arrange(RIGHT, buff = 0.7)
        # "Each cookie represents one item in our total count."
        with self.voiceover(text="Each cookie represents one item in our total count."):
            self.play(FadeIn(cookies))

        # Step 4: Apply a fade-in effect lasting 0.5 seconds for all five cookies.
        # "Now, let’s say you eat 2 of these cookies. ."
        with self.voiceover(text="Now, let’s say you eat 2 of these cookies."):
            self.wait(1)

        # Step 5: Add a minus sign at coordinates (450, 300) with a size of 50x50 pixels.
        minus_sign = Text("-").scale(2).move_to(2.5 * RIGHT)
        # "We’ll start by taking away 2 cookies from the plate.."
        with self.voiceover(text="We’ll start by taking away 2 cookies from the plate."):
            self.play(FadeIn(minus_sign))

        # Step 6: Add the number '5' at coordinates (300, 200) with a font size of 48px bold.
        number_5 = Text("5").scale(1.5).move_to(0.5 * RIGHT + UP)
        # "As each cookie is removed, our total number of cookies decreases."
        with self.voiceover(text="As each cookie is removed, our total number of cookies decreases."):
            self.play(FadeIn(number_5))
        
        # Step 7: Add the number '2' at coordinates (550, 200) with a font size of 48px bold.
        number_2 = Text("2").scale(1.5).move_to(3.5 * RIGHT + UP)
        # "After removing 2 cookies, let’s count how many are left."
        with self.voiceover(text="After removing 2 cookies, let’s count how many are left."):
            self.play(FadeIn(number_2))

        # Step 8: Move 2 cookies starting from the rightmost cookie upwards from (300, 300) to (300, 100) one after the other with 0.5 seconds delay between each cookie and a fade-out effect over 0.3 seconds.
        # "We began with 5 cookies and removed 2."
        with self.voiceover(text="We began with 5 cookies and removed 2."):
            self.play(FadeOut(cookies[3]), run_time=0.3)
            self.play(FadeOut(cookies[4]), run_time=0.3)

        # Step 9: Apply a scale-in effect to the minus sign over 0.3 seconds.
        # "Now, there are 3 cookies left on the plate. "
        with self.voiceover(text="Now, there are 3 cookies left on the plate."):
            self.play(ScaleInPlace(minus_sign, 1.2), run_time=0.3)
        
        # Step 10: Add an equals sign at coordinates (450, 200) with a size of 50x50 pixels and apply a fade-in effect over 0.5 seconds.
        equals_sign = Text("=").scale(2).move_to(2.5 * RIGHT + UP)
        # "This shows that 5 minus 2 equals 3."
        with self.voiceover(text="This shows that 5 minus 2 equals 3"):
            self.play(FadeIn(equals_sign))

        # Step 11: Add the number '3' at coordinates (450, 100) with a font size of 48px bold and apply a fade-in effect over 0.5 seconds.
        number_3 = Text("3").scale(1.5).move_to(2.5 * RIGHT)
        # "You now have 3 cookies left!"
        with self.voiceover(text="You now have 3 cookies left!"):
            self.play(FadeIn(number_3))