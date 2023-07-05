from manim import *

class Scene42(Scene):
    def construct(self):
        header = Text("Prime Number Theorem").scale(1.5)
        header.shift(UP*3)
        self.play(Write(header))
        self.wait(1)

        jacques = ImageMobject("pics/jacques.jpg")
        charles = ImageMobject("pics/charles.jpg")
        riemann = ImageMobject("pics/riemann.webp")
        # make the images the same height
        jacques.scale(1)
        charles.scale(2.2)
        riemann.scale(0.27)
        jacques.shift(LEFT*5)
        riemann.shift(RIGHT*5)

        jacques_caption = Text("Jacques Hadamard").scale(0.5)
        charles_caption = Text("Charles de la Vallée Poussin").scale(0.5)
        riemann_caption = Text("Bernhard Riemann").scale(0.5)
        jacques_caption.next_to(jacques, DOWN)
        charles_caption.next_to(charles, DOWN)
        riemann_caption.next_to(riemann, DOWN)
        self.play(
            FadeIn(jacques),
            FadeIn(charles),
            FadeIn(riemann),
            Write(jacques_caption),
            Write(charles_caption),
            Write(riemann_caption)

        )
        self.wait(1)

        # the number of primes <= N for some integer N is roughly N / log N.
        thm = MathTex(r"\text{For } N \in \mathbb{Z^+}}, \text{ the number of primes } \leq N \
                        \text{ is roughly } \frac{N}{\log N}", color=YELLOW).scale(0.8)
        thm.shift(DOWN*3)
        self.play(Write(thm), run_time=4)
        self.wait(2)
        self.play(
            FadeOut(jacques),
            FadeOut(charles),
            FadeOut(riemann),
            FadeOut(jacques_caption),
            FadeOut(charles_caption),
            FadeOut(riemann_caption),
        )
        self.wait(0.5)
        self.play(
            thm.animate.shift(UP*5)
        )
        self.wait(0.5)
        conc = MathTex(r"\text{Number of primes in } [2..n^3]  \
                       \text{ is roughly } &=\frac{n^3}{\log n^3} \\ \
                       &= \frac{n^3}{3 \log n}")
        conc.shift(DOWN)
        self.play(Write(conc))
        self.wait(2)