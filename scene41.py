from manim import *

class Scene41(Scene):
    def construct(self):
        frac = MathTex(r"= \frac{\text{Number of prime divisors of }C}{\text{Number of choices of } p}")
        frac.shift(UP*2)
        self.play(Write(frac))
        self.wait(2)
        frac_2 = MathTex(r"=\frac{\leq n}{\text{Number of choices of } p}")
        frac_2.move_to(frac.get_center())
        self.play(Transform(frac, frac_2))
        self.wait(2)
        # indicate the denominator of frac_2
        text_match = MathTex(r"\text{Number of choices of } p")
        text_match.shift(UP*1.5)
        self.add(text_match)
        self.play(text_match.animate.shift(DOWN*2 + LEFT*2))
        self.wait(1)
        text_3 = MathTex(r"\in [2 \ldots n^3]")
        text_3.next_to(text_match, RIGHT)
        self.play(Write(text_3))
        self.wait(2)


       
        