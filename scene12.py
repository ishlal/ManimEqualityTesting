from manim import *

class Scene12(Scene):
    def construct(self):
        q = Text("Question", font_size=100, color=BLUE)
        self.play(FadeIn(q))
        self.wait(0.5)
        self.play(FadeOut(q))
        ques_p1 = Text("Does there exist a deterministic procedure in which", font_size=36, color=BLUE)
        ques_p2 = Text("which Alice sends less than n characters to Bob?", font_size=36, color=BLUE)
        ques_p1.shift(UP)
        ques_p2.shift(DOWN)
        self.play(Write(ques_p1))
        self.play(Write(ques_p2))
        self.wait(1)
        self.play(FadeOut(ques_p1), FadeOut(ques_p2))
        a = Text("Answer", font_size=100, color=BLUE)
        self.play(FadeIn(a))
        self.wait(0.3)
        self.play(FadeOut(a), run_time=0.3)
        no = Text("No", font_size=100, color=BLUE)
        self.play(FadeIn(no), run_time=0.3)
        self.wait(0.5)
        self.play(FadeOut(no))


