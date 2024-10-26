from manim import *
from manim_voiceover import VoiceoverScene, VoiceoverTracker
from manim_voiceover.services.gtts import GTTSService
import os


class MultiplicationExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))

        # Placeholder for images - Replace with actual image loading from GCP
        cookie_img = os.path.join("./cookie.png")
        plate_img = os.path.join("./plate.png")

        cookie = ImageMobject(cookie_img).scale(0.3)
        plate = ImageMobject(plate_img).scale(0.5)

        # Positioning plates and cookies
        plate1 = plate.copy()
        plate2 = plate.copy().shift(2 * RIGHT)
        plate3 = plate.copy().shift(4 * RIGHT)

        cookie1 = cookie.copy().shift(0.2 * UP)
        cookie2 = cookie.copy().shift(0.2 * DOWN)
        cookie3 = cookie.copy().shift(0.2 * RIGHT)
        cookie4 = cookie.copy().shift(0.2 * LEFT)

        cookies_plate1 = Group(cookie1, cookie2, cookie3, cookie4)
        cookies_plate2 = cookies_plate1.copy().shift(2 * RIGHT)
        cookies_plate3 = cookies_plate1.copy().shift(4 * RIGHT)

        # Voiceover and animations
        with self.voiceover(
            text="Multiplication is like a shortcut for adding the same number over and over again."
        ) as tracker:
            self.wait(tracker.duration)

        with self.voiceover(
            text="Imagine you have a *_plate_* full of *_cookies_*."
        ) as tracker:
            self.play(FadeIn(plate1), FadeIn(cookies_plate1), run_time=tracker.duration)

        with self.voiceover(
            text="Let's say you have 3 *_plates_* and each *_plate_* has 4 *_cookies_* on it."
        ) as tracker:
            self.play(
                FadeIn(plate2),
                FadeIn(cookies_plate2),
                FadeIn(plate3),
                FadeIn(cookies_plate3),
                run_time=tracker.duration,
            )

        with self.voiceover(
            text="To find out how many *_cookies_* you have in total, you can use multiplication!"
        ) as tracker:
            self.wait(tracker.duration)

        with self.voiceover(
            text="Instead of adding 4 + 4 + 4, we can simply multiply 3 *_plates_* by 4 *_cookies_* per *_plate_*."
        ) as tracker:
            self.play(
                ApplyWave(plate1),
                ApplyWave(plate2),
                ApplyWave(plate3),
                ApplyWave(cookie1),
                ApplyWave(cookie2),
                ApplyWave(cookie3),
                ApplyWave(cookie4),
                run_time=tracker.duration,
            )

        with self.voiceover(
            text="So, 3 times 4, written as 3 x 4, equals 12. That means you have a total of 12 *_cookies_*!"
        ) as tracker:
            all_cookies = Group(cookies_plate1, cookies_plate2, cookies_plate3)
            self.play(Circle(all_cookies, color=YELLOW, run_time=tracker.duration))

        self.wait()
