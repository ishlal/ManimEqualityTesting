from manim import *
from colour import Color


# NEED TO PAUSE AFTER CROSSES AND MAKE A GUESS!

class Scene21(Scene):
    def construct(self):
        finger = ImageMobject("pics/fingerprint.png").scale(0.5)
        squares = VGroup(
            *[VGroup(Square(color=Color(hue = j/25, saturation=1, luminance=0.5),
                     fill_opacity=0.5).scale(0.65),
                     Text("Person " + str(j+1)).scale(0.3)) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0.3)
        text_crim = Text("Criminal").scale(0.5)
        text_crim.move_to(squares[18][1])
        Transform(squares[18][1], text_crim)

        squares.shift(RIGHT*2)
        self.play(Write(squares), run_time=3)   
        self.wait(1.5)
        finger.shift(LEFT*5 + UP)
        self.play(FadeIn(finger))
        pred_square = Square().scale(0.65)
        # MOVE PRED_SQUARE BELOW FINGER
        pred_square.shift(LEFT*5 + DOWN*2)
        text_pred = Text("Prediction").scale(0.5)
        # move text_pred under pred_square
        text_pred.next_to(pred_square, DOWN)
        self.play(FadeIn(pred_square), Write(text_pred))
        for i in range(25):
            if i not in [6, 18, 21]:
                cross = Cross(stroke_width=8).scale(0.8)
                cross.move_to(squares[i][0])
                self.play(Write(cross), run_time=0.1)
        self.wait(1)
        self.play(Indicate(squares[6][0]))
        self.play(Indicate(squares[18][0]))
        self.play(Indicate(squares[21][0]))
        self.wait(1)
        self.play(squares[6].animate.move_to(pred_square))
        self.wait(1)
        c = Cross(stroke_width=8, scale_factor=0.4)
        c.next_to(pred_square, RIGHT)
        self.play(FadeIn(c))
        self.wait(1)

class Scene22(Scene):
    def construct(self):
        finger = ImageMobject("pics/fingerprint.png").scale(0.5)
        hues = [22, 12, 9, 4, 23, 6, 2, 17, 15, 8, 11, 13, 1, 20, 5, 16, 3, 19, 25, 10, 21, 14, 7, 18, 24] 
        finger.shift(LEFT*5 + UP)
        self.add(finger)
        pred_square = Square().scale(0.65)
        # MOVE PRED_SQUARE BELOW FINGER
        pred_square.shift(LEFT*5 + DOWN*2)
        text_pred = Text("Prediction").scale(0.5)
        # move text_pred under pred_square
        text_pred.next_to(pred_square, DOWN)
        self.play(FadeIn(pred_square), Write(text_pred))
        self.wait(1)

        squares = VGroup(
            *[VGroup(Square(color=Color(hue = hues[j]/25, saturation=1, luminance=0.5),
                     fill_opacity=0.5).scale(0.65),
                     Text("Person " + str(j+1)).scale(0.3)) for j in range(25)]
        ).arrange_in_grid(5, 5, buff=0.3)
        text_crim = Text("Criminal").scale(0.5)
        text_crim.move_to(squares[18][1])
        Transform(squares[18][1], text_crim)

        squares.shift(RIGHT*2)
        self.play(Write(squares), run_time=1)   
        self.wait(1)
        
        for i in range(25):
            if i not in [3, 10, 17]:
                cross = Cross(stroke_width=8).scale(0.8)
                cross.move_to(squares[i][0])
                self.play(Write(cross), run_time=0.1)
        self.wait(2)
        self.play(Indicate(squares[3][0]))
        self.play(Indicate(squares[10][0]))
        self.play(Indicate(squares[17][0]))
        self.wait(1)
        # self.play(squares[10][0]..anmove_to, pred_square)
        self.play(squares[17].animate.move_to(pred_square))
        self.wait(2)
        check = ImageMobject("pics/check2.png").scale(0.25)
        check.next_to(pred_square, RIGHT)
        self.play(FadeIn(check))



class Scene20(Scene):
    def construct(self):
        # draw a line down the middle of the screen
        line = Line(start=UP*3, end=DOWN*3)
        self.play(Write(line))
        self.wait(1)
        # text for left side of screen
        text_left = Text("Before").scale(2)
        text_left.move_to(LEFT*3 + UP*3)
        self.play(Write(text_left))
        # text for right side of screen
        text_right = Text("Now").scale(2)
        text_right.move_to(RIGHT*3 + UP*3)
        self.play(Write(text_right))
        self.wait(1)
        suspect = Square(color = Color(hue=18/25, saturation=1, luminance=0.5),
                         fill_opacity=0.5).scale(0.65)
        text_sus = Text("Suspect").scale(0.5)
        text_sus.move_to(suspect)
        group_sus = VGroup(suspect, text_sus)
        # move suspect to left side of screen
        group_sus.move_to(LEFT*3)
        self.play(FadeIn(group_sus))
        text_height = Text("Height: 180cm").scale(0.5)
        text_height.next_to(group_sus, DOWN)
        text_weight = Text("Weight: 100kg").scale(0.5)
        text_weight.next_to(text_height, DOWN)
        self.play(Write(text_height))
        self.play(Write(text_weight))

        # image for right side
        image = ImageMobject("pics/fingerprint.png").scale(0.5)
        image.move_to(RIGHT*3)
        self.play(FadeIn(image))
        self.wait(1)