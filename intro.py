from manim import *
import random

class Intro(Scene):
    def construct(self):
        # create a VGroup of size 400 which contains MathTex objects which are either the number 0 or 1
        arr_vals = []
        for i in range(400):
            # get random number between 0 and 1
            rand = random.randint(0, 1)
            if rand == 1:
                arr_vals.append(MathTex("1"))
            else:
                arr_vals.append(MathTex("0"))
        string1 = VGroup(*arr_vals)
        string1.arrange_in_grid(20, 20, buff=0.1)
        string1.scale(0.5)
        string1.shift(LEFT*4)

        # draw a rectangle around the string
        rect = Rectangle(width=4, height=5, fill_opacity=0)
        rect.move_to(string1.get_center())
        self.play(Write(string1), Write(rect))
        string2 = string1.copy()
        string2.shift(RIGHT*8)

        rect2 = rect.copy()
        rect2.move_to(string2.get_center())
        self.play(Write(string2), Write(rect2))
        self.wait(0.5)

        arrow1 = Arrow(start=rect.get_edge_center(RIGHT), end=string2.get_edge_center(LEFT)+LEFT, buff=0)
        self.play(Write(arrow1))

        prime_val = MathTex("1001001110", color=GREEN)
        prime_val.next_to(arrow1.get_center(), UP)
        self.play(Write(prime_val))

        rem_val = MathTex("110110", color=GREEN)
        rem_val.next_to(arrow1.get_center(), DOWN)
        self.play(Write(rem_val))
        self.wait(2)

        dumb = ImageMobject("pics/dumbledore.webp").scale(0.5)
        dumb.move_to(LEFT*9)
        self.play(dumb.animate.shift(RIGHT*18), run_time=3.5)
        self.wait(2)