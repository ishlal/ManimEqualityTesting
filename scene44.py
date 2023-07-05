from manim import *

class Scene44(Scene):
    def construct(self):
        # draw a line down the middle of the screen
        line = Line(start=UP*3, end=DOWN*3)
        # self.play(Write(line))

        
        text_left = Text("Case 1").scale(1.5)
        text_left.move_to(LEFT*3.2 + UP*3)
        # self.play(Write(text_left))
        # text for right side of screen
        text_right = Text("Case 2").scale(1.5)
        text_right.move_to(RIGHT*3.2 + UP*3)
        # self.play(Write(text_right))


        alice = ImageMobject("pics/alice.png").scale(0.15)
        bob = ImageMobject("pics/bob.png").scale(0.4)
        text_alice = Text("Alice").scale(0.5)
        text_bob = Text("Bob").scale(0.5)
        text_alice.next_to(alice, DOWN)
        text_bob.next_to(bob, DOWN)
        group_alice = Group(alice, text_alice)
        group_bob = Group(bob, text_bob)
        group_alice.shift(LEFT*5)
        group_bob.shift(LEFT*2)
        # self.play(FadeIn(group_alice), FadeIn(group_bob))



        alice_string = MathTex("1101001011", color=GREEN)
        alice_string.next_to(group_alice, DOWN)
        bob_string = MathTex("1101001011", color=GREEN)
        bob_string.next_to(group_bob, DOWN)
        # self.play(Write(alice_string), Write(bob_string))


        text_match = Text("Alice and Bob have same password").scale(0.5)
        text_match.next_to(text_left, DOWN)


        alice2 = ImageMobject("pics/alice.png").scale(0.15)
        bob2 = ImageMobject("pics/bob.png").scale(0.4)
        text_alice2 = Text("Alice").scale(0.5)
        text_bob2 = Text("Bob").scale(0.5)
        text_alice2.next_to(alice2, DOWN)
        text_bob2.next_to(bob2, DOWN)
        group_alice2 = Group(alice2, text_alice2)
        group_bob2 = Group(bob2, text_bob2)
        group_alice2.shift(RIGHT*2)
        group_bob2.shift(RIGHT*5)
        # self.play(FadeIn(group_alice2), FadeIn(group_bob2))




        alice_string2 = MathTex("1101001011", color=RED)
        alice_string2.next_to(group_alice2, DOWN)
        bob_string2 = MathTex("1100001010", color=RED)
        bob_string2.next_to(group_bob2, DOWN)
        # self.play(Write(alice_string2), Write(bob_string2))


        text_no_match = Text("Alice and Bob have different passwords").scale(0.5)
        text_no_match.next_to(text_right, DOWN)
        # self.play(Write(text_no_match))




        # text_update = MathTex(r"\text{Bob detects equality with }100\% \text{ accuracy}").scale(0.5)
        text_update_1 = MathTex(r"\text{Bob makes correct conclusion}")
        text_update_2 = MathTex(r"100\% \text{ of the time}")
        # group = Group(text_update_1, text_update_2)
        text_update_1.move_to((alice_string.get_center() + bob_string.get_center())/2 + DOWN*0.8)
        text_update_2.next_to(text_update_1, DOWN)
        self.play(
            FadeIn(line),
            FadeIn(text_left),
            FadeIn(text_right),
            FadeIn(group_alice),
            FadeIn(group_bob),
            FadeIn(alice_string),
            FadeIn(bob_string),
            FadeIn(group_alice2),
            FadeIn(group_bob2),
            FadeIn(alice_string2),
            FadeIn(bob_string2),
            FadeIn(text_match),
            FadeIn(text_no_match),
            FadeIn(text_update_1),
            FadeIn(text_update_2)
        )
        self.wait(1)
        

        text_update_bob_1 = MathTex(r"\text{Bob errors with probability } \leq \frac{1}{n}").scale(0.8)
        text_update_bob_1.move_to((alice_string2.get_center() + bob_string2.get_center())/2 + DOWN*1.1)
        self.play(Write(text_update_bob_1))
        self.wait(2)

        text_update_trans = MathTex(r"\text{Bob makes the correct conclusion }").scale(0.8)
        text_update_trans_2 = MathTex(r"\text{with probability } \geq 1 - \frac{1}{n}").scale(0.8)
        text_update_trans.move_to((alice_string2.get_center() + bob_string2.get_center())/2 + DOWN*0.8)
        text_update_trans_2.next_to(text_update_trans, DOWN)
        group = VGroup(text_update_trans, text_update_trans_2)
        self.play(Transform(text_update_bob_1, group))
        self.wait(2)


        

        target_text = MathTex(r"\text{Bob makes the correct conclusion with probability } \geq 1 - \frac{1}{n}").scale(0.8)
        target_text.move_to(UP*3)
        group_update_text = VGroup(text_update_trans, text_update_trans_2)
        # self.play(Transform(group_update_text, target_text))
        self.wait(2)
        self.play(
            FadeOut(line),
            FadeOut(text_left),
            FadeOut(text_right),
            FadeOut(group_alice),
            FadeOut(group_bob),
            FadeOut(alice_string),
            FadeOut(bob_string),
            FadeOut(group_alice2),
            FadeOut(group_bob2),
            FadeOut(alice_string2),
            FadeOut(bob_string2),
            FadeOut(text_match),
            FadeOut(text_no_match),
            FadeOut(text_update_1),
            FadeOut(text_update_2),
            FadeOut(text_update_bob_1),
            FadeOut(text_update_trans),
            FadeOut(text_update_trans_2),
            Transform(group_update_text, target_text)
        )
        self.add(target_text)

        table = VGroup(
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("n (number of characters)", font_size=26, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("Accuracy", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("100", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\geq 1 - \frac{1}{100} = 99\%", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("1000", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\geq 1- \frac{1}{1000} = 99.9\%", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
            VGroup(
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                Text("10000", font_size=36, color=BLUE)),
                VGroup(Rectangle(width=4, height=1, fill_opacity=0),
                MathTex(r"\geq 1 - \frac{1}{10000} = 99.99\%", font_size=36 , color=BLUE))
            ).arrange(RIGHT, buff=0), 
        ).arrange(DOWN, buff=0)
        # Animate each row one at a time
        self.play(Write(table))
        self.wait(2)


                                    