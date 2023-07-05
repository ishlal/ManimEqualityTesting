from manim import *


class Scene14(Scene):
    def construct(self):
        # Create the table


        table = VGroup(
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("Number of characters sent", font_size=26, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                VGroup(Text("Probability of Bob knowing", font_size=20 , color=BLUE),
                       Text("Alice's password", font_size=20, color=BLUE)).arrange(DOWN))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("n", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("1", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("n-1", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("1/2", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("n-2", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("1/4", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("n-k", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex("1/2^k", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0)
        ).arrange(DOWN, buff=0)
        table.shift(UP)
        # Animate each row one at a time
        self.play(Write(table), run_time=4)
        self.wait(2)
        self.play(Indicate(table[1][0][1]), 
                  Indicate(table[1][1][1]), run_time=2)
        self.play(Indicate(table[1][0][1]), 
                  Indicate(table[1][1][1]), run_time=2)