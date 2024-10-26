from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class MultiplicationExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Placeholders for images. Replace with actual image loading from GCP.
        cookie_img = ImageMobject("cookie.png").scale(0.5) # Replace "cookie.png" with actual path or URL
        box_img = ImageMobject("box.png").scale(0.7) # Replace "box.png" with actual path or URL

        # Create cookie objects
        cookie1 = cookie_img.copy().shift(LEFT * 2)
        cookie2 = cookie_img.copy()
        cookie3 = cookie_img.copy().shift(RIGHT * 2)

        # Animation for the first sentence
        with self.voiceover(text="Multiplication is like a shortcut for adding the same number over and over again. Let's imagine we have some _cookies_.") as tracker:
            self.play(FadeIn(cookie1), FadeIn(cookie2), FadeIn(cookie3))

        # Create boxes and arrange cookies inside
        box1 = box_img.copy().shift(LEFT * 3)
        box2 = box_img.copy()
        box3 = box_img.copy().shift(RIGHT * 3)

        with self.voiceover(text="Let's say we have 3 _boxes_, and each _box_ has 4 _cookies_ inside.") as tracker:
            self.play(FadeIn(box1), FadeIn(box2), FadeIn(box3))
            self.play(cookie1.animate.move_to(box1.get_center()),
                       cookie2.animate.move_to(box2.get_center()),
                       cookie3.animate.move_to(box3.get_center()))
            # Duplicate and position remaining cookies
            for i in range(3):
                new_cookie = cookie_img.copy()
                self.play(FadeIn(new_cookie.move_to(box1.get_center() + (i + 1) * UP * 0.5)))
            for i in range(3):
                new_cookie = cookie_img.copy()
                self.play(FadeIn(new_cookie.move_to(box2.get_center() + (i + 1) * UP * 0.5)))
            for i in range(3):
                new_cookie = cookie_img.copy()
                self.play(FadeIn(new_cookie.move_to(box3.get_center() + (i + 1) * UP * 0.5)))

        # Animation for the third and fourth sentences
        equation = MathTex("3 \\times 4 = 12").shift(DOWN * 2)
        with self.voiceover(text="So, we have 3 groups of 4 _cookies_. Instead of adding 4+4+4, we can multiply 3 times 4.") as tracker:
            self.play(Create(equation))
        with self.voiceover(text="3 times 4 simply means we are adding 4 to itself 3 times. And guess what? 3 times 4 equals 12, which means we have a total of 12 _cookies_.") as tracker:
            pass  # No animation needed here, but you can add visual emphasis if desired

        # Animation for the last sentence
        with self.voiceover(text="That's it! Multiplication makes it much faster to count when we have groups of the same size.") as tracker:
            self.play(FadeOut(box1), FadeOut(box2), FadeOut(box3), FadeOut(equation),
                       *[FadeOut(mob) for mob in self.mobjects if isinstance(mob, ImageMobject)])

        self.wait()