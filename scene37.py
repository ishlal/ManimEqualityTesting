from manim import *

class Scene37(Scene):
    def construct(self):

        def_c = MathTex("C = |a - b|")
        def_c.shift(UP*2)

        pr_error = MathTex(r"\Pr[", r"\text{error}", r"]")
        pr_err_eq = MathTex("= \Pr[")
        pr_err_eq_oop = MathTex(r"a \bmod p = b \bmod p", color=RED)
        pr_err_eq_2 = MathTex(r"\mid")
        pr_err_eq_3 = MathTex(r"a \neq b", color=GREEN)
        pr_err_eq_4 = MathTex(r"]")
        pr_err_eq_oop.next_to(pr_err_eq, RIGHT)
        pr_err_eq_2.next_to(pr_err_eq_oop, RIGHT)
        pr_err_eq_3.next_to(pr_err_eq_2, RIGHT)
        pr_err_eq_4.next_to(pr_err_eq_3, RIGHT)
        pr_err_eq_group = Group(pr_err_eq, pr_err_eq_oop, pr_err_eq_2, pr_err_eq_3, pr_err_eq_4)

        pr_error.shift(UP)
        pr_err_eq_group.next_to(pr_error, DOWN)
        pr_err_eq_group.shift(DOWN*0.5)

        self.play(Write(def_c))
        self.wait(1)
        self.play(Write(pr_error))
        self.wait(1)
        anim_group_write = AnimationGroup(
            Write(pr_err_eq),
            Write(pr_err_eq_oop),
            Write(pr_err_eq_2),
            Write(pr_err_eq_3),
            Write(pr_err_eq_4),
            lag_ratio=0.5,
            run_time=2
        )
        # self.play(Write(pr_err_eq))
        # self.play(Write(pr_err_eq_oop))
        # self.play(Write(pr_err_eq_2))
        # self.play(Write(pr_err_eq_3))
        # self.play(Write(pr_err_eq_4))
        self.play(anim_group_write)
        self.wait(2)

        # Now, we can use the definition of C to rewrite the probability of error.
        pr_err_eq_c = MathTex("=\Pr[")
        pr_err_eq_c.next_to(pr_err_eq, DOWN, buff=0.5)
        pr_err_eq_c_oop = MathTex(r"C \bmod p = 0", color=RED)
        pr_err_eq_c_2 = MathTex(r"\mid")
        pr_err_eq_c_3 = MathTex(r"C \neq 0", color=GREEN)
        pr_err_eq_c_4 = MathTex(r"]")
        pr_err_eq_c_oop.next_to(pr_err_eq_c, RIGHT)
        pr_err_eq_c_2.next_to(pr_err_eq_c_oop, RIGHT)
        pr_err_eq_c_3.next_to(pr_err_eq_c_2, RIGHT)
        pr_err_eq_c_4.next_to(pr_err_eq_c_3, RIGHT)
        pr_err_eq_c_group = Group(pr_err_eq_c, pr_err_eq_c_oop, pr_err_eq_c_2, pr_err_eq_c_3, pr_err_eq_c_4)

        self.play(Write(pr_err_eq_c), Write(pr_err_eq_c_4))
        pr_err_eq_c_2_copy = pr_err_eq_c_2.copy()
        pr_err_eq_c_2_copy.move_to(pr_err_eq_2)
        self.add(pr_err_eq_c_2_copy)
        self.play(Transform(pr_err_eq_c_2_copy, pr_err_eq_c_2))
        self.wait(0.5)
        pr_err_eq_3_copy = pr_err_eq_3.copy()
        pr_err_eq_3_copy.move_to(pr_err_eq_3)
        self.add(pr_err_eq_3_copy)
        self.play(Transform(pr_err_eq_3_copy, pr_err_eq_c_3))
        self.wait(2)
        pr_err_eq_c_oop_copy = pr_err_eq_oop.copy()
        pr_err_eq_c_oop_copy.move_to(pr_err_eq_oop)
        self.add(pr_err_eq_c_oop_copy)
        self.play(Transform(pr_err_eq_c_oop_copy, pr_err_eq_c_oop))
        self.wait(2)





