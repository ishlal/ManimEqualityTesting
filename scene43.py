from manim import *

class Scene43(Scene):
    def construct(self):

        frac = MathTex(r"\Pr[\text{error}]= \frac{\text{Number of prime divisors of }C}{\text{Number of choices of } p}")
        frac.shift(UP*3)
        self.play(Write(frac))
        self.wait(1)

        fact_1 = MathTex(r"\text{Fact 1: Number of prime divisors of }C \leq n", color=YELLOW)
        fact_1.shift(UP*1.5)
        self.play(Write(fact_1))
        self.wait(1)
        fact_2 = MathTex(r"\text{Fact 2: Number of choices of } p \approx \frac{n^3}{3 \log n}", color=GREEN)

        fact_2.next_to(fact_1, DOWN)
        self.play(Write(fact_2))
        self.wait(2)

        frac_new = MathTex(r"\Pr[\text{error}] \leq \frac{n}{\frac{n^3}{3 \log n}} = \frac{3 \log n}{n^2} \leq \frac{1}{n}")
        frac_new.shift(DOWN*1.5)
        self.play(Write(frac_new))
        self.wait(2)
