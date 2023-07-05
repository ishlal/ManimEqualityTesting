from manim import *

class Scene15(Scene):
    def construct(self):
        text1 = Text("Question", font_size=100, color=BLUE)
        self.play(FadeIn(text1))
        self.wait(0.5)
        self.play(FadeOut(text1))
        text2 = Text("Can we find a procedure that is not deterministic,", font_size=36, color=BLUE)
        text3 = Text("uses less than n characters in its communication", font_size=36, color=YELLOW)
        text4 = Text("but ensures a very high probability of detecting equality?", font_size=36, color=RED)
        text2.shift(UP)
        text4.shift(DOWN)
        self.play(Write(text2), run_time=3)
        self.play(Write(text3), run_time=2.5)
        self.play(Write(text4), run_time=3)
        self.wait(2.5)
class Scene16(Scene):
    def construct(self):
        axes = Axes(
            x_range=[0, 10, 1],
            y_range=[0, 6, 1],
            axis_config={"include_tip": False}
        )

        # make axes smaller
        axes.scale(0.7)

        # Plot the graph
        graph = axes.plot(lambda x: x/2 + 1)
        labels = axes.get_axis_labels(
            Text("Cost").scale(0.7), Text("Accuracy").scale(0.7)
        )

        # Add the point
        point = Dot(axes.c2p(8, 5), color=RED, radius=0.4)
        self.play(FadeIn(axes), Write(graph), Write(labels))
        self.play(FadeIn(point))

        dotted_line = DashedLine(
            start=axes.c2p(0, 5),
            end=point.get_center(),
            color=YELLOW
        )

        dotted_line2 = DashedLine(
            start=axes.c2p(8, 0),
            end=point.get_center(),
            color=YELLOW
        )
        self.play(Write(dotted_line), Write(dotted_line2), run_time=1)


        text = Text("100%", font_size=36, color=BLUE)
        # move text to left of dotted_line
        text.next_to(dotted_line, LEFT)
        text2 = Text("n", font_size=36, color=BLUE)
        # move text to bottom of dotted_line2
        text2.next_to(dotted_line2, DOWN)
        self.play(Write(text), Write(text2))
        self.wait(1)
        self.play(FadeOut(text), FadeOut(text2), FadeOut(dotted_line), FadeOut(dotted_line2))

        # Trace the point down to (2, 2)
        self.play(
            point.animate.move_to(axes.c2p(2, 2)),
            rate_func=smooth,
            run_time=2
        )

        self.wait(1)
        dotted_line = DashedLine(
            start=axes.c2p(0, 2),
            end=point.get_center(),
            color=YELLOW
        )


        dotted_line2 = DashedLine(
            start=axes.c2p(2, 0),
            end=point.get_center(),
            color=YELLOW
        )
        self.play(Write(dotted_line), Write(dotted_line2), run_time=1)


        # Add the text
        text = Text("?", font_size=36, color=BLUE)
        # move text to left of dotted_line
        text.next_to(dotted_line, LEFT)
        text2 = Text("?", font_size=36, color=BLUE)
        # move text to bottom of dotted_line2
        text2.next_to(dotted_line2, DOWN)
        self.play(Write(text), Write(text2))
        text3 = MathTex("99.99%", font_size=36, color=BLUE)
        text3.next_to(dotted_line, LEFT)
        self.wait(1)
        self.play(Transform(text, text3))
        self.wait(2)

