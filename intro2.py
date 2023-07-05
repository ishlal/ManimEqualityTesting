from manim import *
from colour import Color

class Intro2(Scene):
    def construct(self):
        text = MathTex(r"\text{Coming Up}").scale(2)
        text.shift(UP*3)
        self.play(Write(text))
        self.wait(2)

        rectangle = Rectangle(width=13, height=5.8, fill_opacity=0)
        rectangle.shift(DOWN)
        self.play(Write(rectangle))

        suspect = Square(color = Color(hue=18/25, saturation=1, luminance=0.5),
                         fill_opacity=0.5).scale(0.65)
        text_sus = Text("Suspect").scale(0.5)
        text_sus.move_to(suspect)
        group_sus = VGroup(suspect, text_sus)
        group_sus.shift(LEFT*5 + DOWN)
        text_height = Text("Height: 180cm").scale(0.5)
        text_height.next_to(group_sus, DOWN)
        text_weight = Text("Weight: 100kg").scale(0.5)
        text_weight.next_to(text_height, DOWN)
        self.play(Write(group_sus), Write(text_height), Write(text_weight))

        hues = [22, 12, 9, 4, 23, 6, 2, 17, 15, 8, 11, 13, 1, 20, 5, 16, 3, 19, 25, 10, 21, 14, 7, 18, 24]

        square_array = [VGroup(Square(color=Color(hue = hues[j]/25, saturation=1, luminance=0.5),
                     fill_opacity=0.5).scale(0.35),
                     Text("Person " + str(j+1)).scale(0.3)) for j in range(25)]

        squares = VGroup(
            *square_array
        ).arrange_in_grid(5, 5, buff=0.3)
        squares.shift(RIGHT*2 + DOWN)
        self.play(Write(squares), run_time=1)   
        self.wait(1)
        crosses = []
        for i in range(25):
            if i != 23:
                cross = Cross(stroke_width=8).scale(0.4)
                crosses.append(cross)
                cross.move_to(squares[i][0])
                self.play(Write(cross), run_time=0.1)
        self.wait(1)
        # fade out everything in crosses
        for i in range(len(crosses)):
            self.play(FadeOut(crosses[i]), run_time=0.03)
        self.play(FadeOut(squares), FadeOut(group_sus), FadeOut(text_height), FadeOut(text_weight), run_time=0.5)
        self.wait(1)


        alice = ImageMobject("pics/alice.png").scale(0.1)
        bob = ImageMobject("pics/bob.png").scale(0.3)
        text_alice = Text("Alice").scale(0.5)
        text_bob = Text("Bob").scale(0.5)
        text_alice.next_to(alice, DOWN)
        text_bob.next_to(bob, DOWN)
        group_alice = Group(alice, text_alice)
        group_bob = Group(bob, text_bob)
        group_alice.shift(LEFT*4+UP*0.5)
        group_bob.shift(RIGHT*4+UP*0.5)

        # self.play(FadeIn(group_alice))
        # self.play(FadeIn(group_bob))

        self.play(FadeIn(group_alice), FadeIn(group_bob))

        alice_string = Text("a = 1101001011", color=RED).scale(0.5)
        alice_string.next_to(group_alice, DOWN)

        bob_string = Text("b = 1100001010", color=RED).scale(0.5)
        bob_string.next_to(group_bob, DOWN)
        self.play(FadeIn(alice_string), FadeIn(bob_string))
        self.wait(0.5)

        Square1 = Square(color=WHITE, fill_opacity=0).scale(0.4)
        Square2 = Square(color=WHITE, fill_opacity=0).scale(0.4)
        # put Square 1 and Square2 next to each other with some buffer room
        Square1.next_to(alice_string, DOWN, buff=0.5)
        Square1.shift(LEFT)
        Square2.next_to(Square1, RIGHT, buff=0.5)
        self.play(FadeIn(Square1), FadeIn(Square2))
        self.wait(2)

        int_range = MathTex("[2 \ldots n^3]").scale(0.5)
        int_range.next_to(Square1, DOWN, buff=0.5)
        self.play(FadeIn(int_range))
        self.wait(0.5)

        p = MathTex("p").scale(0.5)
        p.move_to(int_range.get_center())
        self.add(p)
        self.play(p.animate.move_to(Square1.get_center()))
        self.play(Square1.animate.set_fill(PURPLE, opacity=0.5), FadeOut(int_range))
        self.wait(2)
        # group square and p
        group_square_p = Group(Square1, p)

        p2 = MathTex("p").scale(0.5)
        p2.move_to(p.get_center())
        self.add(p2)
        # self.play(p2.animate.move_to(Square2.get_center()))
        alice_string_2 = Text("a = 1101001011", color=RED).scale(0.5)
        alice_string_2.move_to(alice_string.get_center())
        self.add(alice_string_2)
        alice_string_2_target = Text("a = 1101001011", color=RED).scale(0.3)
        alice_string_2_target.move_to(Square2.get_center())
        self.play(p2.animate.move_to(Square2.get_center()), Transform(alice_string_2, alice_string_2_target))
        self.wait(0.3)
        group_alice_2 = Group(alice_string_2, p2)
        transform_text = MathTex(r"a \bmod p").scale(0.4)
        transform_text.move_to(Square2.get_center())
        self.play(Transform(group_alice_2, transform_text))
        self.wait(0.3)
        self.play(Square2.animate.set_fill(ORANGE, opacity=0.5))
        # group square and a mod p
        group_square_a_mod_p = Group(Square2, transform_text, group_alice_2)
        self.wait(2)

        self.play(group_square_p.animate.move_to(bob_string.get_center() + DOWN*0.8 + LEFT),
                  group_square_a_mod_p.animate.move_to(bob_string.get_center() + DOWN*1.8 + LEFT))
        self.wait(0.8)

        #group together group_square_p and group_square_a_mod_p
        group_square_p_a_mod_p = Group(group_square_p, group_square_a_mod_p)
        square_bob = Square(color=WHITE, fill_opacity=0).scale(0.4)
        square_bob.next_to(group_square_p_a_mod_p, RIGHT, buff=1)
        self.play(FadeIn(square_bob))
        self.wait(1)
        bob_string_2 = Text("b = 1100001010", color=GREEN).scale(0.5)
        bob_string_2.move_to(bob_string.get_center())
        self.add(bob_string_2)
        bob_string_2_target = Text("b = 1100001010", color=GREEN).scale(0.3)
        bob_string_2_target.move_to(square_bob.get_center())
        p3 = MathTex("p")
        p3.move_to(Square1.get_center())
        self.play(Transform(bob_string_2, bob_string_2_target), p3.animate.move_to(square_bob.get_center()))
        self.wait(0.3)
        group_bob_2 = Group(bob_string_2, p3)
        transform_text_2 = MathTex(r"b \bmod p").scale(0.4)
        transform_text_2.move_to(square_bob.get_center())
        self.play(Transform(group_bob_2, transform_text_2))
        self.wait(0.3)
        self.play(square_bob.animate.set_fill(TEAL_E, opacity=0.5))
        # group square and b mod p
        group_square_b_mod_p = Group(square_bob, transform_text_2, group_bob_2)
        

        #FadeOut everything
        self.play(FadeOut(group_square_p_a_mod_p), FadeOut(group_square_b_mod_p), FadeOut(group_alice), FadeOut(group_bob), FadeOut(alice_string), FadeOut(bob_string),
                  FadeOut(rectangle), FadeOut(text))

        self.wait(2)