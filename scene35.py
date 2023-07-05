from manim import *

class Scene35(Scene):
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

        alice_string = Text("a = 1101001011", color=RED)
        alice_string.next_to(group_alice, DOWN)

        bob_string = Text("b = 1100001010", color=RED)
        bob_string.next_to(group_bob, DOWN)
        self.play(FadeIn(alice_string), FadeIn(bob_string))
        self.wait(0.5)

        Square1 = Square(color=WHITE, fill_opacity=0).scale(0.7)
        Square2 = Square(color=WHITE, fill_opacity=0).scale(0.7)
        # put Square 1 and Square2 next to each other with some buffer room
        Square1.next_to(alice_string, DOWN, buff=0.5)
        Square1.shift(LEFT)
        Square2.next_to(Square1, RIGHT, buff=0.5)
        self.play(FadeIn(Square1), FadeIn(Square2))
        self.wait(0.5)

        int_range = MathTex("[2 \ldots n^3]")
        int_range.next_to(Square1, DOWN, buff=0.5)
        self.play(FadeIn(int_range))
        self.wait(0.5)

        p = MathTex("p")
        p.move_to(int_range.get_center())
        self.add(p)
        self.play(p.animate.move_to(Square1.get_center()))
        self.play(Square1.animate.set_fill(PURPLE, opacity=0.5), FadeOut(int_range))
        self.wait(0.5)
        # group square and p
        group_square_p = Group(Square1, p)

        p2 = MathTex("p")
        p2.move_to(p.get_center())
        self.add(p2)
        # self.play(p2.animate.move_to(Square2.get_center()))
        alice_string_2 = Text("a = 1101001011", color=RED)
        alice_string_2.move_to(alice_string.get_center())
        self.add(alice_string_2)
        alice_string_2_target = Text("a = 1101001011", color=RED).scale(0.3)
        alice_string_2_target.move_to(Square2.get_center())
        self.play(p2.animate.move_to(Square2.get_center()), Transform(alice_string_2, alice_string_2_target))
        self.wait(0.3)
        group_alice_2 = Group(alice_string_2, p2)
        transform_text = MathTex(r"a \bmod p").scale(0.6)
        transform_text.move_to(Square2.get_center())
        self.play(Transform(group_alice_2, transform_text))
        self.wait(0.3)
        self.play(Square2.animate.set_fill(ORANGE, opacity=0.5))
        # group square and a mod p
        group_square_a_mod_p = Group(Square2, transform_text, group_alice_2)
        self.wait(0.5)

        self.play(group_square_p.animate.move_to(bob_string.get_center() + DOWN*1.2 + LEFT),
                  group_square_a_mod_p.animate.move_to(bob_string.get_center() + DOWN*2.7 + LEFT))
        self.wait(0.5)

        #group together group_square_p and group_square_a_mod_p
        group_square_p_a_mod_p = Group(group_square_p, group_square_a_mod_p)
        square_bob = Square(color=WHITE, fill_opacity=0).scale(0.7)
        square_bob.next_to(group_square_p_a_mod_p, RIGHT, buff=1)
        self.play(FadeIn(square_bob))
        self.wait(0.5)
        bob_string_2 = Text("b = 1100001010", color=GREEN)
        bob_string_2.move_to(bob_string.get_center())
        self.add(bob_string_2)
        bob_string_2_target = Text("b = 1100001010", color=GREEN).scale(0.3)
        bob_string_2_target.move_to(square_bob.get_center())
        p3 = MathTex("p")
        p3.move_to(Square1.get_center())
        self.play(Transform(bob_string_2, bob_string_2_target), p3.animate.move_to(square_bob.get_center()))
        self.wait(0.3)
        group_bob_2 = Group(bob_string_2, p3)
        transform_text_2 = MathTex(r"b \bmod p").scale(0.6)
        transform_text_2.move_to(square_bob.get_center())
        self.play(Transform(group_bob_2, transform_text_2))
        self.wait(0.3)
        self.play(square_bob.animate.set_fill(ORANGE, opacity=0.5))
        self.wait(0.5)


        image_equal = ImageMobject("pics/equal.png").scale(1)
        image_equal.move_to(group_bob.get_center() + LEFT*3 + UP*0.5)
        self.play(FadeIn(image_equal))
        self.wait(4)