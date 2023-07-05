from manim import *

class Scene39(Scene):
    def construct(self):
        goal_pr = MathTex(r"\Pr[")
        goal_pr_2 = MathTex(r"C \bmod p = 0", color=RED)
        goal_pr_3 = MathTex(r"\mid")
        goal_pr_4 = MathTex(r"C \neq 0", color=GREEN)
        goal_pr_5 = MathTex(r"]")

        goal_pr_2.next_to(goal_pr, RIGHT)
        goal_pr_3.next_to(goal_pr_2, RIGHT)
        goal_pr_4.next_to(goal_pr_3, RIGHT)
        goal_pr_5.next_to(goal_pr_4, RIGHT)

        group_pr = Group(
            goal_pr, 
            goal_pr_2, 
            goal_pr_3,
            goal_pr_4,
            goal_pr_5
        )

        group_pr.shift(UP*2 + LEFT*4)
        group_write = AnimationGroup(
            Write(goal_pr),
            Write(goal_pr_2),
            Write(goal_pr_3),
            Write(goal_pr_4),
            Write(goal_pr_5),
            lag_ratio=0.5,
            run_time=2
        )
        self.play(group_write)
        self.wait(1)

        goal_pr_2_copy = goal_pr_2.copy()
        goal_pr_2_copy.move_to(goal_pr_2.get_center())
        goal_pr_2_copy.set_color(RED)
        self.play(goal_pr_2_copy.animate.move_to(goal_pr_2_copy.get_center() + DOWN + LEFT))
        
        text_impl = MathTex(r"\implies")
        text_impl_2 = MathTex(r"p \mid C", color=RED)
        text_impl.next_to(goal_pr_2_copy, RIGHT)
        text_impl_2.next_to(text_impl, RIGHT)
        self.play(Write(text_impl))
        self.play(Write(text_impl_2))
        self.wait(1)

        text_impl_2_copy = text_impl_2.copy()
        text_impl_2_copy.move_to(text_impl_2.get_center())
        text_impl_2_copy.set_color(RED)
        self.play(text_impl_2_copy.animate.move_to(goal_pr_2.get_center()),
                  FadeOut(goal_pr_2),
                  FadeOut(goal_pr_2_copy),
                  FadeOut(text_impl),
                  FadeOut(text_impl_2))
        self.wait(2)

        text_rewrite = MathTex(r"p \text{ is a divisor of } C", color=RED).scale(0.8)
        text_rewrite.move_to(goal_pr_2.get_center())
        self.play(Transform(text_impl_2_copy, text_rewrite))
        self.wait(2)

        goal_pr_4_copy = goal_pr_4.copy()
        goal_pr_4_copy.move_to(goal_pr_4.get_center())
        goal_pr_4_copy.set_color(GREEN)
        self.play(goal_pr_4_copy.animate.move_to(goal_pr_4_copy.get_center() + DOWN + LEFT*2))

        text_impl_3 = MathTex(r"\implies")
        text_impl_4 = MathTex(r"C \in \mathbb{Z^+}", color=GREEN)
        text_impl_3.next_to(goal_pr_4_copy, RIGHT)
        text_impl_4.next_to(text_impl_3, RIGHT)
        self.play(Write(text_impl_3))
        self.play(Write(text_impl_4))
        self.wait(1)

        text_impl_4_copy = text_impl_4.copy()
        text_impl_4_copy.move_to(text_impl_4.get_center())
        text_impl_4_copy.set_color(GREEN)
        self.play(text_impl_4_copy.animate.move_to(goal_pr_4.get_center()),
                    FadeOut(goal_pr_4),
                    FadeOut(goal_pr_4_copy),
                    FadeOut(text_impl_3),
                    FadeOut(text_impl_4))
        


        clean_text_1 = MathTex(r"\Pr[")
        clean_text_2 = MathTex(r"p \text{ is a divisor of } C", color=RED)
        clean_text_3 = MathTex(r"\mid")
        clean_text_4 = MathTex(r"C \in \mathbb{Z^+}", color=GREEN)
        clean_text_5 = MathTex(r"]")
        clean_text_2.next_to(clean_text_1, RIGHT)
        clean_text_3.next_to(clean_text_2, RIGHT)
        clean_text_4.next_to(clean_text_3, RIGHT)
        clean_text_5.next_to(clean_text_4, RIGHT)
        group_clean = Group(
            clean_text_1,
            clean_text_2,
            clean_text_3,
            clean_text_4,
            clean_text_5
        )
        group_clean.shift(UP*2 + LEFT*4)
        group_existing = Group(
            text_impl_2_copy,
            text_impl_4_copy,
            goal_pr_5,
            goal_pr_3,
            goal_pr
        )
        self.play(Transform(group_existing, group_clean))
        self.wait(2)

        frac = MathTex(r"= \frac{\text{Number of prime divisors of }C}{\text{Number of choices of } p}")
        self.play(Write(frac))
        self.wait(2)

        