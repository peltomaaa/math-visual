from manim import *
import numpy as np


class FourierEpicyclesAnimated(Scene):
    """Fourier epicycles with actual drawing animation"""
    def construct(self):
        # Parameters
        num_circles = 6
        radii = [1.2, 0.7, 0.4, 0.25, 0.15, 0.1]
        frequencies = [1, 3, 5, 7, 9, 11]
        colors = [BLUE, TEAL, GREEN, YELLOW, ORANGE, RED]

        # Create circles
        circles = VGroup()
        for r, color in zip(radii, colors):
            circle = Circle(radius=r, color=color, stroke_width=2.5, stroke_opacity=0.6)
            circles.add(circle)

        # Create dots at endpoints
        dots = VGroup()
        for color in colors:
            dot = Dot(color=color, radius=0.07)
            dots.add(dot)

        # Lines connecting centers
        lines = VGroup()
        for _ in range(num_circles):
            line = Line(ORIGIN, ORIGIN, color=GREY, stroke_width=1.5, stroke_opacity=0.4)
            lines.add(line)

        # Path being drawn
        path = VMobject(color=YELLOW, stroke_width=3)
        path.set_points_as_corners([ORIGIN, ORIGIN])

        # Add everything
        self.add(circles, lines, dots)

        # Animate
        t = ValueTracker(0)

        def update_system(mob):
            time = t.get_value()
            current_center = np.array([-3.5, 0, 0])

            for i in range(num_circles):
                angle = time * frequencies[i]

                # Update circle position
                circles[i].move_to(current_center)

                # Calculate endpoint of this circle
                endpoint = current_center + np.array([
                    radii[i] * np.cos(angle),
                    radii[i] * np.sin(angle),
                    0
                ])

                # Update line
                if i < num_circles - 1:
                    lines[i].put_start_and_end_on(current_center, endpoint)

                # Update dot
                dots[i].move_to(endpoint)

                # Move to next center
                current_center = endpoint

            # Add final point to path
            if path.get_num_points() > 0:
                path.add_points_as_corners([endpoint])

        system = VGroup(circles, lines, dots)
        system.add_updater(update_system)
        self.add(path)

        # Animate over time
        self.play(
            t.animate.set_value(TAU * 2),
            run_time=6,
            rate_func=linear
        )

        system.clear_updaters()
        self.wait(0.5)


class MandelbrotZoomSpectacular(Scene):
    """More visually striking Mandelbrot with zoom animation"""
    def construct(self):
        # Higher resolution for better quality
        resolution = 70
        x_range = [-2.5, 1.0]
        y_range = [-1.25, 1.25]
        max_iter = 60

        dots = VGroup()

        for i in range(resolution):
            for j in range(resolution):
                x = x_range[0] + (x_range[1] - x_range[0]) * i / resolution
                y = y_range[0] + (y_range[1] - y_range[0]) * j / resolution

                c = complex(x, y)
                z = 0
                iteration = 0

                for n in range(max_iter):
                    if abs(z) > 2:
                        iteration = n
                        break
                    z = z*z + c
                else:
                    iteration = max_iter

                # Enhanced color scheme
                if iteration < max_iter:
                    t = iteration / max_iter

                    # Multi-color gradient
                    if t < 0.16:
                        color = interpolate_color(BLACK, PURPLE, t * 6)
                    elif t < 0.33:
                        color = interpolate_color(PURPLE, BLUE, (t - 0.16) * 6)
                    elif t < 0.5:
                        color = interpolate_color(BLUE, TEAL, (t - 0.33) * 6)
                    elif t < 0.66:
                        color = interpolate_color(TEAL, GREEN, (t - 0.5) * 6)
                    elif t < 0.83:
                        color = interpolate_color(GREEN, YELLOW, (t - 0.66) * 6)
                    else:
                        color = interpolate_color(YELLOW, RED, (t - 0.83) * 6)

                    # Map to screen
                    screen_x = (x + 0.75) * 3.2
                    screen_y = y * 4.5

                    dot = Dot(
                        point=np.array([screen_x, screen_y, 0]),
                        radius=0.05,
                        color=color,
                        fill_opacity=0.95
                    )
                    dots.add(dot)

        # Fade in with cascade effect
        self.play(FadeIn(dots, lag_ratio=0.0002), run_time=2)
        self.wait(0.5)

        # Zoom into interesting region with rotation
        self.play(
            dots.animate.scale(2.2).shift(LEFT * 1.5 + DOWN * 0.2).rotate(0.1),
            run_time=2.5,
            rate_func=smooth
        )
        self.wait(0.5)

        # Zoom back out
        self.play(
            dots.animate.scale(1/2.2).shift(RIGHT * 1.5 + UP * 0.2).rotate(-0.1),
            run_time=1.5
        )
        self.wait(0.5)


class VectorFieldFlowEnhanced(Scene):
    """Beautiful flowing vector field with streamlines"""
    def construct(self):
        # Create refined grid
        plane = NumberPlane(
            x_range=[-5, 5, 1],
            y_range=[-4, 4, 1],
            background_line_style={
                "stroke_color": BLUE_E,
                "stroke_width": 0.5,
                "stroke_opacity": 0.2
            }
        )

        # Vector function - vortex
        def vector_func(pos):
            x, y = pos[0], pos[1]
            # Circular vortex flow
            return np.array([-y, x, 0]) * 0.25

        # Create vector field with better spacing
        vectors = VGroup()
        for x in np.arange(-4.5, 4.6, 0.6):
            for y in np.arange(-3.5, 3.6, 0.6):
                point = np.array([x, y, 0])
                direction = vector_func(point)

                if np.linalg.norm(direction) > 0.01:
                    # Color based on magnitude
                    magnitude = np.linalg.norm(direction)
                    color = interpolate_color(BLUE, RED, min(magnitude * 2, 1))

                    arrow = Arrow(
                        point,
                        point + direction,
                        color=color,
                        buff=0,
                        stroke_width=3,
                        max_tip_length_to_length_ratio=0.35,
                        max_stroke_width_to_length_ratio=5
                    )
                    vectors.add(arrow)

        # Create flowing particles
        num_particles = 12
        particles = VGroup()
        particle_paths = []

        for i in range(num_particles):
            angle = i * TAU / num_particles
            radius = 2.5
            start_pos = np.array([radius * np.cos(angle), radius * np.sin(angle), 0])

            particle = Dot(start_pos, color=YELLOW, radius=0.08)
            particles.add(particle)

            # Create traced path
            path = TracedPath(particle.get_center, stroke_color=YELLOW, stroke_width=2, stroke_opacity=0.4)
            particle_paths.append(path)

        # Animate
        self.play(Create(plane), run_time=0.8)
        self.play(Create(vectors, lag_ratio=0.005), run_time=2)

        # Add particles and their paths
        self.add(particles, *particle_paths)

        # Animate particles flowing
        def update_particle(particle, dt):
            pos = particle.get_center()
            velocity = vector_func(pos)
            new_pos = pos + velocity * dt * 10
            particle.move_to(new_pos)

        for particle in particles:
            particle.add_updater(update_particle)

        self.wait(3)

        for particle in particles:
            particle.clear_updaters()

        self.wait(0.5)


class FractalTreeEnhanced(Scene):
    """Even more beautiful fractal tree with gradient colors"""
    def construct(self):
        def create_branch(start, angle, length, depth, max_depth=7):
            if depth > max_depth or length < 0.08:
                return VGroup()

            # Calculate end point
            end = start + np.array([
                length * np.cos(angle),
                length * np.sin(angle),
                0
            ])

            # Gradient from brown to green based on depth
            t = depth / max_depth
            if t < 0.4:
                color = interpolate_color(rgb_to_color([0.4, 0.2, 0.1]), rgb_to_color([0.5, 0.3, 0.15]), t * 2.5)
            elif t < 0.7:
                color = interpolate_color(rgb_to_color([0.5, 0.3, 0.15]), rgb_to_color([0.3, 0.5, 0.2]), (t - 0.4) * 3.3)
            else:
                color = interpolate_color(rgb_to_color([0.3, 0.5, 0.2]), GREEN, (t - 0.7) * 3.3)

            # Create branch
            branch = Line(
                start, end,
                color=color,
                stroke_width=max(10 - depth * 1.3, 0.8)
            )

            # Recursively create child branches
            branches = VGroup(branch)
            if depth < max_depth:
                # Three branches for more density
                left_branches = create_branch(end, angle + PI/5, length * 0.65, depth + 1, max_depth)
                right_branches = create_branch(end, angle - PI/5, length * 0.68, depth + 1, max_depth)
                middle_branches = create_branch(end, angle + PI/20, length * 0.6, depth + 1, max_depth)

                branches.add(left_branches, right_branches, middle_branches)

            return branches

        # Create tree
        tree = create_branch(
            start=DOWN * 3.2,
            angle=PI/2,
            length=2.2,
            depth=0,
            max_depth=7
        )

        # Animate growth
        self.play(Create(tree, lag_ratio=0.03), run_time=5)
        self.wait(0.5)

        # Gentle sway
        self.play(
            tree.animate.rotate(0.05, about_point=DOWN * 3.2),
            rate_func=there_and_back,
            run_time=1.5
        )
        self.wait(0.5)
