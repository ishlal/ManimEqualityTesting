from manim import *
from colour import Color


class Scene19(Scene):
    def construct(self):
        suspect = Square(color = Color(hue=18/25, saturation=1, luminance=0.5),
                         fill_opacity=0.5).scale(0.65)
        text_sus = Text("Suspect").scale(0.5)
        text_sus.move_to(suspect)
        group_sus = VGroup(suspect, text_sus)
        group_sus.shift(LEFT*5 + UP)
        text_height = Text("Height: 180cm").scale(0.5)
        text_height.next_to(group_sus, DOWN)
        text_weight = Text("Weight: 100kg").scale(0.5)
        text_weight.next_to(text_height, DOWN)
        self.add(group_sus, text_height, text_weight)

        hues = [22, 12, 9, 4, 23, 6, 2, 17, 15, 8, 11, 13, 1, 20, 5, 16, 3, 19, 25, 10, 21, 14, 7, 18, 24]

        squares = VGroup(
            *[VGroup(Square(color=Color(hue = hues[j]/25, saturation=1, luminance=0.5),
                     fill_opacity=0.5).scale(0.65),
                     Text("Person " + str(j+1)).scale(0.3)) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0.3)
        squares.shift(RIGHT*2)
        self.play(Write(squares), run_time=1)   
        self.wait(1)
        for i in range(25):
            if i != 23:
                cross = Cross(stroke_width=8).scale(0.8)
                cross.move_to(squares[i][0])
                self.play(Write(cross), run_time=0.1)
        self.wait(1)

class Scene17(Scene):
    def construct(self):
        text2 = Text("Can we find a procedure that is not deterministic,", font_size=36, color=BLUE)
        text3 = Text("uses less than n characters in its communication", font_size=36, color=YELLOW)
        text4 = Text("but ensures a very high probability of detecting equality?", font_size=36, color=RED)
        text2.shift(UP*2)
        text3.shift(UP)
        self.add(text2, text3, text4)
        text5 = Text("Yes!", font_size=100, color=GREEN)
        text5.shift(DOWN*2, LEFT*2)
        self.play(Write(text5))
        self.wait(2)
        text6 = Text("By fingerprinting!", font_size=36, color=GREEN)
        text6.shift(DOWN*2, RIGHT*2)
        self.play(Write(text6))
        self.wait(1)
        


class Scene18(Scene):
    def construct(self):
        squares = VGroup(
            *[VGroup(Square(color=Color(hue = j/25, saturation=1, luminance=0.5),
                     fill_opacity=0.5).scale(0.65),
                     Text("Person " + str(j+1)).scale(0.3)) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0.3)
        squares.shift(RIGHT*2)
        self.play(Write(squares), run_time=5)   
        self.wait(1.5)

        self.play(Indicate(squares[18][0]))
        self.play(Indicate(squares[18][0]))
        text_crim = Text("Criminal").scale(0.5)
        text_crim.move_to(squares[18][1])
        self.play(Transform(squares[18][1], text_crim))
        self.wait(3)

        suspect = Square(color = Color(hue=18/25, saturation=1, luminance=0.5),
                         fill_opacity=0.5).scale(0.65)
        text_sus = Text("Suspect").scale(0.5)
        text_sus.move_to(suspect)
        group_sus = VGroup(suspect, text_sus)
        group_sus.shift(LEFT*5 + UP)
        self.play(Write(group_sus))
        self.wait(0.5)
        text_height = Text("Height: 180cm").scale(0.5)
        text_height.next_to(group_sus, DOWN)
        self.play(Write(text_height))
        self.wait(0.2)
        text_weight = Text("Weight: 100kg").scale(0.5)
        text_weight.next_to(text_height, DOWN)
        self.play(Write(text_weight))
        self.wait(2)

        for i in range(25):
            if i != 18:
                cross = Cross(stroke_width=8).scale(0.8)
                cross.move_to(squares[i][0])
                self.play(Write(cross), run_time=0.1)
        self.wait(1)



        # labels = VGroup(
        #     *[Text("Person" + str(j), font_size=36, color=BLACK).scale(0.5) for j in range(25)]
        # )
        # labels.arrange_in_grid(5, 5, buff=0.5)
        # labels.shift(LEFT*2)
        # self.play(Write(labels), run_time=2)
