from manim import *

class Positioning(Scene):
    def construct(self):
        #Auxiliary mobject
        plane = NumberPlane()
        self.add(plane)

        # next_to
        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN)
        green_dot.next_to(red_dot, RIGHT + UP) # RIGHT = [1, 0, 0]
        self.add(red_dot, green_dot)

        # shift
        s = Square(color=ORANGE)
        s.shift(4 * RIGHT + 2 * UP)
        self.add(s)

        # move_to (by anchor point. Default is center)
        c = Circle(color=PURPLE)
        c.move_to([-3, -2, 0])
        self.add(c)

        # align_to
        c2 = Circle(radius=0.5, color=RED, fill_opacity=0.5)
        c3 = c2.copy().set_color(YELLOW)
        c4 = c2.copy().set_color(ORANGE)
        # align with square --> c2 is originally in origin
        # will shift c2 so that upper part of circle is aligned with upper part of square
        c2.align_to(s, UP)
        c3.align_to(s, RIGHT)
        c4.align_to(s, UP + RIGHT)
        self.add(c2, c3, c4)


class CriticalPoints(Scene):
    def construct(self):
        c = Circle(color=GREEN, fill_opacity=0.5)
        self.add(c)
        # list all critical points
        for d in [(0, 0, 0), UP, DOWN, LEFT, RIGHT, UL, UR, DL, DR]:
            self.add(Cross(scale_factor=0.2).move_to(c.get_critical_point(d)))

        s = Square(color=RED, fill_opacity=0.5)
        # move left anchor point to (1, 0, 0)
        s.move_to([1, 0, 0], aligned_edge=LEFT)
        self.add(s)

from manim.utils.unit import Percent, Pixels

class UsefulUnits(Scene):
    def construct(self):
        for perc in range(5, 50, 5):
            self.add(Circle(radius=perc * Percent(X_AXIS)))
            self.add(Square(side_length=2*perc * Percent(Y_AXIS), color=YELLOW))
        d = Dot()
        d.shift(100 * Pixels * RIGHT)
        self.add(d)


class Grouping(Scene):
    def construct(self):
        #mobject groups

        red_dot = Dot(color=RED)
        green_dot = Dot(color=GREEN).next_to(red_dot, RIGHT)
        blue_dot = Dot(color=BLUE).next_to(red_dot, UP)
        dot_group = VGroup(red_dot, green_dot, blue_dot)
        dot_group.to_edge(RIGHT)
        self.add(dot_group)

        circles = VGroup(*[Circle(radius=0.2) for _ in range(10)])
        circles.arrange(UP, buff=0.5)
        self.add(circles)

        stars = VGroup(*[Star(n=5, color=YELLOW, fill_opacity=1).scale(0.5) for _ in range(20)])
        stars.arrange_in_grid(4, 5, buff=0.5)
        self.add(stars)