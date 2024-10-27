from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class AdditionExample(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        # Step 1: Initialize a canvas of size 800x600 pixels.
        self.camera.background_color = BLACK  # Set background color to black
        
        # Step 2: Set the size of each apple to 40x40 pixels.
        apple_size = 0.5
        
        # Step 3: Add 3 apples horizontally, starting at coordinates (100, 300) with 50 pixel spacing between each apple.
        apple_spacing = 0.7
        apple_x_start = -2
        apple_y = 0
        apples = [ImageMobject("banana.png").scale(apple_size).move_to(
            [apple_x_start + i * apple_spacing, apple_y, 0]) for i in range(3)]
        
        # Step 4: Apply a fade-in effect lasting 0.5 seconds for all three apples.
        with self.voiceover(text="Let's explore addition."):
            self.wait()
        with self.voiceover(text="Imagine you have a basket with 3 apples."):
            self.play(FadeIn(*apples, lag_ratio=0.2), run_time=0.5)
        with self.voiceover(text="Each apple represents one item in our total count."):
            self.wait(2)

        # Step 5: Add a plus sign at coordinates (450, 300) with a size of 50x50 pixels.
        plus_sign = Text("+", font_size=48).scale(0.6).move_to([2, apple_y, 0])  # Adjust font size here

        # Step 6: Add the number '3' at coordinates (300, 200) with a font size of 48px bold.
        number_3 = Text("3", font_size=48, weight=BOLD).move_to([-1, -1, 0])  # Adjust font size here

        # Step 7: Add the number '2' at coordinates (550, 200) with a font size of 48px bold.
        number_2 = Text("2", font_size=48, weight=BOLD).move_to([3, -1, 0])  # Adjust font size here
        
        with self.voiceover(text="Now, let’s say you pick 2 more apples."):
            self.wait(2)
        with self.voiceover(text="We’ll start by adding 2 more apples to our basket."):
            self.play(FadeIn(plus_sign))
        with self.voiceover(text="As we add more apples, our total number of apples increases."):
            self.play(FadeIn(number_3))
        with self.voiceover(text="After picking 2 more apples, let’s count how many we have."):
            self.play(FadeIn(number_2))

        # Step 8: Move 2 apples starting from the rightmost cookie upwards from (300, 300) to (300, 100) one after the other with 0.5 seconds delay between each cookie and a fade-out effect over 0.3 seconds.
        new_apples = [ImageMobject("banana.png").scale(apple_size).move_to(
            [apple_x_start + (i + 3) * apple_spacing, apple_y, 0]) for i in range(2)]
        with self.voiceover(text="We began with 3 apples and added 2."):
            self.play(FadeIn(*new_apples, lag_ratio=0.2))
            self.play(*[apple.animate.move_to(
                [apple_x_start + i * apple_spacing, apple_y, 0]) for i, apple in enumerate(new_apples)], run_time=2)

        # Step 9: Apply a scale-in effect to the plus sign over 0.3 seconds.
        with self.voiceover(text="Now, there are 5 apples in total."):
            self.play(plus_sign.animate.scale(1.2), run_time=0.3)

        # Step 10: Add an equals sign at coordinates (450, 200) with a size of 50x50 pixels and apply a fade-in effect over 0.5 seconds.
        equals_sign = Text("=", font_size=48).scale(0.6).move_to([2, -1, 0])
        with self.voiceover(text="This shows that 3 plus 2 equals 5."):
            self.play(FadeIn(equals_sign), run_time=0.5)

        # Step 11: Add the number '5' at coordinates (450, 100) with a font size of 48px bold and apply a fade-in effect over 0.5 seconds.
        number_5 = Text("5", font_size=48, weight=BOLD).move_to([3, -2, 0])
        with self.voiceover(text="You now have 5 apples in your basket!"):
            self.play(FadeIn(number_5), run_time=0.5)
        self.wait(2)
