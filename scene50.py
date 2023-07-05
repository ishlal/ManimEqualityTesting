from manim import *

class Scene50(Scene):
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
        point = Dot(axes.c2p(2, 2), color=GREEN, radius=0.4)
        self.play(FadeIn(axes), Write(graph), Write(labels), run_time=0.5)



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

        point2 = Dot(axes.c2p(8, 5), color=RED, radius=0.4)
        self.play(FadeIn(point), FadeIn(point2))
        dotted_line3 = DashedLine(
            start=axes.c2p(0, 5),
            end=point2.get_center(),
            color=YELLOW
        )
        dotted_line4 = DashedLine(
            start=axes.c2p(8, 0),
            end=point2.get_center(),
            color=YELLOW
        )

        self.play(Write(dotted_line), Write(dotted_line2), Write(dotted_line3), Write(dotted_line4), run_time=0.5)


        # Add the text
        self.wait(1)

        text3 = MathTex(">99.99\%", font_size=36, color=RED)
        text3.next_to(dotted_line, LEFT)
        text4 = MathTex("\leq 198", font_size=36, color=GREEN)
        text4.next_to(dotted_line2, DOWN)
        self.wait(1)
        self.play(Write(text3), Write(text4))
        self.wait(1)
        text5 = MathTex("100\%", font_size=36, color=GREEN)
        text5.next_to(dotted_line3, LEFT)
        text6 = MathTex("10^{10}", font_size=36, color=RED)
        text6.next_to(dotted_line4, DOWN)
        self.play(Write(text5), Write(text6))

        self.wait(3)
        self.play(
            FadeOut(text3),
            FadeOut(text4),
            FadeOut(text5),
            FadeOut(text6),
            FadeOut(dotted_line),
            FadeOut(dotted_line2),
            FadeOut(dotted_line3),
            FadeOut(dotted_line4),
            FadeOut(point),
            FadeOut(point2),
            FadeOut(graph),
            FadeOut(labels),
            FadeOut(axes),
        )
