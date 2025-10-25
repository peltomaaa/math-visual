from manim import *
import numpy as np


class MandelbrotSetVisualization(Scene):
    """Beautiful Mandelbrot set with color gradients"""
    def construct(self):
        resolution = 60
        x_range = [-2.5, 1.0]
        y_range = [-1.25, 1.25]
        max_iter = 50

        dots = VGroup()

        for i in range(resolution):
            for j in range(resolution):
                # Map to complex plane
                x = x_range[0] + (x_range[1] - x_range[0]) * i / resolution
                y = y_range[0] + (y_range[1] - y_range[0]) * j / resolution

                c = complex(x, y)
                z = 0
                iteration = 0

                # Mandelbrot iteration
                for n in range(max_iter):
                    if abs(z) > 2:
                        iteration = n
                        break
                    z = z*z + c
                else:
                    iteration = max_iter

                # Color based on iterations
                if iteration < max_iter:
                    # Beautiful color gradient
                    t = iteration / max_iter
                    if t < 0.25:
                        color = interpolate_color(BLUE, TEAL, t * 4)
                    elif t < 0.5:
                        color = interpolate_color(TEAL, GREEN, (t - 0.25) * 4)
                    elif t < 0.75:
                        color = interpolate_color(GREEN, YELLOW, (t - 0.5) * 4)
                    else:
                        color = interpolate_color(YELLOW, RED, (t - 0.75) * 4)

                    # Map to screen coordinates
                    screen_x = (x + 0.75) * 3.2
                    screen_y = y * 4.5

                    dot = Dot(
                        point=np.array([screen_x, screen_y, 0]),
                        radius=0.055,
                        color=color,
                        fill_opacity=0.9
                    )
                    dots.add(dot)

        # Animate appearance
        self.play(FadeIn(dots, lag_ratio=0.0003), run_time=3)
        self.wait(1)

        # Zoom in on interesting region
        self.play(
            dots.animate.scale(1.8).shift(LEFT * 1.2 + DOWN * 0.3),
            run_time=2
        )
        self.wait(1)


class LorenzAttractorPath(Scene):
    """2D projection of the Lorenz attractor"""
    def construct(self):
        # Lorenz parameters
        sigma, rho, beta = 10, 28, 8/3
        dt = 0.008

        # Multiple starting points for richness
        paths = VGroup()
        colors = [BLUE, GREEN, YELLOW, RED, PURPLE]

        for idx, (start_x, color) in enumerate(zip([1, -1, 2, -2, 0.5], colors)):
            x, y, z = start_x, 1, 1
            points = []

            # Generate path points
            for i in range(3000):
                dx = sigma * (y - x)
                dy = x * (rho - z) - y
                dz = x * y - beta * z

                x += dx * dt
                y += dy * dt
                z += dz * dt

                # Project to 2D (use x and z)
                point = np.array([x * 0.08, z * 0.08 - 2, 0])
                points.append(point)

            # Create path
            path = VMobject(stroke_width=1.5, stroke_opacity=0.7)
            path.set_points_as_corners(points)
            path.set_color(color)
            paths.add(path)

        # Animate all paths
        self.play(
            *[Create(path, run_time=4) for path in paths],
            rate_func=linear
        )
        self.wait(1)


class FourierSeriesDrawing(Scene):
    """Fourier series epicycles drawing a shape"""
    def construct(self):
        # Create epicycle system
        num_circles = 7
        radii = [1.5, 0.8, 0.5, 0.3, 0.2, 0.15, 0.1]
        frequencies = [1, 2, 3, 4, 5, 7, 9]
        phases = [0, PI/4, PI/2, 0, PI/3, PI/6, 0]
        colors = [BLUE, GREEN, YELLOW, ORANGE, RED, PURPLE, PINK]

        # Create circles
        circles = VGroup()
        for r, color in zip(radii, colors):
            circle = Circle(radius=r, color=color, stroke_width=2)
            circles.add(circle)

        # Create dots
        dots = VGroup()
        for _ in range(num_circles):
            dot = Dot(color=WHITE, radius=0.06)
            dots.add(dot)

        # Path traced
        path = VMobject(color=YELLOW, stroke_width=3)
        path.set_points_as_corners([ORIGIN, ORIGIN])

        # Lines connecting
        lines = VGroup()
        for _ in range(num_circles - 1):
            line = Line(ORIGIN, ORIGIN, color=GREY, stroke_width=1, stroke_opacity=0.5)
            lines.add(line)

        # Add all objects
        self.add(circles, lines, dots, path)

        # Animation
        alpha_tracker = ValueTracker(0)

        def update_epicycles(mob):
            alpha = alpha_tracker.get_value()
            current_pos = np.array([-3, 0, 0])  # Start from left

            for i in range(num_circles):
                angle = alpha * frequencies[i] + phases[i]

                circles[i].move_to(current_pos)

                # Calculate point on circle
                offset = np.array([
                    radii[i] * np.cos(angle),
                    radii[i] * np.sin(angle),
                    0
                ])

                next_pos = current_pos + offset

                if i < num_circles - 1:
                    lines[i].put_start_and_end_on(current_pos, next_pos)

                dots[i].move_to(next_pos)
                current_pos = next_pos

            # Add to path
            path.add_points_as_corners([current_pos])

        epicycles = VGroup(circles, lines, dots)
        epicycles.add_updater(update_epicycles)

        self.play(
            alpha_tracker.animate.set_value(TAU * 2),
            run_time=6,
            rate_func=linear
        )

        epicycles.clear_updaters()
        self.wait(0.5)


class DoublePendulumChaos(Scene):
    """Three double pendulums showing chaos theory"""
    def construct(self):
        # Setup
        L1, L2 = 2.0, 1.6
        origin = UP * 2.8

        # Three pendulums with tiny differences
        theta1_vals = [PI/2, PI/2 + 0.05, PI/2 + 0.1]
        theta2_vals = [PI/2, PI/2, PI/2]
        colors = [BLUE, GREEN, YELLOW]

        # Create pendulums
        all_trails = []
        all_systems = []

        for theta1, theta2, color in zip(theta1_vals, theta2_vals, colors):
            # Initial positions
            p1 = origin + np.array([L1 * np.sin(theta1), -L1 * np.cos(theta1), 0])
            p2 = p1 + np.array([L2 * np.sin(theta2), -L2 * np.cos(theta2), 0])

            # Create visual elements
            rod1 = Line(origin, p1, color=WHITE, stroke_width=2, stroke_opacity=0.4)
            rod2 = Line(p1, p2, color=WHITE, stroke_width=2, stroke_opacity=0.4)
            bob = Dot(p2, color=color, radius=0.1)

            trail = TracedPath(
                bob.get_center,
                stroke_color=color,
                stroke_width=2.5,
                stroke_opacity=0.6
            )

            system = VGroup(rod1, rod2, bob)
            all_systems.append(system)
            all_trails.append(trail)

            self.add(system, trail)

        # Pivot
        pivot = Dot(origin, color=GREY, radius=0.1)
        self.add(pivot)

        # Physics simulation
        omega1_list = [0.0] * 3
        omega2_list = [0.0] * 3
        theta1_list = list(theta1_vals)
        theta2_list = list(theta2_vals)

        g = 9.8
        dt = 0.025

        for _ in range(200):
            for i in range(3):
                # Simple pendulum physics
                theta1_list[i] += omega1_list[i] * dt
                theta2_list[i] += omega2_list[i] * dt

                omega1_list[i] += (-g / L1) * np.sin(theta1_list[i]) * dt
                omega2_list[i] += (-g / L2) * np.sin(theta2_list[i]) * dt * 1.3

                # Update positions
                p1 = origin + np.array([
                    L1 * np.sin(theta1_list[i]),
                    -L1 * np.cos(theta1_list[i]),
                    0
                ])
                p2 = p1 + np.array([
                    L2 * np.sin(theta2_list[i]),
                    -L2 * np.cos(theta2_list[i]),
                    0
                ])

                system = all_systems[i]
                system[0].put_start_and_end_on(origin, p1)
                system[1].put_start_and_end_on(p1, p2)
                system[2].move_to(p2)

            self.wait(dt)

        self.wait(0.5)


class SortingVisualization(Scene):
    """Quick sort algorithm visualization"""
    def construct(self):
        # Create random bars
        np.random.seed(42)
        values = np.random.randint(1, 20, 15)

        bars = VGroup()
        max_height = 3
        bar_width = 0.4
        spacing = 0.5

        for i, val in enumerate(values):
            height = (val / 20) * max_height
            bar = Rectangle(
                width=bar_width,
                height=height,
                color=BLUE,
                fill_opacity=0.8,
                stroke_width=2
            )
            bar.shift(LEFT * 3.5 + RIGHT * i * spacing + UP * (height / 2 - 1.5))
            bars.add(bar)

        # Create bars
        self.play(Create(bars, lag_ratio=0.1), run_time=2)
        self.wait(0.5)

        # Bubble sort animation
        n = len(values)
        for i in range(n):
            for j in range(0, n - i - 1):
                # Highlight comparing bars
                self.play(
                    bars[j].animate.set_color(YELLOW),
                    bars[j + 1].animate.set_color(YELLOW),
                    run_time=0.15
                )

                # Swap if needed
                if values[j] > values[j + 1]:
                    # Swap values
                    values[j], values[j + 1] = values[j + 1], values[j]

                    # Swap visual positions
                    pos_j = bars[j].get_center()
                    pos_j1 = bars[j + 1].get_center()

                    self.play(
                        bars[j].animate.move_to(pos_j1),
                        bars[j + 1].animate.move_to(pos_j),
                        run_time=0.2
                    )

                    # Swap in VGroup
                    bars.submobjects[j], bars.submobjects[j + 1] = bars.submobjects[j + 1], bars.submobjects[j]

                # Reset colors
                self.play(
                    bars[j].animate.set_color(BLUE),
                    bars[j + 1].animate.set_color(BLUE if j + 1 < n - i - 1 else GREEN),
                    run_time=0.1
                )

            # Mark sorted
            bars[n - i - 1].set_color(GREEN)

        # All sorted
        self.play(bars.animate.set_color(GREEN), run_time=0.5)
        self.wait(1)


class CellularAutomata(Scene):
    """Conway's Game of Life"""
    def construct(self):
        grid_size = 30
        cell_size = 0.2

        # Initialize random grid
        np.random.seed(123)
        grid = np.random.choice([0, 1], size=(grid_size, grid_size), p=[0.7, 0.3])

        # Create cell squares
        cells = VGroup()
        for i in range(grid_size):
            for j in range(grid_size):
                cell = Square(
                    side_length=cell_size,
                    stroke_width=0.5,
                    stroke_opacity=0.3,
                    fill_opacity=0.9 if grid[i][j] else 0
                )
                cell.set_fill(BLUE if grid[i][j] else BLACK)
                cell.move_to(
                    np.array([
                        (j - grid_size/2) * cell_size,
                        (i - grid_size/2) * cell_size,
                        0
                    ])
                )
                cells.add(cell)

        self.add(cells)
        self.wait(0.5)

        # Simulate Game of Life
        for generation in range(30):
            new_grid = grid.copy()

            for i in range(grid_size):
                for j in range(grid_size):
                    # Count neighbors
                    neighbors = 0
                    for di in [-1, 0, 1]:
                        for dj in [-1, 0, 1]:
                            if di == 0 and dj == 0:
                                continue
                            ni, nj = (i + di) % grid_size, (j + dj) % grid_size
                            neighbors += grid[ni][nj]

                    # Game of Life rules
                    if grid[i][j] == 1:
                        if neighbors < 2 or neighbors > 3:
                            new_grid[i][j] = 0
                    else:
                        if neighbors == 3:
                            new_grid[i][j] = 1

            # Update cells
            animations = []
            for i in range(grid_size):
                for j in range(grid_size):
                    idx = i * grid_size + j
                    if new_grid[i][j] != grid[i][j]:
                        if new_grid[i][j]:
                            animations.append(cells[idx].animate.set_fill(BLUE, opacity=0.9))
                        else:
                            animations.append(cells[idx].animate.set_fill(BLACK, opacity=0))

            if animations:
                self.play(*animations, run_time=0.3)
            else:
                self.wait(0.3)

            grid = new_grid

        self.wait(1)
