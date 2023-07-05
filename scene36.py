from manim import *

class Scene36(Scene):
    def construct(self):

        # But now, we ask ourselves, what is the probability of this occurring? 
        # What is the probability that Bob makes an incorrect conclusion given that 
        # the passwords are different? To answer this, we must compute the probability 
        # A mod p = B mod p given that A != B.


        text_question = Text("Question", color=GOLD, font_size=100)
        self.play(Write(text_question))
        self.wait(1)
        self.play(FadeOut(text_question))

        text_q1 = Text("What is the probability of this occurring?").scale(0.8)
        text_q2 = Text("What is the probability that Bob makes an").scale(0.8)
        text_q3 = Text("incorrect conclusion", color=RED).scale(0.8)
        text_q4 = Text("given").scale(0.8)
        text_q5 = Text("that the passwords are different?", color=GREEN).scale(0.8)
        text_q1.move_to(UP*2)
        # text_q2.next_to(text_q1, DOWN)
        text_q4.next_to(text_q3, RIGHT)
        text_q5.next_to(text_q4, RIGHT)
        # group q3, q4, and q5
        group_q3 = Group(text_q3, text_q4, text_q5)
        group_q3.move_to(LEFT*0.01)
        text_q2.move_to(UP)
        self.play(Write(text_q1))
        self.wait(1)
        self.play(Write(text_q2))
        self.play(FadeIn(group_q3))
        self.wait(2)

        text_pr = MathTex(r"\Pr[")
        text_pr.move_to(DOWN*2+LEFT*4)
        text_pr_part_1 = MathTex(r"a \bmod p = b \bmod p", color=RED)
        text_pr_part_2 = MathTex(r"\mid")
        text_pr_part_3 = MathTex(r"a \neq b", color=GREEN)
        text_pr_part_4 = MathTex(r"]")
        text_pr_part_1.next_to(text_pr, RIGHT)
        text_pr_part_2.next_to(text_pr_part_1, RIGHT)
        text_pr_part_3.next_to(text_pr_part_2, RIGHT)
        text_pr_part_4.next_to(text_pr_part_3, RIGHT)

        
        self.play(Write(text_pr))
        # animate text_q3 moving to location of text_pr_part_1 but text_pr_part_1 appears
        text_q3_copy = text_q3.copy()
        text_q3_copy.move_to(text_q3.get_center())
        self.add(text_q3_copy)
        # self.play(text_q3_copy.animate.move_to(text_pr_part_1.get_center()))
        self.play(Transform(text_q3_copy, text_pr_part_1))
        self.wait(1)
        text_q4_copy = text_q4.copy()
        text_q4_copy.move_to(text_q4.get_center())
        self.add(text_q4_copy)
        self.play(Transform(text_q4_copy, text_pr_part_2))
        self.wait(1)
        text_q5_copy = text_q5.copy()
        text_q5_copy.move_to(text_q5.get_center())
        self.add(text_q5_copy)
        self.play(Transform(text_q5_copy, text_pr_part_3))
        self.wait(0.2)
        self.play(Write(text_pr_part_4))
        self.wait(2)

