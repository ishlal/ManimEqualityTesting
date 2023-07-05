from manim import *
import random

class Thumbnail(Scene):
    def construct(self):
        # create a VGroup of size 400 which contains MathTex objects which are either the number 0 or 1
        arr_vals = []
        for i in range(400):
            # get random number between 0 and 1
            rand = random.randint(0, 1)
            if rand == 1:
                arr_vals.append(MathTex("1").scale(0.8))
            else:
                arr_vals.append(MathTex("0").scale(0.8))
        string1 = VGroup(*arr_vals)
        string1.arrange_in_grid(20, 20, buff=0.1)
        string1.scale(0.5)
        string1.shift(LEFT*4)

        # draw a rectangle around the string
        rect = Rectangle(width=4, height=5, fill_opacity=0).scale(0.8)
        rect.move_to(string1.get_center())
        self.add(string1, rect)
        string2 = string1.copy()
        string2.shift(RIGHT*8)

        rect2 = rect.copy()
        rect2.move_to(string2.get_center())
        self.add(   string2, rect2)

        arrow1 = Arrow(start=rect.get_edge_center(RIGHT), end=string2.get_edge_center(LEFT)+LEFT, buff=0)
        self.add(arrow1)


        prime_val = MathTex("1001001110", color=GREEN)
        prime_val.next_to(arrow1.get_center(), UP)
        self.add(prime_val)


        rem_val = MathTex("110110", color=GREEN)
        rem_val.next_to(arrow1.get_center(), DOWN)
        self.add(rem_val)

        title_1 = MathTex(r"\text{The Magic Of}", color=BLUE_C).scale(2)
        title_2 = MathTex(r"\text{Sublinear Communication}", color=BLUE_C).scale(2)
        title_1.shift(UP*3)
        title_2.shift(DOWN*3)
        self.add(title_1, title_2)

