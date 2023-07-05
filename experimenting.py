from manim import *

class Positioning(Scene):
    def construct(self):
        # img = ImageMobject("manim.png").scale(0.5)
        # text = Text("Manim is cool").scale(0.5)
        # text.next_to(img, DOWN)
        # # group text and image together
        # group = Group(img, text)

        # square = Square(color=RED, fill_opacity=0.5)
        # square.move_to(UP + RIGHT*2)

        # # animate the group moving to the right
        # self.add(group)
        # self.add(square)
        # # self.play(group.animate.shift(RIGHT))
        # self.wait(1)

        # # animate group's top anchor point moving to square's top anchor point
        # self.play(group.animate.move_to(square.get_top(), aligned_edge=UP))

        alice = ImageMobject("pics/alice.png").scale(0.2)
        bob = ImageMobject("pics/bob.png").scale(0.5)
        text_alice = Text("Alice").scale(0.5)
        text_bob = Text("Bob").scale(0.5)
        text_alice.next_to(alice, DOWN)
        text_bob.next_to(bob, DOWN)
        group_alice = Group(alice, text_alice)
        group_bob = Group(bob, text_bob)
        self.add(group_alice)
        self.play(FadeIn(group_alice))
        self.play(group_alice.animate.shift(LEFT*4 + UP))
        self.wait(1)
        self.play(FadeIn(group_bob))
        self.add(group_bob)
        self.play(group_bob.animate.shift(RIGHT*4 + UP))
        self.wait(2)

        chicago = ImageMobject("pics/chicago.png").scale(0.4)
        chicago_text = Text("Chicago").scale(0.5)
        chicago_text.next_to(chicago, DOWN)
        group_chicago = Group(chicago, chicago_text)
        group_chicago.shift(LEFT*4 + DOWN*2)
        self.add(group_chicago)
        # fade in chicago group below alice
        self.play(FadeIn(group_chicago))
        self.wait(1)

        guangzhou = ImageMobject("pics/guangzhou.png").scale(0.4)
        guangzhou_text = Text("Guangzhou").scale(0.5)
        guangzhou_text.next_to(guangzhou, DOWN)
        group_guangzhou = Group(guangzhou, guangzhou_text)
        group_guangzhou.shift(RIGHT*4 + DOWN*2)
        self.add(group_guangzhou)
        # fade in guangzhou group below bob
        self.play(FadeIn(group_guangzhou))
        self.wait(1)
        self.play(FadeOut(group_chicago), FadeOut(group_guangzhou))
        self.wait(0.5) 


        netflix = ImageMobject("pics/netflix.png").scale(0.4)
        netflix.shift(DOWN*2)
        self.add(netflix)
        self.play(FadeIn(netflix))
        self.wait(1)

        # create an arrow from DOWN RIGHT anchor point of Alice to TOP LEFT anchor point of netflix
        arrow_alice_netflix = Arrow(alice.get_corner(DOWN + RIGHT), netflix.get_corner(UP + LEFT), color=RED)
        arrow_bob_netflix = Arrow(bob.get_corner(DOWN + LEFT), netflix.get_corner(UP + RIGHT), color=RED) 
        self.add(arrow_alice_netflix)
        self.add(arrow_bob_netflix)
        self.play(FadeIn(arrow_alice_netflix), FadeIn(arrow_bob_netflix))
        self.wait(2)
    



