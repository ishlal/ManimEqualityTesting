from manim import *


class Scene11(Scene):
    def construct(self):
        # Create the table


        table = VGroup(
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("n (number of characters)", font_size=26, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("Cost", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("100", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("$100", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("1000", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("$1000", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("10000", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("$10000", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("1000000000", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("$1000000000", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0)
        ).arrange(DOWN, buff=0)
        table.shift(UP)
        # Animate each row one at a time
        for row in table:
            self.play(Write(row), run_time=2)
            self.wait(0.5)
        self.wait(3)
        comm = Text("Communication Complexity: ")
        # create LaTeX formula O(n) in yellow text
        formula = MathTex("O(n)", color=YELLOW)
        # arrange formula to the right of comm
        formula.next_to(comm, RIGHT)
        comm_formula = VGroup(comm, formula)
        # place comm_formula below table
        comm_formula.next_to(table, DOWN*1.5)
        self.play(Write(comm_formula))
        self.wait(3)