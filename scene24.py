from manim import *

class Scene24(Scene):
    def construct(self):
        text1 = Text("Procedure", font_size=60, color=TEAL_B).to_edge(UP)
        text2 = MathTex(r"\text{1. Alice has her password } a")
        text3 = MathTex(r"\text{2. Alice develops fingerprinting algorithm } h")
        text4 = MathTex(r"\text{3. Alice computes } h(a)")
        text5 = MathTex(r"\text{4. Alice sends } h \text{ and } h(a) \text{ to Bob}")
        text6 = MathTex(r"\text{5. Bob computes } h(b) \text{ using } h \text{ that he received from Alice}")
        text7 = MathTex(r"\text{6. If } h(a) = h(b) \text{, Bob concludes equality with } 100\% \text{ accuracy}")
        text8 = MathTex(r"\text{7. If } h(a) \neq h(b) \text{, Bob concludes inequality with high accuracy}")

        text2.next_to(text1, DOWN)
        text3.next_to(text2, DOWN)
        text4.next_to(text3, DOWN)
        text5.next_to(text4, DOWN)
        text6.next_to(text5, DOWN)
        text7.next_to(text6, DOWN)
        text8.next_to(text7, DOWN)

        self.play(Write(text1), run_time=2)
        self.wait(0.5)
        self.play(Write(text2), run_time=2)
        self.wait(0.5)
        self.play(Write(text3), run_time=3)
        self.wait(0.5)
        self.play(Write(text4), run_time=2)
        self.wait(0.5)
        self.play(Write(text5), run_time=2)
        self.wait(5.5)
        self.play(Write(text6), run_time=3)
        self.wait(2)
        self.play(Write(text7), run_time=4)
        self.wait(3)
        self.play(Write(text8), run_time=4)
        self.wait(5)

