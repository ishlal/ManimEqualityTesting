from manim import *

class Scene13(Scene):
    def construct(self):
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


        self.wait(0.3)
        alice_string = "1101001011"
        # put each character of the string in a rectangle and arrange right
        alice_char_group = VGroup()
        for char in alice_string:
            char_obj = VGroup(Rectangle(width=0.5, height=1, fill_opacity=0), MathTex(char, color=WHITE))
            alice_char_group.add(char_obj)
        alice_char_group.arrange(RIGHT, buff=0)
        # place char_group below alice
        alice_char_group.next_to(group_alice, DOWN)


        bob_blank_group = VGroup()
        for _ in alice_string:
            char_obj = Rectangle(width=0.5, height=1, fill_opacity=0)
            bob_blank_group.add(char_obj)
        bob_blank_group.arrange(RIGHT, buff=0)
        # place char_group2 below bob
        bob_blank_group.next_to(group_bob, DOWN)
        self.play(FadeIn(group_alice), FadeIn(group_bob), Write(alice_char_group), Write(bob_blank_group), run_time=2)
        self.wait(0.3)
        text_num_bits = Text("Number of bits sent: ")
        counter = Text("0/10", color=WHITE)
        counter.next_to(text_num_bits, RIGHT)
        text_num_bits.shift(UP*3)
        counter.shift(UP*3)
        self.play(Write(text_num_bits), run_time=0.3)
        self.play(Write(counter), run_time=0.3)
        count_val = 0
        for i in range(5):
            if i!= 3:
                if i < 5:
                    self.play(Indicate(alice_char_group[i][0]))
                else:
                    self.play(Indicate(alice_char_group[i][0]), run_time=0.2)
                char_obj = MathTex(alice_string[i], color=WHITE)
                char_obj.move_to(alice_char_group[i][1])
                # increment the value of counter
                # value_text.set_text(f"Value: {value}")
                
                count_val += 1
                new_counter = Text(f"{count_val}/10", color=WHITE)
                new_counter.next_to(text_num_bits, RIGHT)
                
                if i < 5:
                    self.play(ApplyMethod(char_obj.shift, DOWN), run_time=0.3)
                    self.play( ApplyMethod(char_obj.move_to, bob_blank_group[i].get_center()), run_time=0.3)
                    self.play(Indicate(counter), run_time=0.3)
                    self.play(Transform(counter, new_counter), run_time=0.3)
                    self.play(ApplyMethod(char_obj.set_color, GREEN), ApplyMethod(bob_blank_group[i].set_color, GREEN), run_time=0.2)
                else:
                    self.play(ApplyMethod(char_obj.shift, DOWN), run_time=0.1)
                    self.play( ApplyMethod(char_obj.move_to, bob_blank_group[i].get_center()), run_time=0.1)
                    self.play(Transform(counter, new_counter), run_time = 0.3)
                    self.play(ApplyMethod(char_obj.set_color, GREEN), ApplyMethod(bob_blank_group[i].set_color, GREEN), run_time=0.1)
        
        # char_group = VGroup(*[alice_char_group[i][1] for i in range(5, 10)])
        char_group = VGroup(*[MathTex(alice_string[i], color=WHITE).move_to(alice_char_group[i][1]) for i in range(5, 10)])
        # char_group.arrange(RIGHT, buff=0.5)
        char_group.move_to(alice_char_group[7].get_center())
        self.play(Indicate(char_group))
        self.play(ApplyMethod(char_group.shift, DOWN), run_time=0.3)
        self.play( ApplyMethod(char_group.move_to, bob_blank_group[7].get_center()), run_time=0.3)
        self.play(Indicate(counter))
        new_counter = Text("9/10", color=WHITE)
        new_counter.next_to(text_num_bits, RIGHT)
        self.play(Transform(counter, new_counter), run_time=0.3)
        self.play(ApplyMethod(char_group.set_color, GREEN), ApplyMethod(bob_blank_group[5].set_color, GREEN),
                  ApplyMethod(bob_blank_group[6].set_color, GREEN), ApplyMethod(bob_blank_group[7].set_color, GREEN),
                   ApplyMethod(bob_blank_group[8].set_color, GREEN), ApplyMethod(bob_blank_group[9].set_color, GREEN), run_time=0.2)

        self.wait(0.5)
        self.play(ApplyMethod(alice_char_group[3][1].set_color, RED), ApplyMethod(bob_blank_group[3].set_color, RED), run_time=0.2)
        self.wait(2)

        option1 = Text("0", color=RED)
        option2 = Text("1", color=RED)
        option1.next_to(bob_blank_group[3], DOWN*4 + LEFT*0.5)
        option2.next_to(bob_blank_group[3], DOWN*4 + RIGHT*0.5)
        self.play(FadeIn(option1), FadeIn(option2), run_time=0.7)
        # draw arrow from bottom of bob_blank_group[3][1] to option1
        arrow = Arrow(bob_blank_group[3].get_bottom(), option1.get_top(), color=RED)
        arrow2 = Arrow(bob_blank_group[3].get_bottom(), option2.get_top(), color=RED)
        self.play(GrowArrow(arrow), GrowArrow(arrow2), run_time=0.4)
        self.wait(1)
        self.play(FadeOut(arrow), FadeOut(arrow2), FadeOut(option1), FadeOut(option2))
        strin1 = "1101001011"
        group_string1 = VGroup(*[MathTex(strin1[i], color=WHITE) for i in range(len(strin1))])
        strin2 = "1100001011"
        group_string2 = VGroup(*[MathTex(strin2[i], color=WHITE) for i in range(len(strin2))])
        # write strin1 below bob_blank_group
        group_string1.arrange(RIGHT, buff=0.35)
        group_string1.next_to(bob_blank_group, DOWN)
        self.play(Write(group_string1), run_time=2)
        self.wait(0.5)

        # write strin2 below bob_blank_group
        group_string2.arrange(RIGHT, buff=0.35)
        group_string2.next_to(group_string1, DOWN)
        self.play(Write(group_string2), run_time=2)
        self.wait(1)

        qmark = Text("?", color=RED, font_size=120)
        self.play(FadeIn(qmark))
        self.wait(2)
