from manim import *
 
class Scene2(Scene):
    def construct(self):
        pw_reqs = Text("Password Facts:").scale(0.8)
        pw_reqs.shift(UP)
        req1 = Tex(r"\text{1. }", r"\text{Exactly }", r"$n$", r"\text{ characters long}").scale(0.8)

        req2 = Tex(r"\text{2. }", r"\text{Every character is either a }", r"$0$", r"\text{ or a }", r"$1$").scale(0.8)
        req2.shift(DOWN)
        # self.add(pw_reqs, req1)
        self.wait(1)
        self.play(FadeIn(pw_reqs))
        self.wait(1)
        self.play(FadeIn(req1))
        self.wait(1)
        self.play(FadeIn(req2))
        self.wait(2)