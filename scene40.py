from manim import *

class Scene40(Scene):
    def construct(self):

        text_top = MathTex(r"\text{Q: How many prime divisors does } C \text{ have?}").scale(0.8)
        text_top.shift(UP*3)
        self.play(Write(text_top))
        self.wait(2)

        text_answer = MathTex(r"\text{A: } C \text{ has } \leq \log_2 C \text{ prime divisors.}").scale(0.8)
        text_answer.next_to(text_top, DOWN)
        self.play(Write(text_answer))
        self.wait(1)

        guy_robin_img = ImageMobject("pics/guy_robin.jpg").scale(3.5)
        guy_robin_img.scale(0.5)
        guy_robin_img.shift(LEFT*4 + DOWN)
        guy_robin_caption = MathTex(r"\text{Guy Robin, 1983}").scale(0.8)
        guy_robin_caption.next_to(guy_robin_img, DOWN)
        self.play(FadeIn(guy_robin_img), Write(guy_robin_caption))
        self.wait(2)

        guy_robin_conclusion = MathTex(r"\text{The number of prime factors of } N \in \mathbb{Z^+} \\ \
                                        \text{ is } \mathcal{O}\left(\frac{\log N}{\log \log N}\right)").scale(0.8)

        guy_robin_conclusion.shift(DOWN + RIGHT)
        self.play(Write(guy_robin_conclusion))
        self.wait(2)
        self.play(
            FadeOut(text_answer),
            FadeOut(guy_robin_img),
            FadeOut(guy_robin_caption),
            FadeOut(guy_robin_conclusion)
        )

        alice = ImageMobject("pics/alice.png").scale(0.2)
        bob = ImageMobject("pics/bob.png").scale(0.5)
        text_alice = Text("Alice").scale(0.5)
        text_bob = Text("Bob").scale(0.5)
        text_alice.next_to(alice, DOWN)
        text_bob.next_to(bob, DOWN)
        group_alice = Group(alice, text_alice)
        group_bob = Group(bob, text_bob)
        group_alice.shift(LEFT*4 + UP)
        group_bob.shift(RIGHT*4 + UP)

        # self.play(FadeIn(group_alice))
        # self.play(FadeIn(group_bob))

        self.play(FadeIn(group_alice), FadeIn(group_bob))

        alice_string = MathTex(r"1101001011_{\text{base } 2}")
        alice_string.next_to(group_alice, DOWN)
        self.play(FadeIn(alice_string))

        bob_string = MathTex(r"1100001011_{\text{base } 2}")
        bob_string.next_to(group_bob, DOWN)
        self.play(FadeIn(bob_string))
        self.wait(1)

        alice_string_undrbr = MathTex(r"\underbrace{1101001011_{\text{base } 2}}_{\text{length } n}")
        alice_string_undrbr.next_to(group_alice, DOWN)
        # replace alice_string with alice_string_undrbr
        self.remove(alice_string)
        self.add(alice_string_undrbr)

        bob_string_ub = MathTex(r"\underbrace{1100001011_{\text{base } 2}}_{\text{length } n}")
        bob_string_ub.next_to(group_bob, DOWN)
        # replace alice_string with alice_string_undrbr
        self.remove(bob_string)
        self.add(bob_string_ub)
        self.wait(2)

        alice_string_base_10 = MathTex(r"< 2^n}")
        alice_string_base_10.next_to(alice_string_undrbr, DOWN)

        self.play(FadeIn(alice_string_base_10))
        self.wait(0.5)

        bob_string_base_10 = MathTex(r"<2^n")
        bob_string_base_10.next_to(bob_string_ub, DOWN)

        self.play(FadeIn(bob_string_base_10))
        self.wait(0.5)

        eq = MathTex(r" \
                     C &= |A - B| \\ \
                        &< 2^n")
        

        self.play(Write(eq))
        self.wait(1)

        conc = MathTex(r" \
                       \text{Therefore, C has } \\ \
                       \leq \log_2 C < \log_2 2^n = n \\ \
                       \text{ prime divisors.}").scale(0.8)
        
        conc.shift(DOWN*2.5)
        self.play(Write(conc))
        self.wait(2)

        self.play(
            FadeOut(alice_string_undrbr),
            FadeOut(bob_string_ub),
            FadeOut(alice_string_base_10),
            FadeOut(bob_string_base_10),
            FadeOut(eq),
            FadeOut(conc),
            FadeOut(group_alice),
            FadeOut(group_bob)
        )

        answer_2 = MathTex(r"\text{A: } C \text{ has } \leq n \text{ prime divisors.}").scale(0.8)
        answer_2.next_to(text_top, DOWN)
        self.play(Write(answer_2))
        self.wait(2)
        