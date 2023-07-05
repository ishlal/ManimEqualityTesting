from manim import *

class Scene38(Scene):
    def construct(self):
        proof_p1 = MathTex(r"a \bmod p = k \implies a = pq + k\; q \in \mathbb{Z}")
        proof_p2 = MathTex(r"a \bmod p = b \bmod p \implies b \bmod p = k")
        proof_p3 = MathTex(r"\implies b = p\ell + k \; \ell \in \mathbb{Z}")
        proof_p4 = MathTex(r"|A - B| \bmod p = |pq + k - (p\ell + k)| \bmod p")
        proof_p5 = MathTex(r"= |pq - pl| \bmod p")
        proof_p6 = MathTex(r"= |p(q - \ell)| \bmod p")
        proof_p7 = MathTex(r"\boxed{= 0}")

        proof_p8 = MathTex(r"\therefore a \bmod p = b \bmod p \implies |A - B| \bmod p = C \bmod p = 0", color=YELLOW)

        proof_p1.shift(UP*2)
        proof_p2.next_to(proof_p1, DOWN)
        proof_p3.next_to(proof_p2, DOWN)
        proof_p4.next_to(proof_p3, DOWN)
        proof_p5.next_to(proof_p4, DOWN)
        proof_p6.next_to(proof_p5, DOWN)
        proof_p7.next_to(proof_p6, DOWN)
        proof_p8.next_to(proof_p7, DOWN)

        group_anim = AnimationGroup(
            Write(proof_p1),
            Write(proof_p2),
            Write(proof_p3),
            Write(proof_p4),
            Write(proof_p5),
            Write(proof_p6),
            Write(proof_p7),
            Write(proof_p8),
            run_time=2
        )
        # self.play(group_anim)
        # self.wait(2)
        # self.play(
        #     FadeOut(proof_p1),
        #     FadeOut(proof_p2),
        #     FadeOut(proof_p3),
        #     FadeOut(proof_p4),
        #     FadeOut(proof_p5),
        #     FadeOut(proof_p6),
        #     FadeOut(proof_p7),
        #     FadeOut(proof_p8)
        # )

        long_proof = MathTex(
            r" \
            a \bmod p = k &\implies a = pq + k, \text{for } q \in \mathbb{Z} \\ \
                a\bmod p = b \bmod p &\implies b \bmod p = k\\ \
                &\implies b = p\ell + k, \text{for }\ell \in \mathbb{Z} \\ \
                |A - B| \bmod p &= |pq + k - (p\ell + k)| \bmod p \\ \
                &= |pq - pl| \bmod p \\ \
                &= |p(q - \ell)| \bmod p \\ \
                &\boxed{=0} \\ \
            "
        )
        self.play(Write(long_proof))
        self.play(Write(proof_p8))
        self.wait(2)
        self.play(FadeOut(long_proof), FadeOut(proof_p8))