from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class Multiplication(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        
        # Images
        apple = ImageMobject("apple.png").scale(0.5)
        basket = ImageMobject("basket.png").scale(0.5)
        
        # Place three apples in the basket
        apple1 = apple.copy().move_to(basket.get_center() + UP * 0.2)
        apple2 = apple.copy().move_to(basket.get_center() + LEFT * 0.3 + DOWN * 0.2)
        apple3 = apple.copy().move_to(basket.get_center() + RIGHT * 0.3 + DOWN * 0.2)

        # Group the basket and apples
        basket_group = Group(basket, apple1, apple2, apple3)
        
        # 00:00:05,000: Draw a basket.
        with self.voiceover(text="Multiplication is like a shortcut for adding the same number over and over again.") as tracker:
            self.wait(tracker.duration)
        
        with self.voiceover(text="Imagine you have a basket of apples. Let's say there are 3 apples in each basket.") as tracker:
            self.play(FadeIn(basket_group), run_time=tracker.duration)
        
        # 00:00:10,000: Duplicate the basket three times.
        with self.voiceover(text="Now, if you have 4 baskets, how many apples do you have in total?") as tracker:
            self.wait(tracker.duration / 2)
            basket_group_2 = basket_group.copy().shift(RIGHT * 2.5)
            basket_group_3 = basket_group.copy().shift(RIGHT * 5)
            basket_group_4 = basket_group.copy().shift(RIGHT * 7.5)
            self.play(
                FadeIn(basket_group_2),
                FadeIn(basket_group_3),
                FadeIn(basket_group_4),
                run_time=tracker.duration / 2
            )

        # 00:00:15,000: 
        with self.voiceover(text="Instead of adding 3 + 3 + 3 + 3, we can simply multiply!") as tracker:
            self.wait(tracker.duration)

        # 00:00:20,000: 
        with self.voiceover(text="We multiply the number of apples in each basket (3) by the number of baskets (4).") as tracker:
            self.wait(tracker.duration)

        # 00:00:25,000: Highlight all four baskets.
        with self.voiceover(text="So, 3 x 4 = 12. You have 12 apples in total!") as tracker:
            highlight_rect = SurroundingRectangle(
                Group(basket_group, basket_group_2, basket_group_3, basket_group_4),
                color=YELLOW,
                fill_opacity=0.2,
                buff=0.2,
            )
            self.play(Create(highlight_rect), run_time=tracker.duration)

        # Display the equation using Text
        equation_text = Text("3 x 4 = 12", font_size=48).next_to(highlight_rect, DOWN)
        self.play(Write(equation_text))
        self.wait()
