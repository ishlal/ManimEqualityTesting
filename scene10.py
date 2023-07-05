from manim import *

class Scene10(Scene):
    def construct(self):
        text1 = Text("With this procedure, Alice always sends Bob exactly n characters").scale(0.8)
        text2 = Text("and this procedure is deterministic, as Bob is always able to", color=YELLOW).scale(0.8)
        text3 = Text("correctly conclude if his password and Alice’s password are the same").scale(0.75)
        text4 = Text("or different").scale(0.8);
        text1.shift(UP)
        text3.shift(DOWN)
        text4.shift(DOWN*2)
        self.play(Write(text1), run_time=4)
        self.play(Write(text2), run_time=4)
        self.play(Write(text3), run_time=4.5)
        self.play(Write(text4))
        self.wait(1.5)
        self.play(FadeOut(text1), FadeOut(text2), FadeOut(text3), FadeOut(text4))