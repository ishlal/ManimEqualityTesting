from manim import *

class Scene6(Scene):
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
        self.play(Write(alice_char_group), Write(bob_char_group))
        self.wait(0.2)


        for i in range(10):
            char_obj = MathTex(alice_string[i], color=WHITE)
            char_obj.move_to(alice_char_group[i])
            self.play(ApplyMethod(char_obj.shift, DOWN), run_time=0.1)
            self.play( ApplyMethod(char_obj.move_to, bob_char_group[i].get_center() + DOWN*0.5), run_time=0.2 )
            self.wait(0.2)
            if alice_string[i] == bob_string[i]:
                self.play(ApplyMethod(char_obj.set_color, GREEN), ApplyMethod(bob_char_group[i].set_color, GREEN), run_time=0.1)
                self.wait(0.1)
            else:
                self.play(ApplyMethod(char_obj.set_color, RED), ApplyMethod(bob_char_group[i].set_color, RED), run_time=0.1)
                self.wait(0.1)
                break
        self.wait(1)
        image = ImageMobject("pics/equal.png").scale(1)
        image.move_to(group_bob.get_center() + UP*2 + LEFT*2)
        self.play(FadeIn(image))

class Scene5(Scene):
    def construct(self):
        # opening slide
        title = Text("A First Approach").scale(1.5)
        self.play(Write(title), run_time=1)
        self.wait(0.5)
        # self.play(FadeOut(title))

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

        self.play(FadeOut(title), FadeIn(group_alice), FadeIn(group_bob))

        self.wait(0.3)

        # create a group of text objects
        alice_string = "1101001011"
        alice_char_group = VGroup()
        for char in alice_string:
            char_obj = MathTex(char, color=WHITE)
            alice_char_group.add(char_obj)

        bob_string = "0001001011"
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
        self.wait(2)

        # animate the first element of alice_char_group shifting down
        # and the first element of bob_char_group shifting up
        char_obj_first = MathTex("1", color=WHITE)
        char_obj_first.move_to(alice_char_group[0])
        self.play(ApplyMethod(char_obj_first.shift, DOWN))
        self.play( ApplyMethod(char_obj_first.move_to, bob_char_group[0].get_center() + DOWN*0.5) )
        self.wait(0.5)
        self.play(ApplyMethod(char_obj_first.set_color, RED), ApplyMethod(bob_char_group[0].set_color, RED))
        self.wait(2)
        # add image mobject
        image = ImageMobject("pics/not_equal.png").scale(1)
        # move image to top left of group_bob
        image.move_to(group_bob.get_center() + UP*2 + LEFT*2)
        self.play(FadeIn(image))
        self.wait(2)
        self.play(FadeOut(image), FadeOut(alice_char_group), FadeOut(bob_char_group), FadeOut(char_obj_first))
        self.wait(1)

        alice_string = "1101001011"
        alice_char_group = VGroup()
        for char in alice_string:
            char_obj = MathTex(char, color=WHITE)
            alice_char_group.add(char_obj)

        bob_string = "1001001011"
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
        self.play(Write(alice_char_group), Write(bob_char_group), run_time=0.5)
        self.wait(0.3)
        char_obj_first2 = MathTex("1", color=WHITE)
        char_obj_first2.move_to(alice_char_group[0])
        self.play(ApplyMethod(char_obj_first2.shift, DOWN))
        self.play( ApplyMethod(char_obj_first2.move_to, bob_char_group[0].get_center() + DOWN*0.5) )
        self.wait(0.5)
        self.play(ApplyMethod(char_obj_first2.set_color, GREEN), ApplyMethod(bob_char_group[0].set_color, GREEN))
        self.wait(0.5)
        image = ImageMobject("pics/continue.png").scale(1)
        image.move_to(group_bob.get_center() + UP*2 + LEFT*2)
        self.play(FadeIn(image))
        self.wait(1)
        self.play(FadeOut(image))

        char_obj_second = MathTex("1", color=WHITE)
        char_obj_second.move_to(alice_char_group[1])
        self.play(ApplyMethod(char_obj_second.shift, DOWN))
        self.play( ApplyMethod(char_obj_second.move_to, bob_char_group[1].get_center() + DOWN*0.5) )
        self.wait(0.5)
        self.play(ApplyMethod(char_obj_second.set_color, RED), ApplyMethod(bob_char_group[1].set_color, RED))
        self.wait(0.5)
        image = ImageMobject("pics/not_equal.png").scale(1)
        image.move_to(group_bob.get_center() + UP*2 + LEFT*2)
        self.play(FadeIn(image))
        self.wait(2)
        self.play(FadeOut(image))

        for i in range(2, 10):
            char_obj = MathTex(alice_string[i], color=WHITE)
            char_obj.move_to(alice_char_group[i])
            self.play(ApplyMethod(char_obj.shift, DOWN), run_time=0.1)
            self.play( ApplyMethod(char_obj.move_to, bob_char_group[i].get_center() + DOWN*0.5), run_time=0.2 )
            self.wait(0.2)
            if alice_string[i] == bob_string[i]:
                self.play(ApplyMethod(char_obj.set_color, GREEN), ApplyMethod(bob_char_group[i].set_color, GREEN), run_time=0.1)
                self.wait(0.1)
            else:
                self.play(ApplyMethod(char_obj.set_color, RED), ApplyMethod(bob_char_group[i].set_color, RED), run_time=0.1)
                self.wait(0.1)
                break
        self.wait(3)
        self.play(Indicate(char_obj_second), Indicate(bob_char_group[1]), run_time=1)
        self.play(Indicate(char_obj_second), Indicate(bob_char_group[1]), run_time=1)
        self.play(Indicate(char_obj_second), Indicate(bob_char_group[1]), run_time=1)
        self.wait(0.5)
        image = ImageMobject("pics/not_equal.png").scale(1)
        image.move_to(group_bob.get_center() + UP*2 + LEFT*2)
        self.play(FadeIn(image))
        self.wait(7)
        # self.play(FadeOut(image), FadeOut(alice_char_group), FadeOut(bob_char_group), FadeOut(char_obj_first2), FadeOut(char_obj_second), FadeOut(char_obj))
        # red_color = RED
        # green_color = GREEN 
        # for i, char in enumerate(string):
        #     color = red_color if char == '1' and i == 3 else green_color
        #     char_obj = MathTex(char, color=color)
        #     char_group.add(char_obj)
        # char_group.arrange(RIGHT, buff=0.1)

    



