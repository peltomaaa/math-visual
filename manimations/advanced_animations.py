from manim import *
import numpy as np


class ComplexFourierEpicycles(Scene):
    """Advanced Fourier epicycles with multiple rotating circles"""
    def construct(self):
        # Create epicycle system
        radii = [1.8, 1.0, 0.5, 0.25, 0.12]
        speeds = [1, -2, 3, -5, 8]  # Mix of clockwise and counter-clockwise
        colors = [BLUE, GREEN, YELLOW, ORANGE, RED]

        circles = VGroup()
        for r, color in zip(radii, colors):
            circle = Circle(radius=r, color=color, stroke_width=2.5)
            circles.add(circle)

        dots = VGroup()
        for _ in range(len(radii)):
            dot = Dot(color=WHITE, radius=0.08)
            dots.add(dot)

        # Show initial circles
        self.play(Create(circles[0]), run_time=0.8)

        # Animate nested rotations
        for i in range(len(circles)):
            if i > 0:
                self.play(Create(circles[i]), run_time=0.5)

        # Complex rotation pattern
        self.play(
            *[Rotate(circles[i], angle=TAU * speeds[i] * 0.5, about_point=ORIGIN if i == 0 else circles[i-1].get_center())
              for i in range(len(circles))],
            run_time=4
        )

        self.wait(0.5)


class FluidParticles(Scene):
    """Advanced particle system with wave propagation"""
    def construct(self):
        # Create particle grid
        num_particles_x = 25
        num_particles_y = 15
        particles = VGroup()

        for i in range(num_particles_x):
            for j in range(num_particles_y):
                x = (i - num_particles_x/2) * 0.35
                y = (j - num_particles_y/2) * 0.35

                particle = Dot(
                    point=np.array([x, y, 0]),
                    radius=0.05,
                    color=interpolate_color(BLUE, PURPLE, i/num_particles_x)
                )
                particles.add(particle)

        self.play(FadeIn(particles, lag_ratio=0.002), run_time=1.5)

        # Create wave effect
        animations = []
        for particle in particles:
            pos = particle.get_center()
            x, y = pos[0], pos[1]

            # Wave displacement
            wave_offset = UP * 0.5 * np.sin(x * 1.5) * np.cos(y * 1.5)
            new_pos = pos + wave_offset

            animations.append(particle.animate.move_to(new_pos))

        self.play(*animations, run_time=2, rate_func=there_and_back)

        # Spiral out effect
        animations = []
        for particle in particles:
            pos = particle.get_center()
            x, y = pos[0], pos[1]
            angle = np.arctan2(y, x)
            distance = np.sqrt(x**2 + y**2)

            new_distance = distance * 1.5
            new_pos = np.array([
                new_distance * np.cos(angle + 0.5),
                new_distance * np.sin(angle + 0.5),
                0
            ])

            animations.append(particle.animate.move_to(new_pos).set_opacity(0.3))

        self.play(*animations, run_time=2)
        self.play(FadeOut(particles), run_time=1)


class FractalTree(Scene):
    """Beautiful fractal tree generation"""
    def construct(self):
        def create_branch(start, angle, length, depth, max_depth=6):
            if depth > max_depth or length < 0.1:
                return VGroup()

            # Calculate end point
            end = start + np.array([
                length * np.cos(angle),
                length * np.sin(angle),
                0
            ])

            # Color based on depth
            color = interpolate_color(
                rgb_to_color([0.6, 0.3, 0.1]),  # Brown
                GREEN,
                depth / max_depth
            )

            # Create branch line
            branch = Line(
                start, end,
                color=color,
                stroke_width=max(8 - depth, 1)
            )

            # Recursively create child branches
            branches = VGroup(branch)
            if depth < max_depth:
                # Left branch
                left_branches = create_branch(
                    end, angle + PI/6, length * 0.7, depth + 1, max_depth
                )
                # Right branch
                right_branches = create_branch(
                    end, angle - PI/6, length * 0.7, depth + 1, max_depth
                )
                branches.add(left_branches, right_branches)

            return branches

        # Create tree
        tree = create_branch(
            start=DOWN * 3,
            angle=PI/2,
            length=2,
            depth=0,
            max_depth=6
        )

        # Animate tree growth
        self.play(Create(tree, lag_ratio=0.05), run_time=5)
        self.wait(1)


class DoublePendulumChaos(Scene):
    """Chaotic double pendulum with trail"""
    def construct(self):
        # Pendulum setup
        L1, L2 = 2.0, 1.8
        origin = UP * 2.5

        # Initial angles
        theta1_vals = [PI/2 + 0.1 * i for i in range(3)]
        theta2 = PI/2

        # Create multiple pendulums with slightly different starting positions
        pendulum_systems = VGroup()
        colors = [BLUE, GREEN, YELLOW]

        for theta1, color in zip(theta1_vals, colors):
            # Calculate initial positions
            p1 = origin + np.array([L1 * np.sin(theta1), -L1 * np.cos(theta1), 0])
            p2 = p1 + np.array([L2 * np.sin(theta2), -L2 * np.cos(theta2), 0])

            # Create pendulum parts
            rod1 = Line(origin, p1, color=WHITE, stroke_width=2, stroke_opacity=0.5)
            rod2 = Line(p1, p2, color=WHITE, stroke_width=2, stroke_opacity=0.5)
            bob = Dot(p2, color=color, radius=0.12)

            trail = TracedPath(bob.get_center, stroke_color=color, stroke_width=2, stroke_opacity=0.7)

            system = VGroup(rod1, rod2, bob)
            pendulum_systems.add(system)
            self.add(system, trail)

        # Pivot point
        pivot = Dot(origin, color=GREY, radius=0.12)
        self.add(pivot)

        # Animate with physics simulation
        omega1_vals = [0] * 3
        omega2_vals = [0] * 3
        theta1_current = list(theta1_vals)
        theta2_current = [theta2] * 3

        dt = 0.03
        for frame in range(180):
            for i in range(3):
                # Simplified pendulum physics
                g = 9.8
                m1 = m2 = 1

                # Simplified equations
                theta1_current[i] += omega1_vals[i] * dt
                theta2_current[i] += omega2_vals[i] * dt

                omega1_vals[i] += (-g / L1) * np.sin(theta1_current[i]) * dt
                omega2_vals[i] += (-g / L2) * np.sin(theta2_current[i]) * dt * 1.5

                # Update positions
                p1 = origin + np.array([
                    L1 * np.sin(theta1_current[i]),
                    -L1 * np.cos(theta1_current[i]),
                    0
                ])
                p2 = p1 + np.array([
                    L2 * np.sin(theta2_current[i]),
                    -L2 * np.cos(theta2_current[i]),
                    0
                ])

                system = pendulum_systems[i]
                system[0].put_start_and_end_on(origin, p1)
                system[1].put_start_and_end_on(p1, p2)
                system[2].move_to(p2)

            self.wait(dt)


class LissajousCurves(Scene):
    """Beautiful Lissajous curves"""
    def construct(self):
        axes = Axes(
            x_range=[-1.5, 1.5, 0.5],
            y_range=[-1.5, 1.5, 0.5],
            x_length=8,
            y_length=8,
            axis_config={"stroke_opacity": 0.3}
        )

        self.play(Create(axes), run_time=1)

        # Parameters for different curves
        params = [(3, 2), (5, 4), (4, 3)]
        colors = [BLUE, GREEN, YELLOW]

        for (a, b), color in zip(params, colors):
            curve = ParametricFunction(
                lambda t: axes.c2p(
                    np.sin(a * t),
                    np.sin(b * t)
                ),
                t_range=[0, TAU],
                color=color,
                stroke_width=3
            )

            # Dot tracing the curve
            dot = Dot(color=color, radius=0.1)

            self.play(
                Create(curve),
                MoveAlongPath(dot, curve),
                run_time=4,
                rate_func=linear
            )
            self.remove(dot)

        self.wait(1)


class MandelBrotSet(Scene):
    """Simplified Mandelbrot set visualization"""
    def construct(self):
        resolution = 50
        x_range = [-2.5, 1]
        y_range = [-1.25, 1.25]
        max_iter = 30

        dots = VGroup()

        for i in range(resolution):
            for j in range(resolution):
                # Map to complex plane
                x = x_range[0] + (x_range[1] - x_range[0]) * i / resolution
                y = y_range[0] + (y_range[1] - y_range[0]) * j / resolution

                c = complex(x, y)
                z = 0

                # Mandelbrot iteration
                for n in range(max_iter):
                    if abs(z) > 2:
                        break
                    z = z*z + c

                # Color based on iterations
                if n < max_iter - 1:
                    color = interpolate_color(BLUE, RED, n / max_iter)

                    # Map to screen coordinates
                    screen_x = (x + 0.75) * 3.5
                    screen_y = y * 4

                    dot = Dot(
                        point=np.array([screen_x, screen_y, 0]),
                        radius=0.06,
                        color=color,
                        fill_opacity=0.8
                    )
                    dots.add(dot)

        self.play(FadeIn(dots, lag_ratio=0.0005), run_time=3)
        self.play(dots.animate.scale(1.5).shift(LEFT * 0.5), run_time=2)
        self.wait(1)
