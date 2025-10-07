from manim import *


class SquareToCircle(Scene):
    def construct(self):
        # Create a square
        square = Square(color=BLUE, fill_opacity=0.5)

        # Create a circle
        circle = Circle(color=RED, fill_opacity=0.5)

        # Animate transforming square to circle
        self.play(Create(square))
        self.wait(1)
        self.play(Transform(square, circle))
        self.wait(1)
