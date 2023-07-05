from manim import *

class StringScene(Scene):
    def construct(self):
        self.wait(1)
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
        self.add(group_alice)
        self.add(group_bob)
        self.wait(1)

        string = "1101001011"
        char_group = VGroup()
        red_color = RED
        green_color = GREEN 
        for i, char in enumerate(string):
            color = red_color if char == '1' and i == 3 else green_color
            char_obj = MathTex(char, color=color)
            char_group.add(char_obj)
        char_group.arrange(RIGHT, buff=0.1)


        string2 = "1100001011"
        char_group2 = VGroup()
        for i, char in enumerate(string2):
            color = red_color if char == '0' and i == 3 else green_color
            char_obj = MathTex(char, color=color)
            char_group2.add(char_obj)
        char_group2.arrange(RIGHT, buff=0.1)

        # place char_group below alice
        char_group.shift(LEFT*4 + DOWN*2)
        # place char_group2 below bob
        char_group2.shift(RIGHT*4 + DOWN*2)
        self.play(Write(char_group), Write(char_group2))
        self.wait(0.7)
        self.play(FadeOut(char_group), FadeOut(char_group2), FadeOut(group_alice), FadeOut(group_bob))
        self.wait(0.5)