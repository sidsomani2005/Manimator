from manim import *
from manim_voiceover import VoiceoverScene
from manim_voiceover.services.gtts import GTTSService

class Multiplication(VoiceoverScene):
    def construct(self):
        self.set_speech_service(GTTSService(lang="en", tld="com"))
        # Set background color to black
        self.camera.background_color = BLACK

        # Load images
        apple_image = ImageMobject("apple.png")
        basket_image = ImageMobject("basket.png")

        # Scale images
        apple_image.scale(0.3)
        basket_image.scale(0.4)

        # Create baskets
        basket1 = basket_image.copy()
        basket2 = basket_image.copy()
        basket3 = basket_image.copy()
        baskets = Group(basket1, basket2, basket3).arrange(RIGHT, buff=1)

        # Position baskets
        baskets.shift(DOWN)

        #Voiceover for intro and the question
        self.play(Write(Tex("Let's learn about multiplication!").set_color(WHITE).scale(0.8)))
        self.wait(1)
        self.play(FadeOut(Tex("Let's learn about multiplication!").set_color(WHITE).scale(0.8)))
        self.wait(1)
        with self.voiceover(text="Imagine you have a basket of apples.") as tracker:
            self.play(FadeIn(basket1), run_time=tracker.duration)

        with self.voiceover(text="Let's say you have 3 baskets, and each basket has 4 apples.") as tracker:
            self.play(
                FadeIn(basket2),
                FadeIn(basket3),
                run_time=tracker.duration
            )
            self.wait(tracker.duration)

        # Add apples to each basket
        apples_group = Group()  # Create a group to hold all the apples
        for basket in baskets:
            apples = Group(*[apple_image.copy() for _ in range(4)]).arrange_in_grid(n_cols=2, buff=0.2)
            apples.move_to(basket.get_center() + UP * 0.5)
            apples_group.add(apples)
            self.play(FadeIn(apples), run_time=0.5)

        self.wait(1.5)

        with self.voiceover(text="Multiplication helps us find the total number of apples quickly.") as tracker:
            self.play(
                FadeToColor(baskets, BLUE), 
                run_time=tracker.duration/2
            )
            self.play(
                FadeToColor(baskets, WHITE), 
                run_time=tracker.duration/2
            ) 

        with self.voiceover(text="Instead of counting each apple one by one, we can multiply!") as tracker:
            self.play(
                FadeToColor(apples_group, YELLOW), 
                run_time=tracker.duration/2
            )
            self.play(
                FadeToColor(apples_group, WHITE), 
                run_time=tracker.duration/2
            ) 

        # Multiplication step
        equation = MathTex("3", "\\times", "4", "=", "12").set_color(WHITE).scale(0.8)
        equation.to_edge(UP)

        with self.voiceover(text="We multiply the number of baskets (3) by the number of apples in each basket (4).") as tracker:
            self.play(Write(equation[0:3]), run_time=tracker.duration)

        self.wait(0.5)

        with self.voiceover(text="3 times 4 equals 12. So, we have a total of 12 apples!") as tracker:
            self.play(Write(equation[3:]), run_time=tracker.duration)
            self.play(
                FadeToColor(apples_group, GREEN),  # Highlight all apples in green
                run_time=tracker.duration
            )
            self.play(
                FadeToColor(apples_group, WHITE), 
                run_time=tracker.duration
            )

        self.wait(2)