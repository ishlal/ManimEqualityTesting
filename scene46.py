from manim import *

class Scene46(Scene):
    def construct(self):
        text_question = Text("Question", color=GOLD, font_size=100)
        self.play(Write(text_question))
        self.wait(1)
        self.play(FadeOut(text_question))

        text_q1 = Text("How many bits are communicated?").scale(0.8)
        text_q1.move_to(UP*3)
        self.play(Write(text_q1))

        alice = ImageMobject("pics/alice.png").scale(0.2)
        bob = ImageMobject("pics/bob.png").scale(0.5)
        text_alice = Text("Alice").scale(0.5)
        text_bob = Text("Bob").scale(0.5)
        text_alice.next_to(alice, DOWN)
        text_bob.next_to(bob, DOWN)
        group_alice = Group(alice, text_alice)
        group_bob = Group(bob, text_bob)
        group_alice.shift(LEFT*4 + UP*1.5)
        group_bob.shift(RIGHT*4 + UP*1.5)

        # self.play(FadeIn(group_alice))
        # self.play(FadeIn(group_bob))

        self.play(FadeIn(group_alice), FadeIn(group_bob))

        alice_string = Text("a = 1101001011", color=GREEN)
        alice_string.next_to(group_alice, DOWN)

        bob_string = Text("b = 1101001011", color=GREEN)
        bob_string.next_to(group_bob, DOWN)
        self.play(FadeIn(alice_string), FadeIn(bob_string))


        Square1 = Square(color=WHITE, fill_opacity=0).scale(0.6)
        Square2 = Square(color=WHITE, fill_opacity=0).scale(0.6)
        # put Square 1 and Square2 next to each other with some buffer room
        Square1.next_to(alice_string, DOWN, buff=0.5)
        Square1.shift(LEFT)
        Square2.next_to(Square1, RIGHT, buff=0.5)


        p = MathTex("p")
        p.move_to(Square1.get_center())


        # group square and p
        group_square_p = Group(Square1, p)
        transform_text = MathTex(r"a \bmod p").scale(0.6)
        transform_text.move_to(Square2.get_center())
        self.play(
            FadeIn(Square1),
            FadeIn(p),
            Square1.animate.set_fill(PURPLE, opacity=0.5),
            FadeIn(transform_text),
            Square2.animate.set_fill(ORANGE, opacity=0.5)
        )
        # group square and a mod p
        group_square_a_mod_p = Group(Square2, transform_text)
        self.wait(2)

        self.play(group_square_p.animate.move_to(bob_string.get_center() + DOWN*1.2 + LEFT),
                  group_square_a_mod_p.animate.move_to(bob_string.get_center() + DOWN*2.7 + LEFT))
        self.wait(2)

        self.play(
            FadeOut(group_alice),
            FadeOut(group_bob),
            FadeOut(alice_string),
            FadeOut(bob_string),
            FadeOut(text_q1),
        )
        self.wait(0.5)
        self.play(
            group_square_p.animate.move_to(UP*1.2 + LEFT*4),
            group_square_a_mod_p.animate.move_to(DOWN*1.2 + LEFT*4)
        )
        self.play(
            group_square_p.animate.scale(1.5),
            group_square_a_mod_p.animate.scale(1.5)
        )
        self.wait(2)

        text_1 = MathTex(r"\in [2\ldots n^3]")
        text_1.next_to(group_square_p, RIGHT)
        self.play(Write(text_1))
        self.wait(1)
        text_2 = MathTex(r"\implies  p \leq n^3")
        text_2.next_to(text_1, RIGHT)
        self.play(Write(text_2))
        self.wait(1)
        self.play(FadeOut(text_1))
        self.play(text_2.animate.next_to(group_square_p, RIGHT))
        text_3 = MathTex(r"\implies  n^3 \text{ has } \log_2(n^3) = 3\log_2 n\text{ bits}").scale(0.9)
        text_3.next_to(text_2, RIGHT)
        self.play(Write(text_3))
        self.wait(1)
        self.play(FadeOut(text_2))
        self.play(text_3.animate.next_to(group_square_p, RIGHT))
        text_4 = MathTex(r"\implies  p \text{ has } \leq 3\log_2 n \text{ bits}", color=YELLOW).scale(0.9)
        text_4.next_to(text_3, DOWN)
        self.play(Write(text_4))
        self.wait(2)

        text_1_amp = MathTex(r" \leq p")
        text_1_amp.next_to(group_square_a_mod_p, RIGHT)
        self.play(Write(text_1_amp))
        self.wait(1)
        text_2_amp = MathTex(r"\leq n^3")
        text_2_amp.next_to(text_1_amp, RIGHT)
        self.play(Write(text_2_amp))
        self.wait(1)
        self.play(FadeOut(text_1_amp))
        self.play(text_2_amp.animate.next_to(group_square_a_mod_p, RIGHT))
        text_3_amp = MathTex(r"\implies  a \bmod p \text{ has } \leq 3\log_2 n \text{ bits}", color=YELLOW).scale(0.9)
        text_3_amp.next_to(text_2_amp, RIGHT)
        self.play(Write(text_3_amp))
        self.wait(2)

        text_conc = MathTex(r"\text{Alice and Bob communicate } \leq 3 \log_2 n + 3 \log_2 n = 6 \log_2 n \text{ bits}", color=GREEN)
        text_conc.move_to(DOWN*3)
        self.play(Write(text_conc))
        self.wait(2)
