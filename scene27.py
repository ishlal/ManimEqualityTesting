from manim import *

class Scene27(Scene):
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
        self.add(group_alice, group_bob)

        text_bits_communicated = Text("Bits communicated:", font_size=36, color=BLUE)
        text_bits_communicated.to_edge(DOWN)
        text_bits_communicated.shift(LEFT)
        

        alice_string = MathTex("a = 1101001011")
        alice_string.next_to(group_alice, DOWN)
        self.add(alice_string)

        bob_string = MathTex("b = 1100001011")
        bob_string.next_to(group_bob, DOWN)
        self.add(bob_string)

        self.play(Write(text_bits_communicated))
        self.wait(1)


        alice_string_send = Text("11011")
        alice_string_send.next_to(alice_string, DOWN)
        alice_string_send.shift(DOWN*0.5)
        self.play(FadeIn(alice_string_send))
        arrow = (Arrow(alice_string_send.get_bottom(), group_bob.get_center()+DOWN*3.3, color=RED))
        self.play(GrowArrow(arrow))
        self.wait(0.5)
        self.play(alice_string_send.animate.move_to(group_bob.get_center() + DOWN*3.3))
        self.wait(2)

        text_check = MathTex(" < 2^{10} = 2^{n} ")
        text_check.next_to(alice_string_send, DOWN)
        self.play(Write(text_check))
        self.wait(1)
        image_check = ImageMobject("pics/check2.png").scale(0.2)
        image_check.move_to(text_check.get_center() + RIGHT*2)
        self.play(FadeIn(image_check))
        self.wait(1)

        text_bits_comm = MathTex("5 < n")
        text_bits_comm.next_to(text_bits_communicated, RIGHT)
        self.play(Write(text_bits_comm))
        self.wait(2)
        # Fade out everything
        #remove arrow
        self.remove(arrow)
        self.play(
            FadeOut(text_bits_communicated),
            FadeOut(text_bits_comm),
            FadeOut(alice_string),
            FadeOut(bob_string),
            FadeOut(alice_string_send),
            FadeOut(image_check),
            FadeOut(text_check),
            FadeOut(arrow),
            FadeOut(group_alice),
            FadeOut(group_bob)
        )
        self.wait(1)
        
