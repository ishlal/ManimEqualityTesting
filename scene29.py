from manim import *

class Scene29(Scene):
    def construct(self):
        # draw a line down the middle of the screen
        line = Line(start=UP*3, end=DOWN*3)
        self.play(Write(line))
        self.wait(1)
        # text for left side of screen
        text_left = Text("Old Solution").scale(1.5)
        text_left.move_to(LEFT*3.2 + UP*3)
        self.play(Write(text_left))
        # text for right side of screen
        text_right = Text("New Solution").scale(1.5)
        text_right.move_to(RIGHT*3.2 + UP*3)
        self.play(Write(text_right))

        text_expl_left = Text("Idea: Send Everything").scale(0.8)
        text_expl_left.move_to(LEFT*3.2 + UP*1)
        self.play(Write(text_expl_left))
        text_expl_right = Text("Idea: Send prime stuff").scale(0.8)
        text_expl_right.move_to(RIGHT*3.2 + UP*1)
        self.play(Write(text_expl_right))
        self.wait(1)

        text_acc_left = MathTex(r"\text{Accuracy: } 100\%")
        text_acc_left.move_to(LEFT*3.2)
        self.play(Write(text_acc_left))
        text_acc_right = MathTex(r"\text{Accuracy: Hopefully High}")
        text_acc_right.move_to(RIGHT*3.2)
        self.play(Write(text_acc_right))
        self.wait(1)

        text_compl_left = MathTex(r"\text{Communication: full string").scale(0.8)
        text_compl_left.move_to(LEFT*3.2 + DOWN)
        self.play(Write(text_compl_left))
        text_compl_right = MathTex(r"\text{Communication: } p \text{ and } a \bmod p").scale(0.8)
        text_compl_right.move_to(RIGHT*3.2 + DOWN)
        self.play(Write(text_compl_right))
        self.wait(1)

        text_size = MathTex(r"\text{Complexity: } n \text{ bits}").scale(0.8)
        text_size.move_to(LEFT*3.2 + DOWN*2)
        self.play(Write(text_size))
        text_size_right = MathTex(r"\text{Complexity: } << n \text{ bits ideally}").scale(0.8)
        text_size_right.move_to(RIGHT*3.2 + DOWN*2)
        self.play(Write(text_size_right))
        self.wait(2.5)
        self.play(
            FadeOut(text_left),
            FadeOut(text_right),
            FadeOut(text_expl_left),
            FadeOut(text_expl_right),
            FadeOut(text_acc_left),
            FadeOut(text_acc_right),
            FadeOut(text_compl_left),
            FadeOut(text_compl_right),
            FadeOut(text_size),
            FadeOut(text_size_right),
            FadeOut(line)
        )