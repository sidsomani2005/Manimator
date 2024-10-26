from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class Division(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Step 1: Initialize a canvas of size 800x600 pixels.

        with self.voiceover(text="Let's learn about division! Imagine we have a bunch of cookies that we want to divide equally."):
            self.wait()

        # Step 2: Set the size of each cookie to 40x40 pixels.
        cookie_size = 40

        # Step 3: Add plate 1 at coordinates (200, 200).
        plate1 = ImageMobject("plate.png").scale(0.5).move_to(np.array([-4, -1, 0]))
        with self.voiceover(text="We're going to use plates to help us divide the cookies. Here's our first plate."):
            self.play(FadeIn(plate1))

        # Step 4: Add plate 2 at coordinates (400, 200).
        plate2 = ImageMobject("plate.png").scale(0.5).move_to(np.array([0, -1, 0]))
        with self.voiceover(text="And here's our second plate."):
            self.play(FadeIn(plate2))

        # Step 5: Add plate 3 at coordinates (600, 200).
        plate3 = ImageMobject("plate.png").scale(0.5).move_to(np.array([4, -1, 0]))
        with self.voiceover(text="Finally, here's our third plate."):
            self.play(FadeIn(plate3))

        # Step 6: Add 6 cookies at coordinates (100, 300) with 5 pixel spacing.
        cookies = [ImageMobject("cookie.png").scale(0.1).move_to(np.array([-6 + i * 0.5, 1, 0])) for i in range(6)]
        with self.voiceover(text="We have six delicious cookies to divide."):
            self.play(*[FadeIn(cookie) for cookie in cookies])

        # Step 7: Apply a fade-in effect lasting 0.5 seconds for each object.

        # Step 8: Move 2 cookies from (100, 300) to (200, 200) over 0.7 seconds.
        with self.voiceover(text="Now, let's start dividing! We'll put two cookies on the first plate."):
            self.play(
                cookies[0].animate.move_to(plate1.get_center() + np.array([cookie_size / 4, cookie_size / 4, 0])),
                cookies[1].animate.move_to(plate1.get_center() + np.array([-cookie_size / 4, -cookie_size / 4, 0])),
                run_time=0.7
            )

        # Step 9: Move 2 cookies from (100, 300) to (400, 200) over 0.7 seconds.
        with self.voiceover(text="Next, we'll put two cookies on the second plate."):
            self.play(
                cookies[2].animate.move_to(plate2.get_center() + np.array([cookie_size / 4, cookie_size / 4, 0])),
                cookies[3].animate.move_to(plate2.get_center() + np.array([-cookie_size / 4, -cookie_size / 4, 0])),
                run_time=0.7
            )

        # Step 10: Move 2 cookies from (100, 300) to (600, 200) over 0.7 seconds.
        with self.voiceover(text="And finally, the last two cookies go on the third plate."):
            self.play(
                cookies[4].animate.move_to(plate3.get_center() + np.array([cookie_size / 4, cookie_size / 4, 0])),
                cookies[5].animate.move_to(plate3.get_center() + np.array([-cookie_size / 4, -cookie_size / 4, 0])),
                run_time=0.7
            )

        # Step 11: Apply an ease-in effect to the movement of the cookies.

        # Step 12: Add a text box displaying '6 / 3 = 2' at coordinates (350, 100).
        equation = Text("6 / 3 = 2").scale(0.8).move_to(np.array([0, -2, 0]))
        with self.voiceover(text="See how we divided 6 cookies into 3 groups and each plate has 2 cookies?"):
            self.play(Write(equation))

        # Step 13: Set the font size to 48px bold for the text.
        with self.voiceover(text="This shows us that 6 divided by 3 equals 2!"):
            self.wait()