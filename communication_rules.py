from manim import *
 
class Communication(Scene):
    def construct(self):
        pw_reqs = Tex(r"\underline{\text{Communication Rules:}}").scale(1.2)
        pw_reqs.shift(UP*2)
        req1 = Tex(r"\text{1. }", r"\text{Alice and Bob communicate by text}").scale(0.8)
        req2 = Tex(r"\text{2. }", r"\text{All text messages must be sent in binary}").scale(0.8)
        req3 = Tex(r"\text{3. }", r"\text{They are charged 1 dollar for each bit communicated}").scale(0.8)

        req1.shift(UP)
        req3.shift(DOWN)
        # self.add(pw_reqs, req1)
        self.wait(0.2)
        self.play(FadeIn(pw_reqs))
        self.wait(0.2)
        self.play(FadeIn(req1))
        self.wait(1)
        self.play(FadeIn(req2))
        self.wait(1.5)
        self.play(FadeIn(req3))
        self.wait(3.5)

        question = Tex(r"\text{How can Alice communicate to Bob in such a way that Bob is }").scale(0.8).set_color(YELLOW)
        question2 = Tex(r"\text{able to determine if their passwords are the same,}").scale(0.8).set_color(YELLOW)
        question3 = Tex(r"\text{all while ensuring a low enough charge?}").scale(0.8).set_color(YELLOW)
        question.shift(DOWN*2)
        question2.next_to(question, DOWN)
        question3.next_to(question2, DOWN)
        self.play(Write(question), run_time=2.8)
        self.play(Write(question2), run_time=2.8)
        self.play(Write(question3), run_time=2.8)
        self.wait(2) 