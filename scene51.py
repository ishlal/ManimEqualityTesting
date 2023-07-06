from manim import *

class Scene51(Scene):
    def construct(self):
        recap = MathTex(r"\text{Recap}", font_size=100)
        self.play(Write(recap))
        self.wait(1)
        self.play(FadeOut(recap))
        text_1 = MathTex(r"1. \text{ Deterministic solution requires } n \text{ bit communication}")
        text_1.shift(UP)
        self.play(Write(text_1))
        self.wait(2)
        text_2 = MathTex(r"2. \text{ Using fingerprinting, we can significantly} \\ \
                         \text{reduce communication cost}")
        text_2.shift(DOWN)
        self.play(Write(text_2))
        self.wait(2)
        self.play(
            FadeOut(text_1),
            FadeOut(text_2)
        )

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
        self.play(FadeIn(group_alice), FadeIn(group_bob))


        alice_graph = Graph(
            vertices=[1, 2, 3, 4, 5, 6, 7, 8],
            edges=[(1, 5), (1, 6), (1, 7),
                   (2, 5), (2, 6), (2, 8),
                   (3, 5), (3, 7), (3, 8),
                   (4, 6), (4, 7), (4, 8)],
            layout="partite",
            partitions=[[1, 2, 3, 4], [5, 6, 7, 8]]
        ).scale(0.5)
        alice_graph.next_to(group_alice, DOWN)
        self.play(Write(alice_graph))

        bob_graph = Graph(
            vertices=[1, 2, 3, 4, 5, 6, 7, 8],
            edges=[(1, 2), (1, 4), (1, 5),
                   (2, 3), (2, 6),
                   (3, 4), (3, 7),
                   (4, 8),
                   (5, 6), (5, 7), 
                   (6, 7), (7, 8)],
            layout="shell"
        ).scale(0.6)
        bob_graph.next_to(group_bob, DOWN)
        self.play(Write(bob_graph))
        self.wait(1)
        img_fp = ImageMobject("pics/fingerprint.png").scale(0.5)
        img_fp.next_to(alice_graph, RIGHT)
        self.play(FadeIn(img_fp))
        self.wait(0.5)
        self.play(
            img_fp.animate.move_to(bob_graph.get_center() + LEFT*2.5)
        )
        self.wait(0.5)
        iso = ImageMobject("pics/isomorphic.png").scale(2)
        iso.next_to(bob, LEFT)
        iso.shift(UP*0.5)
        self.play(FadeIn(iso))
        self.wait(1.5)
        self.play(
            FadeOut(img_fp),
            FadeOut(iso),
            FadeOut(alice_graph),
            FadeOut(bob_graph),
            FadeOut(group_alice),
            FadeOut(group_bob)
        )


