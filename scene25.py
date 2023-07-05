from manim import *

class Scene25(Scene):
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
            MathTex(r"\text{Cost with } n = 10^{10}").scale(0.7), Text("Accuracy").scale(0.7)
        )

        # Add the point
        point = Dot(axes.c2p(2, 2), color=RED, radius=0.4)
        self.play(FadeIn(axes), Write(graph), Write(labels))
        self.play(FadeIn(point))


        # self.wait(1)
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
        text3 = MathTex(">99.99\%", font_size=36, color=BLUE)
        text3.next_to(dotted_line, LEFT)
        self.wait(1)
        self.play(Transform(text, text3))
        self.wait(0.3)
        text4 = MathTex("< 200", font_size=36, color=BLUE)
        text4.next_to(dotted_line2, DOWN)
        self.play(Transform(text2, text4))
        self.wait(1)

        # # Trace the point down to (2, 2)
        self.play(
            point.animate.move_to(axes.c2p(8, 5)),
            rate_func=smooth,
            run_time=2
        )
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
        self.play(Write(dotted_line), Write(dotted_line2), run_time=0.5)
        text5 = MathTex("100\%", font_size=36, color=BLUE)
        text5.next_to(dotted_line, LEFT)
        text6 = MathTex("10^{10}", font_size=36, color=BLUE)
        text6.next_to(dotted_line2, DOWN)
        self.play(Write(text5), Write(text6))
        self.wait(2)

