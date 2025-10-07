from manim import *
import numpy as np


class FourierCircles(Scene):
    """Beautiful Fourier series visualization with epicycles"""
    def construct(self):
        # Create multiple rotating circles
        circles = VGroup()
        radii = [2, 1, 0.5, 0.25]
        colors = [BLUE, GREEN, YELLOW, RED]

        for i, (r, color) in enumerate(zip(radii, colors)):
            circle = Circle(radius=r, color=color, stroke_width=2)
            circles.add(circle)

        self.play(
            *[Create(c) for c in circles],
            run_time=2
        )

        # Rotate them with different speeds
        self.play(
            *[Rotate(circles[i], angle=2*PI*(i+1), run_time=4) for i in range(len(circles))],
        )

        self.wait(0.5)


class WaveInterference(Scene):
    """Two waves interfering with each other"""
    def construct(self):
        axes = Axes(
            x_range=[0, 4*PI, PI/2],
            y_range=[-2.5, 2.5, 1],
            x_length=10,
            y_length=6,
            axis_config={"color": BLUE_D, "stroke_width": 2}
        )

        # Create two sine waves
        wave1 = axes.plot(lambda x: np.sin(x), color=BLUE)
        wave2 = axes.plot(lambda x: np.sin(x + PI/3), color=GREEN)
        wave_sum = axes.plot(lambda x: np.sin(x) + np.sin(x + PI/3), color=YELLOW, stroke_width=4)

        # Animate
        self.play(Create(axes), run_time=1)
        self.play(Create(wave1), Create(wave2), run_time=2)
        self.wait(0.5)
        self.play(Transform(VGroup(wave1, wave2), wave_sum), run_time=2)
        self.wait(1)


class FibonacciSpiral(Scene):
    """Fibonacci spiral with golden ratio rectangles"""
    def construct(self):
        # Fibonacci numbers
        fibs = [1, 1, 2, 3, 5, 8]
        colors = [RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE]

        squares = VGroup()
        current_pos = ORIGIN
        direction = RIGHT

        for i, (fib, color) in enumerate(zip(fibs, colors)):
            square = Square(side_length=fib*0.3, color=color, fill_opacity=0.3, stroke_width=3)

            if i == 0:
                square.move_to(ORIGIN)
            else:
                # Position based on previous squares
                if i == 1:
                    square.next_to(squares[0], RIGHT, buff=0)
                elif i == 2:
                    square.next_to(squares[1], UP, buff=0, aligned_edge=RIGHT)
                elif i == 3:
                    square.next_to(squares[2], LEFT, buff=0, aligned_edge=UP)
                elif i == 4:
                    square.next_to(squares[3], DOWN, buff=0, aligned_edge=LEFT)
                elif i == 5:
                    square.next_to(squares[4], RIGHT, buff=0, aligned_edge=DOWN)

            squares.add(square)
            self.play(Create(square), run_time=0.8)

        # Create spiral arcs
        self.wait(0.5)

        # Scale everything to fit nicely
        self.play(squares.animate.scale(0.8).move_to(ORIGIN), run_time=1)
        self.wait(1)


class ParticleSystem(Scene):
    """Particle explosion effect"""
    def construct(self):
        # Create center point
        center = Dot(ORIGIN, color=WHITE, radius=0.1)
        self.add(center)

        # Create particles
        num_particles = 30
        particles = VGroup()

        for i in range(num_particles):
            angle = i * 2 * PI / num_particles
            particle = Dot(ORIGIN, color=interpolate_color(BLUE, RED, i/num_particles), radius=0.08)
            particles.add(particle)

        self.play(FadeIn(particles), run_time=0.5)

        # Explode outward
        animations = []
        for i, particle in enumerate(particles):
            angle = i * 2 * PI / num_particles
            direction = np.array([np.cos(angle), np.sin(angle), 0])
            target_pos = ORIGIN + direction * 3
            animations.append(particle.animate.move_to(target_pos))

        self.play(*animations, run_time=2, rate_func=rush_from)
        self.wait(0.5)

        # Fade out
        self.play(FadeOut(particles), FadeOut(center), run_time=1)


class GeometricTransformations(Scene):
    """Morphing geometric shapes"""
    def construct(self):
        # Create shapes
        triangle = RegularPolygon(n=3, color=RED, fill_opacity=0.5).scale(1.5)
        square = Square(color=GREEN, fill_opacity=0.5).scale(1.5)
        pentagon = RegularPolygon(n=5, color=BLUE, fill_opacity=0.5).scale(1.5)
        hexagon = RegularPolygon(n=6, color=PURPLE, fill_opacity=0.5).scale(1.5)
        circle = Circle(color=YELLOW, fill_opacity=0.5, radius=1.5)

        # Animate transformations
        self.play(Create(triangle), run_time=1)
        self.wait(0.3)
        self.play(Transform(triangle, square), run_time=1.2)
        self.wait(0.3)
        self.play(Transform(triangle, pentagon), run_time=1.2)
        self.wait(0.3)
        self.play(Transform(triangle, hexagon), run_time=1.2)
        self.wait(0.3)
        self.play(Transform(triangle, circle), run_time=1.2)
        self.wait(0.5)


class VectorField(Scene):
    """Flowing vector field visualization"""
    def construct(self):
        # Create vector field
        plane = NumberPlane(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
                "stroke_opacity": 0.3
            }
        )

        # Define vector function (circular flow)
        def vector_func(pos):
            x, y = pos[0], pos[1]
            return np.array([-y, x, 0]) * 0.3

        # Create arrows
        vectors = VGroup()
        for x in np.arange(-3, 3.5, 0.7):
            for y in np.arange(-3, 3.5, 0.7):
                point = np.array([x, y, 0])
                direction = vector_func(point)
                if np.linalg.norm(direction) > 0:
                    arrow = Arrow(
                        point,
                        point + direction,
                        color=interpolate_color(BLUE, RED, np.linalg.norm(direction)),
                        buff=0,
                        stroke_width=2,
                        max_tip_length_to_length_ratio=0.3
                    )
                    vectors.add(arrow)

        self.play(Create(plane), run_time=1)
        self.play(Create(vectors), run_time=2, lag_ratio=0.01)
        self.wait(1)


class SineWavePulse(Scene):
    """Animated sine wave pulse"""
    def construct(self):
        axes = Axes(
            x_range=[0, 4*PI, PI],
            y_range=[-1.5, 1.5, 0.5],
            x_length=11,
            y_length=6,
            axis_config={"color": GREY}
        )

        # Create animated sine wave
        sine_wave = always_redraw(
            lambda: axes.plot(
                lambda x: np.sin(x - self.time * 2),
                color=BLUE,
                stroke_width=4
            )
        )

        self.time = 0
        self.play(Create(axes), run_time=1)
        self.add(sine_wave)

        # Animate time
        self.play(
            UpdateFromFunc(self, lambda m, dt: setattr(self, 'time', self.time + dt)),
            run_time=4,
            rate_func=linear
        )
        self.wait(0.5)


class MatrixTransformation(Scene):
    """2D matrix transformation visualization"""
    def construct(self):
        # Create grid
        grid = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 1,
            }
        )

        # Create a shape to transform
        shape = VGroup(
            Square(side_length=2, color=YELLOW, fill_opacity=0.5),
            Dot(color=RED)
        )

        self.play(Create(grid), run_time=1)
        self.play(Create(shape), run_time=1)
        self.wait(0.5)

        # Apply rotation and scaling
        self.play(
            grid.animate.apply_matrix([[1.5, 0.5], [0.5, 1.5]]),
            shape.animate.apply_matrix([[1.5, 0.5], [0.5, 1.5]]),
            run_time=3
        )
        self.wait(1)
