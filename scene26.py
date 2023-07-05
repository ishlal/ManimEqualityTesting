from manim import *


class Scene26(Scene):
    def construct(self):

        alice = ImageMobject("pics/alice.png").scale(0.2)
        bob = ImageMobject("pics/bob.png").scale(0.5)
        text_alice = Text("Alice").scale(0.5)
        text_bob = Text("Bob").scale(0.5)
        text_alice.next_to(alice, DOWN)
        text_bob.next_to(bob, DOWN)
        group_alice = Group(alice, text_alice)
        group_bob = Group(bob, text_bob)
        group_alice.shift(LEFT*4 + UP*2)
        group_bob.shift(RIGHT*4 + UP*2)

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

        alice_string_base_10 = MathTex(r"=843_{\text{base } 10}")
        alice_string_base_10.next_to(alice_string_undrbr, DOWN)

        self.play(FadeIn(alice_string_base_10))
        self.wait(0.5)

        bob_string_base_10 = MathTex(r"=779_{\text{base } 10}")
        bob_string_base_10.next_to(bob_string_ub, DOWN)

        self.play(FadeIn(bob_string_base_10))
        self.wait(0.5)

        string_bound = MathTex(r"< 2^{10} = 2^{n}")
        string_bound.next_to(alice_string_base_10, DOWN)
        string_bound2 = MathTex(r"< 2^{10} = 2^{n}")
        string_bound2.next_to(bob_string_base_10, DOWN)
        self.play(FadeIn(string_bound), FadeIn(string_bound2))
        self.wait(2)

        
