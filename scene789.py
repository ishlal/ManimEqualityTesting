from manim import *
 
class Scene7(Scene):
    def construct(self):
        pw_reqs = Text("Observations:").scale(0.8)
        pw_reqs.shift(UP)
        req1 = Tex(r"\text{1. }", r"\text{Alice always sends all }", r"$n$", r"\text{ characters to Bob}").scale(0.8)

        req2 = Tex(r"\text{2. }", r"\text{Only Bob will know whether or not the passwords match}").scale(0.8)
        req2.shift(DOWN)
        # self.add(pw_reqs, req1)
        self.wait(1)
        self.play(FadeIn(pw_reqs))
        self.wait(1.5)
        self.play(FadeIn(req1))
        self.wait(3)
        self.play(FadeIn(req2))
        self.wait(3)
        self.play(FadeOut(req1), FadeOut(req2), FadeOut(pw_reqs)) 

class Scene8(Scene):
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
        self.add(group_alice, group_bob)


        alice_string = "1101001011"
        alice_char_group = VGroup()
        for char in alice_string:
            char_obj = MathTex(char, color=WHITE)
            alice_char_group.add(char_obj)

        bob_string = "1101001011"
        bob_char_group = VGroup()
        for char in bob_string:
            char_obj = MathTex(char, color=WHITE)
            bob_char_group.add(char_obj)
        alice_char_group.arrange(RIGHT, buff=0.1)
        bob_char_group.arrange(RIGHT, buff=0.1)
        # place char_group below alice
        alice_char_group.next_to(group_alice, DOWN)
        # place char_group2 below bob
        bob_char_group.next_to(group_bob, DOWN)
        self.play(Write(alice_char_group), run_time=1.5)
        self.play(Write(bob_char_group), run_time=1.5)
        for i in range(10):
            self.play(ApplyMethod(alice_char_group[i].set_color, GREEN), ApplyMethod(bob_char_group[i].set_color, GREEN), run_time=0.3)
        self.wait(2)

        image = ImageMobject("pics/one.png").scale(1)
        image.move_to(group_bob.get_center() + UP*2 + LEFT*2)
        self.play(FadeIn(image))
        self.wait(2)


class Scene9(Scene):
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
        self.add(group_alice, group_bob)


        alice_string = "1101001011"
        alice_char_group = VGroup()
        for char in alice_string:
            char_obj = MathTex(char, color=WHITE)
            alice_char_group.add(char_obj)

        bob_string = "1111101011"
        bob_char_group = VGroup()
        for char in bob_string:
            char_obj = MathTex(char, color=WHITE)
            bob_char_group.add(char_obj)
        alice_char_group.arrange(RIGHT, buff=0.1)
        bob_char_group.arrange(RIGHT, buff=0.1)
        # place char_group below alice
        alice_char_group.next_to(group_alice, DOWN)
        # place char_group2 below bob
        bob_char_group.next_to(group_bob, DOWN)
        self.play(Write(alice_char_group), Write(bob_char_group))
        for i in range(10):
            if alice_string[i] == bob_string[i]:
                self.play(ApplyMethod(alice_char_group[i].set_color, GREEN), ApplyMethod(bob_char_group[i].set_color, GREEN), run_time=0.1)
            else:
                self.play(ApplyMethod(alice_char_group[i].set_color, RED), ApplyMethod(bob_char_group[i].set_color, RED), run_time=0.1)
        self.wait(2)

        image = ImageMobject("pics/zero.png").scale(1)
        image.move_to(group_bob.get_center() + UP*2 + LEFT*2)
        self.play(FadeIn(image))
        self.wait(2)