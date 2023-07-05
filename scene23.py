from manim import *

class Scene23(Scene):
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

        alice_string = Text("1101001011")
        alice_string.next_to(group_alice, DOWN)
        self.play(FadeIn(alice_string))

        fingerprint = ImageMobject("pics/fingerprint.png").scale(0.3)
        fingerprint.move_to(alice_string.get_center() + DOWN*2)
        arrow = Arrow(alice_string.get_bottom(), fingerprint.get_top(), color=RED)
        self.play(GrowArrow(arrow))
        self.wait(1)
        self.play(FadeIn(fingerprint))
        self.wait(1)

        # animate fingerprint moving to below bob
        arrow2 = Arrow(fingerprint.get_center(), group_bob.get_center()+DOWN*2.5, color=RED)
        self.play(GrowArrow(arrow2))
        self.wait(0.5)
        self.play(fingerprint.animate.move_to(group_bob.get_center() + DOWN*2.5))
        self.wait(0.8)

        bob_string = Text("1101001011", color=GREEN)
        bob_string.move_to(fingerprint.get_bottom() + DOWN*1.5)
        arrow3 = Arrow(fingerprint.get_bottom(), bob_string.get_top(), color=RED)
        self.play(GrowArrow(arrow3))
        self.wait(1)
        self.play(FadeIn(bob_string))
        self.wait(2)

        # arrow = Arrow(bob_blank_group[3].get_bottom(), option1.get_top(), color=RED)
        # arrow2 = Arrow(bob_blank_group[3].get_bottom(), option2.get_top(), color=RED)
        # self.play(GrowArrow(arrow), GrowArrow(arrow2), run_time=0.4)
        