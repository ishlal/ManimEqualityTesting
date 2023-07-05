from manim import *

class Scene31(Scene):
    def construct(self):
        title = Text("Case 1", font_size=100, color=PURPLE_B)
        subtitle = Text("Alice and Bob have the same password", font_size=60, color=TEAL_B).next_to(title, DOWN)
        self.play(Write(title), run_time=1.5)
        self.wait(0.5)
        self.play(Write(subtitle), run_time=2)
        self.wait(0.5)
        self.play(FadeOut(title), FadeOut(subtitle))

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

        alice_string = Text("a = 1101001011", color=GREEN)
        alice_string.next_to(group_alice, DOWN)

        bob_string = Text("b = 1101001011", color=GREEN)
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
        self.wait(2)

        int_range = MathTex("[2 \ldots n^3]")
        int_range.next_to(Square1, DOWN, buff=0.5)
        self.play(FadeIn(int_range))
        self.wait(0.5)

        p = MathTex("p")
        p.move_to(int_range.get_center())
        self.add(p)
        self.play(p.animate.move_to(Square1.get_center()))
        self.play(Square1.animate.set_fill(PURPLE, opacity=0.5), FadeOut(int_range))
        self.wait(2)
        # group square and p
        group_square_p = Group(Square1, p)

        p2 = MathTex("p")
        p2.move_to(p.get_center())
        self.add(p2)
        # self.play(p2.animate.move_to(Square2.get_center()))
        alice_string_2 = Text("a = 1101001011", color=GREEN)
        alice_string_2.move_to(alice_string.get_center())
        self.add(alice_string_2)
        alice_string_2_target = Text("a = 1101001011", color=GREEN).scale(0.3)
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
        self.wait(2)

        self.play(group_square_p.animate.move_to(bob_string.get_center() + DOWN*1.2 + LEFT),
                  group_square_a_mod_p.animate.move_to(bob_string.get_center() + DOWN*2.7 + LEFT))
        self.wait(0.8)

        #group together group_square_p and group_square_a_mod_p
        group_square_p_a_mod_p = Group(group_square_p, group_square_a_mod_p)
        square_bob = Square(color=WHITE, fill_opacity=0).scale(0.7)
        square_bob.next_to(group_square_p_a_mod_p, RIGHT, buff=1)
        self.play(FadeIn(square_bob))
        self.wait(1)
        bob_string_2 = Text("b = 1101001011", color=GREEN)
        bob_string_2.move_to(bob_string.get_center())
        self.add(bob_string_2)
        bob_string_2_target = Text("b = 1101001011", color=GREEN).scale(0.3)
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
        # group square and b mod p
        group_square_b_mod_p = Group(square_bob, transform_text_2, group_bob_2)
        self.wait(2)

        # ungroup the groups

        # move group_square_a_mod_p to left side of screen and enlarge it

        target_group_square_a_mod_p = Square(color=ORANGE, fill_opacity=0.5).scale(1.5)
        target_group_square_a_mod_p.shift(LEFT*3 + UP*2)
        target_group_square_b_mod_p = Square(color=ORANGE, fill_opacity=0.5).scale(1.5)
        target_group_square_b_mod_p.shift(RIGHT*3 + UP*2)
        # self.add(target_group_square_a_mod_p, target_group_square_b_mod_p)

        a_mod_p_center = group_square_a_mod_p.get_center()
        b_mod_p_center = group_square_b_mod_p.get_center()

        square_a_mod_p_copy = Square(color=ORANGE, fill_opacity=0.5).scale(0.7)
        square_a_mod_p_copy.move_to(a_mod_p_center)
        square_a_mod_p_copy_text = MathTex(r"a \bmod p").scale(0.6)
        square_a_mod_p_copy_text.move_to(a_mod_p_center)
        # group text and square together
        group_square_a_mod_p_copy = Group(square_a_mod_p_copy, square_a_mod_p_copy_text)
        square_b_mod_p_copy = Square(color=ORANGE, fill_opacity=0.5).scale(0.7)
        square_b_mod_p_copy.move_to(b_mod_p_center)
        square_b_mod_p_copy_text = MathTex(r"b \bmod p").scale(0.6)
        square_b_mod_p_copy_text.move_to(b_mod_p_center)
        # group text and square together
        group_square_b_mod_p_copy = Group(square_b_mod_p_copy, square_b_mod_p_copy_text)
        self.add(group_square_a_mod_p_copy, group_square_b_mod_p_copy)

        self.play(FadeOut(group_square_p_a_mod_p),
                    FadeOut(group_square_b_mod_p),
                  FadeOut(group_square_p),
                  FadeOut(group_alice),
                  FadeOut(group_bob),
                    FadeOut(bob_string),
                    FadeOut(alice_string),
                    FadeOut(p),
                    FadeOut(p2),
                    FadeOut(p3),
                    FadeOut(Square1),
                    group_square_a_mod_p_copy.animate.move_to(target_group_square_a_mod_p.get_center()),
                    group_square_b_mod_p_copy.animate.move_to(target_group_square_b_mod_p.get_center()),
        )
        # scale group_square_a_mod_p_copy and group_square_b_mod_p_copy
        self.play(group_square_a_mod_p_copy.animate.scale(2),
                    group_square_b_mod_p_copy.animate.scale(2))
        
        text_equal = MathTex("=").scale(1.5)
        # move text_equal so it is in between group_square_a_mod_p_copy and group_square_b_mod_p_copy
        text_equal.move_to((group_square_a_mod_p_copy.get_center() + group_square_b_mod_p_copy.get_center())/2)
        self.play(FadeIn(text_equal))
        self.wait(2)

        rect_mod_p = Rectangle(color=GREY, fill_opacity=0.5).scale(1.5)
        rect_mod_p.shift(DOWN*2)
        text_rect_mod_p = MathTex(r"\bmod \;p \text{ operation}")
        # move text to center of rectangle
        text_rect_mod_p.move_to(rect_mod_p.get_center())
        group_rect_mod_p = Group(rect_mod_p, text_rect_mod_p)
        self.play(FadeIn(group_rect_mod_p))

        #text a
        text_a = MathTex("a").scale(1.5)
        text_b = MathTex("b").scale(1.5)
        # self.play(FadeIn(text_a), FadeIn(text_b))
        # self.wait(0.5)

        # move text_a to top left corner of rectangle
        text_a.move_to(rect_mod_p.get_corner(UL) + LEFT*2)
        text_b.move_to(rect_mod_p.get_corner(DL) + LEFT*2)

        text_equal_2 = MathTex("=").scale(1.5)
        # move text_equal_2 in between text_a and text_b
        text_equal_2.move_to((text_a.get_center() + text_b.get_center())/2)
        self.play(FadeIn(text_a), FadeIn(text_b))
        self.play(FadeIn(text_equal_2))

        # draw arrow from text_a to middle of left edge of rectangle
        arrow_a = Arrow(text_a.get_center(), rect_mod_p.get_edge_center(LEFT))
        arrow_b = Arrow(text_b.get_center(), rect_mod_p.get_edge_center(LEFT))
        self.play(FadeIn(arrow_a), FadeIn(arrow_b))
        self.wait(0.5)
        # animate text_a and text_b moving along their respective arrows
        self.play(text_a.animate.move_to(rect_mod_p.get_edge_center(LEFT)),
                    text_b.animate.move_to(rect_mod_p.get_edge_center(LEFT)))
        self.play(FadeOut(text_a), FadeOut(text_b))
        self.wait(0.5)

        text_a_result = MathTex(r"a \bmod p").scale(0.7)
        text_b_result = MathTex(r"b \bmod p").scale(0.7)
        # move text_a_result and text_b_result to right side of rectangle
        
        text_a_result.move_to(rect_mod_p.get_corner(UR) + RIGHT*2)
        text_b_result.move_to(rect_mod_p.get_corner(DR) + RIGHT*2)
        arrow_a_result = Arrow(rect_mod_p.get_edge_center(RIGHT), text_a_result.get_center())
        arrow_b_result = Arrow(rect_mod_p.get_edge_center(RIGHT), text_b_result.get_center())
        text_a_result_copy = text_a_result.copy()
        text_b_result_copy = text_b_result.copy()
        text_a_result_copy.move_to(rect_mod_p.get_edge_center(RIGHT))
        text_b_result_copy.move_to(rect_mod_p.get_edge_center(RIGHT))
        self.play(FadeIn(text_a_result_copy), FadeIn(text_b_result_copy), 
                  FadeIn(arrow_a_result), FadeIn(arrow_b_result))
        self.play(text_a_result_copy.animate.move_to(text_a_result.get_center()),
                    text_b_result_copy.animate.move_to(text_b_result.get_center()))
        self.wait(2)

        text_equals_copy = MathTex("=").scale(1.5)
        text_equals_copy.move_to((text_a_result_copy.get_center() + text_b_result_copy.get_center())/2)
        self.play(FadeIn(text_equals_copy))
        self.wait(1)

        


        
