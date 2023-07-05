from manim import *

class Scene32(Scene):
    def construct(self):
        text_1 = Text("In this case,").scale(0.8)
        text_2 = Text("where Alice and Bob have the same password,").scale(0.8)
        text_3 = Text("since a mod p ALWAYS matches b mod p").scale(0.8)
        text_4 = Text("Bob will ALWAYS conclude that their passwords indeed match").scale(0.8)
        text_5 = Text("and will ALWAYS be correct").scale(0.8)

        text_1.shift(UP*2)
        text_2.shift(UP)
        text_4.shift(DOWN)
        text_5.shift(DOWN*2)
        self.play(Write(text_1))
        self.play(Write(text_2))
        self.play(Write(text_3))
        self.wait(1)
        self.play(Write(text_4))
        self.wait(0.5)
        self.play(Write(text_5))
        self.wait(2)
        self.play(FadeOut(text_1), FadeOut(text_2), FadeOut(text_3), FadeOut(text_4), FadeOut(text_5))
        self.wait(2)
