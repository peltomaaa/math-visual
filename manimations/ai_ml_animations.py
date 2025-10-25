from manim import *
import numpy as np


class AttentionMechanism(Scene):
    """
    Transformer Attention Mechanism Visualization
    Shows how attention weights connect tokens with beautiful heatmap
    """
    def construct(self):
        # Title that fades out
        title = Text("Self-Attention Mechanism", font_size=36, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        # Input tokens
        tokens = ["The", "cat", "sat", "on", "mat"]
        token_labels = VGroup(*[
            Text(token, font_size=24, color=WHITE)
            for token in tokens
        ]).arrange(RIGHT, buff=0.8).shift(UP * 2.5)

        # Create attention matrix (5x5)
        # Simulate realistic attention patterns
        attention_weights = np.array([
            [0.7, 0.1, 0.05, 0.05, 0.1],   # "The" attends mostly to itself and "cat"
            [0.15, 0.6, 0.15, 0.05, 0.05],  # "cat" attends to itself and neighbors
            [0.1, 0.2, 0.5, 0.15, 0.05],    # "sat" attends to "cat" and itself
            [0.05, 0.05, 0.15, 0.6, 0.15],  # "on" attends to neighbors
            [0.1, 0.05, 0.05, 0.15, 0.65]   # "mat" attends mostly to itself
        ])

        # Create heatmap squares
        square_size = 0.65
        heatmap = VGroup()
        
        for i in range(5):
            for j in range(5):
                weight = attention_weights[i][j]
                
                # Color gradient from dark blue (low) to bright yellow (high)
                if weight < 0.2:
                    color = interpolate_color(BLUE_E, BLUE_D, weight * 5)
                elif weight < 0.4:
                    color = interpolate_color(BLUE_D, TEAL, (weight - 0.2) * 5)
                elif weight < 0.6:
                    color = interpolate_color(TEAL, GREEN, (weight - 0.4) * 5)
                else:
                    color = interpolate_color(GREEN, YELLOW, (weight - 0.6) * 2.5)
                
                square = Square(
                    side_length=square_size,
                    fill_color=color,
                    fill_opacity=0.8,
                    stroke_color=BLUE_B,
                    stroke_width=1.5
                )
                
                # Position in grid
                x_pos = (j - 2) * (square_size + 0.08)
                y_pos = -(i - 2) * (square_size + 0.08)
                square.move_to([x_pos, y_pos, 0])
                
                # Add weight text
                weight_text = Text(
                    f"{weight:.2f}",
                    font_size=14,
                    color=WHITE if weight > 0.4 else BLUE_A
                ).move_to(square.get_center())
                
                heatmap.add(VGroup(square, weight_text))

        # Axis labels
        query_label = Text("Query →", font_size=20, color=BLUE_B).next_to(heatmap, LEFT, buff=0.5)
        key_label = Text("Key →", font_size=20, color=BLUE_B).next_to(heatmap, UP, buff=0.5)

        # Animate tokens appearing
        self.play(LaggedStart(*[FadeIn(token) for token in token_labels], lag_ratio=0.2))
        self.wait(0.5)

        # Animate heatmap building
        self.play(FadeIn(query_label), FadeIn(key_label))
        self.play(
            LaggedStart(*[FadeIn(cell) for cell in heatmap], lag_ratio=0.03),
            run_time=3
        )
        self.wait(1)

        # Highlight strongest attention
        highlights = VGroup()
        for i in range(5):
            max_idx = np.argmax(attention_weights[i])
            arrow = Arrow(
                token_labels[i].get_bottom(),
                heatmap[i * 5 + max_idx][0].get_top(),
                color=YELLOW,
                stroke_width=4,
                buff=0.1
            )
            highlights.add(arrow)

        self.play(LaggedStart(*[GrowArrow(arrow) for arrow in highlights], lag_ratio=0.15))
        self.wait(1.5)

        # Fade out and show formula
        self.play(
            FadeOut(VGroup(token_labels, heatmap, highlights, query_label, key_label))
        )

        # Show the attention formula
        formula = Text(
            "Attention(Q,K,V) = softmax(QK^T/√d_k)V",
            font_size=32,
            color=BLUE_B
        )
        
        self.play(Write(formula))
        self.wait(2)
        self.play(FadeOut(formula))


class NeuralNetworkActivation(Scene):
    """
    Neural Network with signal propagation through layers
    Shows forward propagation with sigmoid activation
    """
    def construct(self):
        # Title
        title = Text("Neural Network Forward Propagation", font_size=32, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        # Network architecture: [3, 4, 4, 2]
        layer_sizes = [3, 4, 4, 2]
        layer_spacing = 3.0
        neuron_spacing = 0.9

        # Create neurons
        all_neurons = VGroup()
        layer_positions = []

        for layer_idx, size in enumerate(layer_sizes):
            x_pos = -4.5 + layer_idx * layer_spacing
            layer = VGroup()
            
            for neuron_idx in range(size):
                y_pos = (size - 1) * neuron_spacing / 2 - neuron_idx * neuron_spacing
                
                neuron = Circle(
                    radius=0.25,
                    color=BLUE_D,
                    fill_opacity=0.3,
                    stroke_width=2
                )
                neuron.move_to([x_pos, y_pos, 0])
                layer.add(neuron)
            
            all_neurons.add(layer)
            layer_positions.append(x_pos)

        # Create connections (edges)
        edges = VGroup()
        for layer_idx in range(len(layer_sizes) - 1):
            for i, start_neuron in enumerate(all_neurons[layer_idx]):
                for j, end_neuron in enumerate(all_neurons[layer_idx + 1]):
                    # Random weights for visual variety
                    weight = np.random.uniform(0.2, 1.0)
                    opacity = 0.1 + weight * 0.2
                    
                    line = Line(
                        start_neuron.get_right(),
                        end_neuron.get_left(),
                        stroke_width=1,
                        stroke_opacity=opacity,
                        color=BLUE_B
                    )
                    edges.add(line)

        # Layer labels
        labels = VGroup(
            Text("Input", font_size=20, color=BLUE_A).next_to(all_neurons[0], DOWN, buff=0.4),
            Text("Hidden 1", font_size=20, color=BLUE_A).next_to(all_neurons[1], DOWN, buff=0.4),
            Text("Hidden 2", font_size=20, color=BLUE_A).next_to(all_neurons[2], DOWN, buff=0.4),
            Text("Output", font_size=20, color=BLUE_A).next_to(all_neurons[3], DOWN, buff=0.4)
        )

        # Build network
        self.play(
            LaggedStart(*[Create(edge) for edge in edges], lag_ratio=0.001),
            run_time=2
        )
        self.play(
            LaggedStart(*[FadeIn(neuron) for layer in all_neurons for neuron in layer], lag_ratio=0.02),
            run_time=1.5
        )
        self.play(FadeIn(labels))
        self.wait(0.5)

        # Signal propagation animation
        for propagation in range(2):
            for layer_idx in range(len(layer_sizes)):
                layer_neurons = all_neurons[layer_idx]
                
                # Activate neurons with wave effect
                animations = []
                for neuron in layer_neurons:
                    animations.extend([
                        neuron.animate.set_fill(YELLOW, opacity=0.8),
                        neuron.animate.set_stroke(YELLOW, width=3)
                    ])
                
                self.play(*animations, run_time=0.4)
                
                # Pulse effect
                self.play(
                    *[neuron.animate.scale(1.3).set_fill(GREEN, opacity=0.9) for neuron in layer_neurons],
                    run_time=0.2
                )
                self.play(
                    *[neuron.animate.scale(1/1.3).set_fill(BLUE_D, opacity=0.3).set_stroke(BLUE_D, width=2) 
                      for neuron in layer_neurons],
                    run_time=0.3
                )

        self.wait(0.5)

        # Show activation function
        self.play(FadeOut(VGroup(all_neurons, edges, labels)))

        # Sigmoid function
        axes = Axes(
            x_range=[-6, 6, 2],
            y_range=[-0.2, 1.2, 0.5],
            x_length=8,
            y_length=4,
            axis_config={"color": BLUE_B, "include_tip": True}
        )
        
        sigmoid_graph = axes.plot(
            lambda x: 1 / (1 + np.exp(-x)),
            color=YELLOW,
            stroke_width=3
        )
        
        formula = MathTex(
            r"\sigma(z) = \frac{1}{1 + e^{-z}}",
            font_size=40,
            color=BLUE_B
        ).to_edge(UP)
        
        func_label = Text("Sigmoid Activation", font_size=28, color=BLUE_A).next_to(formula, DOWN)

        self.play(Create(axes), Write(formula), Write(func_label))
        self.play(Create(sigmoid_graph), run_time=2)
        self.wait(2)
        self.play(FadeOut(VGroup(axes, sigmoid_graph, formula, func_label)))


class GradientDescentOptimization(Scene):
    """
    3D surface with ball rolling down to minimum (gradient descent)
    """
    def construct(self):
        # Title
        title = Text("Gradient Descent Optimization", font_size=32, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        # Create 2D loss surface (bowl shape)
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[0, 5, 1],
            x_length=10,
            y_length=5,
            axis_config={"color": BLUE_B}
        )
        
        # Loss function (quadratic bowl)
        loss_curve = axes.plot(
            lambda x: 0.3 * x**2 + 0.5,
            color=BLUE_D,
            stroke_width=3
        )
        
        # Fill under curve for depth
        area = axes.get_area(
            loss_curve,
            x_range=[-3, 3],
            color=[BLUE_E, BLUE_D],
            opacity=0.3
        )

        # Labels
        x_label = axes.get_x_axis_label("\\theta \\text{ (parameters)}", direction=DOWN, buff=0.3)
        y_label = axes.get_y_axis_label("J(\\theta) \\text{ (loss)}", direction=LEFT, buff=0.3)

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(loss_curve), FadeIn(area))
        self.wait(0.5)

        # Starting point (high on curve)
        start_x = 2.5
        start_y = 0.3 * start_x**2 + 0.5
        
        ball = Dot(
            axes.c2p(start_x, start_y),
            radius=0.15,
            color=YELLOW,
            fill_opacity=1
        )
        
        # Trail for path
        path_points = [ball.get_center()]

        self.play(FadeIn(ball, scale=0.5))
        self.wait(0.3)

        # Gradient descent steps
        learning_rate = 0.4
        current_x = start_x
        
        for step in range(12):
            # Calculate gradient (derivative)
            gradient = 0.6 * current_x
            
            # Update position
            current_x = current_x - learning_rate * gradient
            current_y = 0.3 * current_x**2 + 0.5
            
            new_pos = axes.c2p(current_x, current_y)
            
            # Gradient arrow
            arrow_start = ball.get_center()
            arrow_direction = normalize(new_pos - arrow_start)
            arrow = Arrow(
                arrow_start,
                arrow_start + arrow_direction * 0.5,
                color=RED,
                stroke_width=3,
                buff=0,
                max_tip_length_to_length_ratio=0.3
            )
            
            # Animate step
            self.play(GrowArrow(arrow), run_time=0.2)
            self.play(
                ball.animate.move_to(new_pos),
                FadeOut(arrow),
                run_time=0.4
            )
            
            path_points.append(ball.get_center())
            
            # Decrease learning rate (simulate momentum)
            learning_rate *= 0.95
            
            # Stop near minimum
            if abs(current_x) < 0.1:
                break

        # Highlight minimum
        self.play(
            ball.animate.set_color(GREEN).scale(1.4),
            run_time=0.4
        )
        self.play(
            ball.animate.scale(1/1.4),
            run_time=0.3
        )
        
        # Draw path
        path = VMobject(color=YELLOW, stroke_width=2)
        path.set_points_as_corners(path_points)
        self.play(Create(path), run_time=1)
        
        self.wait(1)

        # Show formula
        self.play(FadeOut(VGroup(axes, loss_curve, area, ball, path, x_label, y_label)))
        
        formula = MathTex(
            r"\theta_{t+1} = \theta_t - \alpha \nabla_\theta J(\theta_t)",
            font_size=40,
            color=BLUE_B
        )
        
        explanation = VGroup(
            MathTex(r"\theta_t", color=BLUE_A),
            Text(" = parameters at step t", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.2).next_to(formula, DOWN, buff=0.8)
        
        explanation2 = VGroup(
            MathTex(r"\alpha", color=BLUE_A),
            Text(" = learning rate", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.2).next_to(explanation, DOWN, buff=0.3)
        
        explanation3 = VGroup(
            MathTex(r"\nabla_\theta J", color=BLUE_A),
            Text(" = gradient of loss", font_size=24, color=WHITE),
        ).arrange(RIGHT, buff=0.2).next_to(explanation2, DOWN, buff=0.3)

        self.play(Write(formula))
        self.wait(0.5)
        self.play(
            LaggedStart(
                FadeIn(explanation),
                FadeIn(explanation2),
                FadeIn(explanation3),
                lag_ratio=0.3
            )
        )
        self.wait(2)
        self.play(FadeOut(VGroup(formula, explanation, explanation2, explanation3)))


class EmbeddingSpace(Scene):
    """
    Vector embeddings visualization showing semantic clustering
    Perfect for RAG and vector database concepts
    """
    def construct(self):
        # Title
        title = Text("Word Embeddings & Vector Space", font_size=32, color=BLUE)
        self.play(Write(title))
        self.wait(0.5)
        self.play(FadeOut(title))

        # Create coordinate system
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[-4, 4, 1],
            x_length=9,
            y_length=9,
            axis_config={"color": BLUE_B, "include_tip": True, "stroke_width": 2}
        )
        
        axes_labels = axes.get_axis_labels(
            x_label=Text("Dimension 1", font_size=20),
            y_label=Text("Dimension 2", font_size=20)
        )

        self.play(Create(axes), Write(axes_labels))
        self.wait(0.3)

        # Define semantic clusters
        # Animals cluster
        animals = [
            ("cat", np.array([2.5, 2.2]), RED),
            ("dog", np.array([2.8, 2.5]), RED),
            ("lion", np.array([2.3, 2.7]), RED),
            ("tiger", np.array([2.9, 2.1]), RED),
        ]
        
        # Food cluster
        foods = [
            ("pizza", np.array([-2.5, -2.3]), YELLOW),
            ("burger", np.array([-2.2, -2.6]), YELLOW),
            ("pasta", np.array([-2.7, -2.1]), YELLOW),
            ("sushi", np.array([-2.4, -2.5]), YELLOW),
        ]
        
        # Technology cluster
        tech = [
            ("AI", np.array([1.5, -2.5]), GREEN),
            ("ML", np.array([1.8, -2.2]), GREEN),
            ("neural", np.array([1.3, -2.8]), GREEN),
            ("LLM", np.array([1.6, -2.4]), GREEN),
        ]
        
        # Nature cluster
        nature = [
            ("tree", np.array([-1.8, 2.5]), BLUE),
            ("flower", np.array([-1.5, 2.2]), BLUE),
            ("river", np.array([-2.1, 2.7]), BLUE),
            ("mountain", np.array([-1.6, 2.4]), BLUE),
        ]

        all_words = animals + foods + tech + nature

        # Create word dots and labels
        word_objects = VGroup()
        
        for word, pos, color in all_words:
            # Vector point
            point = axes.c2p(pos[0], pos[1])
            dot = Dot(point, radius=0.12, color=color, fill_opacity=0.9)
            
            # Label
            label = Text(word, font_size=16, color=color).next_to(dot, UP, buff=0.15)
            
            word_objects.add(VGroup(dot, label))

        # Animate words appearing by cluster
        clusters = [
            [word_objects[i] for i in range(4)],           # animals
            [word_objects[i] for i in range(4, 8)],        # foods
            [word_objects[i] for i in range(8, 12)],       # tech
            [word_objects[i] for i in range(12, 16)],      # nature
        ]

        for cluster in clusters:
            self.play(
                LaggedStart(*[FadeIn(word, scale=0.5) for word in cluster], lag_ratio=0.15),
                run_time=1
            )
            self.wait(0.2)

        self.wait(0.5)

        # Show vector similarity (cosine similarity visualization)
        # Query: "cat" looking for similar words
        query_word = "cat"
        query_idx = 0  # cat is first
        query_pos = axes.c2p(animals[0][1][0], animals[0][1][1])

        # Highlight query
        query_circle = Circle(radius=0.25, color=YELLOW, stroke_width=3).move_to(query_pos)
        query_label = Text("Query", font_size=20, color=YELLOW).next_to(query_circle, DOWN, buff=0.3)
        
        self.play(Create(query_circle), Write(query_label))
        self.wait(0.3)

        # Draw similarity arrows (to nearby animals)
        similarity_arrows = VGroup()
        for i, (word, pos, color) in enumerate(animals[1:], start=1):
            target_pos = axes.c2p(pos[0], pos[1])
            arrow = Arrow(
                query_pos,
                target_pos,
                color=YELLOW,
                stroke_width=2,
                buff=0.15,
                max_tip_length_to_length_ratio=0.2
            )
            
            # Distance label (similarity score)
            dist = np.linalg.norm(animals[0][1] - pos)
            similarity = max(0, 1 - dist / 2)  # Normalize to 0-1
            score_label = Text(
                f"{similarity:.2f}",
                font_size=14,
                color=YELLOW
            ).next_to(arrow, UP, buff=0.05)
            
            similarity_arrows.add(VGroup(arrow, score_label))

        self.play(
            LaggedStart(*[GrowArrow(arrow[0]) for arrow in similarity_arrows], lag_ratio=0.2)
        )
        self.play(
            LaggedStart(*[FadeIn(arrow[1]) for arrow in similarity_arrows], lag_ratio=0.2)
        )
        self.wait(1.5)

        # Cluster highlighting
        # Draw circles around semantic clusters
        cluster_circles = VGroup(
            Circle(radius=1.2, color=RED, stroke_width=2, stroke_opacity=0.5)
                .move_to(axes.c2p(2.6, 2.4)),
            Circle(radius=1.2, color=YELLOW, stroke_width=2, stroke_opacity=0.5)
                .move_to(axes.c2p(-2.45, -2.4)),
            Circle(radius=1.2, color=GREEN, stroke_width=2, stroke_opacity=0.5)
                .move_to(axes.c2p(1.55, -2.5)),
            Circle(radius=1.2, color=BLUE, stroke_width=2, stroke_opacity=0.5)
                .move_to(axes.c2p(-1.75, 2.5)),
        )

        self.play(
            FadeOut(query_circle),
            FadeOut(query_label),
            FadeOut(similarity_arrows)
        )
        
        self.play(
            LaggedStart(*[Create(circle) for circle in cluster_circles], lag_ratio=0.2),
            run_time=1.5
        )
        self.wait(1)

        # Fade to formula
        self.play(
            FadeOut(VGroup(axes, axes_labels, word_objects, cluster_circles))
        )

        # Show distance formula
        formula = MathTex(
            r"d(\mathbf{x}, \mathbf{y}) = ||\mathbf{x} - \mathbf{y}||_2 = \sqrt{\sum_{i=1}^{n}(x_i - y_i)^2}",
            font_size=36,
            color=BLUE_B
        )
        
        cosine_sim = MathTex(
            r"\text{similarity} = \frac{\mathbf{x} \cdot \mathbf{y}}{||\mathbf{x}|| \cdot ||\mathbf{y}||}",
            font_size=36,
            color=GREEN
        ).next_to(formula, DOWN, buff=0.8)
        
        explanation = Text(
            "Used in RAG & Vector Databases",
            font_size=24,
            color=BLUE_A
        ).next_to(cosine_sim, DOWN, buff=0.6)

        self.play(Write(formula))
        self.wait(1)
        self.play(Write(cosine_sim))
        self.wait(0.5)
        self.play(FadeIn(explanation))
        self.wait(2)
        self.play(FadeOut(VGroup(formula, cosine_sim, explanation)))
