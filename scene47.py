from manim import *

class Scene47(Scene):
    def construct(self):
        table = VGroup(
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"n \text{ (number of characters)}", font_size=32, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\text{Old Cost }(n)", font_size=36 , color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\text{New Cost }(\leq 6\log_2 n)", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("100", font_size=42, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\$ 100", font_size=42 , color=RED)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\leq \$ 40", font_size=42 , color=GREEN))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("1000", font_size=42, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\$ 1000", font_size=42 , color=RED)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\leq \$ 60", font_size=42 , color=GREEN))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("10000", font_size=42, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\$ 10000", font_size=42 , color=RED)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\leq \$ 78", font_size=42 , color=GREEN))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("10^{10}", font_size=42, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\$ 10^{10}", font_size=42 , color=RED)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\leq \$ 198", font_size=42 , color=GREEN))
            ).arrange(RIGHT, buff=0), 
        ).arrange(DOWN, buff=0)

        for row in table:
            self.play(Write(row), run_time=2)
            self.wait(0.5)
        self.wait(2)