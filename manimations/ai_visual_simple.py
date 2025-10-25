from manim import *
import numpy as np


class AttentionMechanism(Scene):
    """
    Transformer Attention Mechanism Visualization
    Shows how attention weights connect tokens with beautiful heatmap
    """
    def construct(self):
        # Title
        title = Text("Attention Mechanism", font_size=48, color=BLUE_B)
        subtitle = Text("Core of Transformer LLMs", font_size=24, color=BLUE_D)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(0.8)
        self.play(
            title.animate.to_edge(UP).scale(0.6),
            FadeOut(subtitle)
        )
        
        # Create query, key, value tokens
        tokens = ["The", "cat", "sat", "on", "mat"]
        token_objects = VGroup(*[
            Text(t, font_size=28, color=WHITE)
            for t in tokens
        ]).arrange(RIGHT, buff=0.6)
        
        # Add "Tokens" label
        tokens_label = Text("Tokens", font_size=24, color=BLUE_B)
        tokens_label.next_to(token_objects, UP, buff=0.5)
        
        self.play(FadeIn(token_objects))
        self.play(Write(tokens_label))
        self.wait(0.8)
        
        # Create attention matrix (heatmap)
        attention_weights = np.array([
            [0.8, 0.1, 0.05, 0.03, 0.02],
            [0.1, 0.7, 0.15, 0.03, 0.02],
            [0.05, 0.2, 0.6, 0.1, 0.05],
            [0.03, 0.05, 0.2, 0.65, 0.07],
            [0.02, 0.03, 0.05, 0.15, 0.75],
        ])
        
        # Create heatmap
        matrix_group = VGroup()
        for i in range(5):
            for j in range(5):
                intensity = attention_weights[i][j]
                square = Square(
                    side_length=0.5,
                    fill_color=interpolate_color(BLUE_E, YELLOW, intensity),
                    fill_opacity=0.8,
                    stroke_width=1,
                    stroke_color=BLUE_B
                )
                square.move_to(np.array([j * 0.55 - 1.1, -i * 0.55 + 0.5, 0]))
                matrix_group.add(square)
        
        # Add "Attention Matrix" label
        matrix_label = Text("Attention Weights", font_size=24, color=YELLOW)
        matrix_label.next_to(matrix_group, LEFT, buff=0.8)
        
        self.play(
            token_objects.animate.shift(UP * 2),
            FadeOut(tokens_label),
            FadeIn(matrix_group, shift=UP)
        )
        self.play(Write(matrix_label))
        self.wait(1)
        
        # Show connections from "cat" to other words
        cat_idx = 1
        
        # Highlight "cat" token
        cat_highlight = token_objects[cat_idx].copy()
        cat_highlight.set_color(YELLOW).scale(1.3)
        
        focus_label = Text("Focus: 'cat'", font_size=22, color=YELLOW)
        focus_label.next_to(token_objects[cat_idx], DOWN, buff=0.8)
        
        self.play(
            Transform(token_objects[cat_idx], cat_highlight),
            Write(focus_label)
        )
        self.wait(0.5)
        
        connections = VGroup()
        for target_idx in range(5):
            if target_idx != cat_idx:
                weight = attention_weights[cat_idx][target_idx]
                if weight > 0.05:
                    line = Line(
                        token_objects[cat_idx].get_bottom(),
                        token_objects[target_idx].get_top(),
                        color=interpolate_color(BLUE, YELLOW, weight * 2),
                        stroke_width=weight * 10,
                        stroke_opacity=0.7
                    )
                    connections.add(line)
        
        self.play(Create(connections), run_time=2)
        self.wait(2)
        
        # Fade out
        self.play(
            FadeOut(token_objects),
            FadeOut(matrix_group),
            FadeOut(matrix_label),
            FadeOut(connections),
            FadeOut(focus_label),
            FadeOut(title)
        )


class NeuralNetworkActivation(Scene):
    """
    Neural Network Forward Propagation
    Shows signals flowing through layers with activation
    """
    def construct(self):
        # Title
        title = Text("Neural Network", font_size=48, color=BLUE_B)
        subtitle = Text("Foundation of Deep Learning", font_size=24, color=BLUE_D)
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(0.8)
        self.play(
            title.animate.to_edge(UP).scale(0.6),
            FadeOut(subtitle)
        )
        
        # Create network layers
        layer_sizes = [4, 6, 6, 3]
        layers = []
        layer_labels = ["Input", "Hidden 1", "Hidden 2", "Output"]
        
        for i, size in enumerate(layer_sizes):
            layer = VGroup(*[
                Circle(radius=0.2, color=BLUE_B, fill_opacity=0.3)
                for _ in range(size)
            ]).arrange(DOWN, buff=0.4)
            layer.shift(LEFT * 4 + RIGHT * i * 2.8)
            layers.append(layer)
        
        # Create all neurons
        all_neurons = VGroup(*layers)
        self.play(FadeIn(all_neurons), run_time=1.5)
        
        # Add layer labels
        labels = VGroup()
        for i, (layer, label_text) in enumerate(zip(layers, layer_labels)):
            label = Text(label_text, font_size=20, color=BLUE_B)
            label.next_to(layer, DOWN, buff=0.5)
            labels.add(label)
        
        self.play(Write(labels), run_time=1)
        self.wait(0.5)
        
        # Create connections with better visibility
        connections = VGroup()
        for i in range(len(layers) - 1):
            for neuron1 in layers[i]:
                for neuron2 in layers[i + 1]:
                    line = Line(
                        neuron1.get_center(),
                        neuron2.get_center(),
                        stroke_width=1.5,
                        stroke_opacity=0.4,
                        color=BLUE_C
                    )
                    connections.add(line)
        
        self.play(Create(connections), run_time=2)
        
        # Animate signal propagation
        for layer_idx in range(len(layers)):
            layer = layers[layer_idx]
            
            # Light up neurons
            self.play(*[
                neuron.animate.set_fill(YELLOW, opacity=0.8).set_stroke(YELLOW, width=2)
                for neuron in layer
            ], run_time=0.5)
            
            # Send signals to next layer
            if layer_idx < len(layers) - 1:
                next_layer = layers[layer_idx + 1]
                signal_lines = VGroup()
                
                for neuron1 in layer:
                    for neuron2 in next_layer:
                        line = Line(
                            neuron1.get_center(),
                            neuron2.get_center(),
                            color=YELLOW,
                            stroke_width=2,
                            stroke_opacity=0.6
                        )
                        signal_lines.add(line)
                
                self.play(
                    Create(signal_lines),
                    run_time=0.8
                )
                self.play(FadeOut(signal_lines), run_time=0.3)
            
            # Dim previous layer
            if layer_idx > 0:
                self.play(*[
                    neuron.animate.set_fill(BLUE_B, opacity=0.3).set_stroke(BLUE_B, width=1)
                    for neuron in layers[layer_idx - 1]
                ], run_time=0.3)
        
        self.wait(1)
        
        # Final pulse with "Output" label
        output_label = Text("Prediction", font_size=22, color=GREEN).next_to(layers[-1], RIGHT, buff=0.8)
        self.play(*[
            neuron.animate.scale(1.3).set_fill(GREEN, opacity=0.9)
            for neuron in layers[-1]
        ])
        self.play(Write(output_label))
        self.play(*[
            neuron.animate.scale(1/1.3)
            for neuron in layers[-1]
        ])
        
        self.wait(1)
        self.play(FadeOut(all_neurons), FadeOut(connections), FadeOut(labels), FadeOut(output_label), FadeOut(title))


class GradientDescent(Scene):
    """
    Gradient Descent Optimization - How AI Learns
    Shows how neural networks minimize error
    """
    def construct(self):
        # Title with AI context
        title = Text("Gradient Descent", font_size=48, color=BLUE_B, font="Sans")
        subtitle = Text("How Neural Networks Learn", font_size=24, color=BLUE_D, font="Sans")
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(0.8)
        self.play(
            title.animate.to_edge(UP).scale(0.6),
            FadeOut(subtitle)
        )
        
        # Create loss surface (parabola)
        axes = Axes(
            x_range=[-4, 4, 1],
            y_range=[0, 8, 2],
            x_length=8,
            y_length=5,
            axis_config={"color": BLUE_D},
        ).shift(DOWN * 0.5)
        
        # Loss function (quadratic)
        def loss_func(x):
            return 0.3 * x ** 2 + 0.5
        
        curve = axes.plot(loss_func, color=BLUE_B, stroke_width=4)
        
        # Add axis labels with better positioning
        x_label = Text("Model Parameters", font_size=20, color=BLUE_C, font="Sans")
        x_label.next_to(axes, DOWN, buff=0.4)
        
        y_label = Text("Loss", font_size=22, color=RED_C, font="Sans")
        y_label.next_to(axes, LEFT, buff=0.5).shift(UP * 1.5)
        
        self.play(Create(axes), Create(curve))
        self.play(Write(x_label), Write(y_label))
        self.wait(0.5)
        
        # Starting point
        x_val = 3.5
        ball = Dot(
            axes.c2p(x_val, loss_func(x_val)),
            color=YELLOW,
            radius=0.15
        )
        
        start_label = Text("Start", font_size=20, color=YELLOW, font="Sans")
        start_label.next_to(ball, RIGHT, buff=0.3)
        
        self.play(FadeIn(ball, scale=0.5))
        self.play(Write(start_label))
        self.wait(0.8)
        self.play(FadeOut(start_label))
        
        # Add learning rate label
        lr_label = Text("Learning Rate", font_size=18, color=GREEN, font="Sans")
        lr_label.to_corner(UP + RIGHT, buff=0.8)
        self.play(Write(lr_label))
        
        # Gradient descent steps
        learning_rate = 0.4
        steps = 15
        step_counter = 0
        
        for step in range(steps):
            # Calculate gradient (derivative)
            gradient = 0.6 * x_val  # derivative of 0.3x^2
            
            # Update position
            x_new = x_val - learning_rate * gradient
            
            # Create arrow showing gradient
            arrow = Arrow(
                ball.get_center(),
                axes.c2p(x_new, loss_func(x_val)),
                color=RED,
                buff=0,
                stroke_width=4,
                max_tip_length_to_length_ratio=0.2
            )
            
            # Show gradient label on first few steps
            if step < 3:
                grad_label = Text("Gradient", font_size=16, color=RED, font="Sans").next_to(arrow, UP, buff=0.1)
                self.play(GrowArrow(arrow), Write(grad_label), run_time=0.4)
                self.play(
                    ball.animate.move_to(axes.c2p(x_new, loss_func(x_new))),
                    FadeOut(arrow),
                    FadeOut(grad_label),
                    run_time=0.5
                )
            else:
                # Animate step
                self.play(GrowArrow(arrow), run_time=0.2)
                self.play(
                    ball.animate.move_to(axes.c2p(x_new, loss_func(x_new))),
                    FadeOut(arrow),
                    run_time=0.4
                )
            
            x_val = x_new
            step_counter += 1
            
            # Slow down near minimum
            if abs(gradient) < 0.1:
                learning_rate *= 0.8
        
        self.play(FadeOut(lr_label))
        
        # Success pulse
        self.play(
            ball.animate.scale(1.5).set_color(GREEN),
            run_time=0.5
        )
        self.play(
            ball.animate.scale(1/1.5),
            run_time=0.5
        )
        
        # Show minimum label - positioned away from axes
        min_label = Text("Minimum", font_size=22, color=GREEN, font="Sans")
        min_label.move_to(axes.c2p(0, 6.5))
        
        self.play(Write(min_label))
        
        self.wait(2)
        self.play(
            FadeOut(axes), FadeOut(curve), FadeOut(ball), 
            FadeOut(min_label),
            FadeOut(x_label), FadeOut(y_label), FadeOut(title)
        )


class EmbeddingSpace(Scene):
    """
    Vector Embedding Space Visualization
    Shows semantic similarity in 2D space for RAG/vector databases
    """
    def construct(self):
        # Title with RAG context
        title = Text("Vector Embeddings", font_size=48, color=BLUE_B, font="Sans")
        subtitle = Text("Powers RAG & Semantic Search", font_size=24, color=BLUE_D, font="Sans")
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(0.8)
        self.play(
            title.animate.to_edge(UP).scale(0.6),
            FadeOut(subtitle)
        )
        
        # Create 2D coordinate system
        axes = Axes(
            x_range=[-5, 5, 1],
            y_range=[-5, 5, 1],
            x_length=8,
            y_length=6,
            axis_config={"color": BLUE_D, "include_tip": True},
        )
        
        self.play(Create(axes))
        
        # Define word categories with better-spaced positions and fixed directions
        words = {
            "cat": (1.8, 3.5, YELLOW, UR),
            "dog": (2.8, 2.5, YELLOW, RIGHT),
            "kitten": (1.2, 2.8, YELLOW, LEFT),
            "car": (-3.5, -1.5, BLUE, LEFT),
            "truck": (-3.8, -2.8, BLUE, DL),
            "vehicle": (-2.3, -1.8, BLUE, UR),
            "apple": (0.5, -3.8, GREEN, DR),
            "banana": (1.2, -3.2, GREEN, RIGHT),
            "fruit": (-0.3, -3.0, GREEN, LEFT),
        }
        
        word_dots = VGroup()
        word_labels = VGroup()
        
        # Create and position words with smart label placement
        for word, (x, y, color, direction) in words.items():
            dot = Dot(axes.c2p(x, y), color=color, radius=0.12)
            label = Text(word, font_size=18, color=color, font="Sans")
            label.next_to(dot, direction, buff=0.18)
            word_dots.add(dot)
            word_labels.add(label)
        
        self.play(
            LaggedStart(*[FadeIn(dot, scale=0.5) for dot in word_dots], lag_ratio=0.1),
            run_time=2
        )
        self.play(
            LaggedStart(*[Write(label) for label in word_labels], lag_ratio=0.1),
            run_time=2
        )
        
        self.wait(1)
        
        # Show semantic similarity within category (updated positions)
        cat_pos = axes.c2p(1.8, 3.5)
        dog_pos = axes.c2p(2.8, 2.5)
        car_pos = axes.c2p(-3.5, -1.5)
        
        similarity_line = DashedLine(cat_pos, dog_pos, color=YELLOW, stroke_width=3)
        sim_label = Text("Similar", font_size=16, color=YELLOW, font="Sans")
        sim_label.move_to(axes.c2p(2.3, 2.0))
        
        distance_line = Line(cat_pos, car_pos, color=RED_D, stroke_width=2, stroke_opacity=0.3)
        dist_label = Text("Different", font_size=16, color=RED_D, font="Sans")
        dist_label.move_to(axes.c2p(-0.8, 0.8))
        
        # Animate similarity visualization
        self.play(Create(similarity_line), Write(sim_label))
        self.wait(1)
        self.play(Create(distance_line), Write(dist_label))
        self.wait(1.5)
        
        # Add RAG context label
        rag_info = Text(
            "RAG finds documents by vector distance",
            font_size=18,
            color=BLUE_C,
            font="Sans"
        )
        rag_info.to_edge(DOWN, buff=0.5)
        self.play(FadeIn(rag_info, shift=UP))
        self.wait(2)
        
        # Fade out everything
        self.play(
            FadeOut(axes),
            FadeOut(word_dots),
            FadeOut(word_labels),
            FadeOut(similarity_line),
            FadeOut(sim_label),
            FadeOut(distance_line),
            FadeOut(dist_label),
            FadeOut(rag_info),
            FadeOut(title),
        )
        self.wait(0.5)


class ContextWindow(Scene):
    """
    Context Window & Token Management
    Shows how conversation history accumulates and gets pruned
    """
    def construct(self):
        # Title
        title = Text("Context Window", font_size=48, color=BLUE_B, font="Sans")
        subtitle = Text("How LLMs Remember Conversations", font_size=24, color=BLUE_D, font="Sans")
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(0.8)
        self.play(
            title.animate.to_edge(UP).scale(0.6),
            FadeOut(subtitle)
        )
        
        # Create window frame
        window = Rectangle(
            width=10,
            height=5,
            color=BLUE,
            stroke_width=3
        ).shift(DOWN * 0.3)
        
        window_label = Text("Context Window", font_size=18, color=BLUE_C, font="Sans")
        window_label.next_to(window, UP, buff=0.2)
        
        self.play(Create(window), Write(window_label))
        self.wait(0.5)
        
        # Token counter
        token_count = 0
        max_tokens = 8
        counter = Text(f"Tokens: {token_count}/{max_tokens}", font_size=20, color=GREEN, font="Sans")
        counter.to_corner(UR, buff=0.8)
        self.play(Write(counter))
        
        # Message queue
        messages = VGroup()
        
        # Helper function to create message bubble
        def create_message(text, color, side="left"):
            bubble = RoundedRectangle(
                width=4,
                height=0.6,
                corner_radius=0.15,
                fill_color=color,
                fill_opacity=0.3,
                stroke_color=color,
                stroke_width=2
            )
            label = Text(text, font_size=16, color=WHITE, font="Sans")
            label.move_to(bubble.get_center())
            message = VGroup(bubble, label)
            return message
        
        # Add messages one by one
        conversation = [
            ("User: Hello!", BLUE, 2),
            ("AI: Hi there!", GREEN, 2),
            ("User: What is AI?", BLUE, 3),
            ("AI: AI is...", GREEN, 2),
        ]
        
        y_pos = window.get_top()[1] - 0.5
        
        for i, (text, color, tokens) in enumerate(conversation):
            # Create message
            msg = create_message(text, color)
            msg.move_to([0, y_pos, 0])
            
            # Check if window is full
            if token_count + tokens <= max_tokens:
                # Add message
                self.play(FadeIn(msg, shift=UP), run_time=0.5)
                messages.add(msg)
                token_count += tokens
                
                # Update counter
                new_counter = Text(f"Tokens: {token_count}/{max_tokens}", font_size=20, color=GREEN, font="Sans")
                new_counter.to_corner(UR, buff=0.8)
                self.play(Transform(counter, new_counter), run_time=0.3)
                
                y_pos -= 0.8
                self.wait(0.3)
            else:
                # Window full - need to prune
                full_label = Text("FULL!", font_size=24, color=RED, font="Sans", weight=BOLD)
                full_label.next_to(counter, DOWN, buff=0.3)
                self.play(Write(full_label))
                self.wait(0.5)
                
                # Remove oldest message
                if len(messages) > 0:
                    oldest = messages[0]
                    self.play(
                        FadeOut(oldest, shift=LEFT),
                        FadeOut(full_label),
                        run_time=0.5
                    )
                    messages.remove(oldest)
                    token_count = token_count - conversation[0][2]  # Remove first message tokens
                    conversation.pop(0)
                    
                    # Shift remaining messages up
                    self.play(
                        messages.animate.shift(UP * 0.8),
                        run_time=0.5
                    )
                    
                    # Update counter
                    new_counter = Text(f"Tokens: {token_count}/{max_tokens}", font_size=20, color=YELLOW, font="Sans")
                    new_counter.to_corner(UR, buff=0.8)
                    self.play(Transform(counter, new_counter), run_time=0.3)
                    
                    # Now add new message
                    msg = create_message(text, color)
                    msg.move_to([0, y_pos, 0])
                    self.play(FadeIn(msg, shift=UP), run_time=0.5)
                    messages.add(msg)
                    token_count += tokens
                    
                    # Update counter again
                    new_counter = Text(f"Tokens: {token_count}/{max_tokens}", font_size=20, color=GREEN, font="Sans")
                    new_counter.to_corner(UR, buff=0.8)
                    self.play(Transform(counter, new_counter), run_time=0.3)
        
        self.wait(1)
        
        # Show "sliding window" concept
        sliding_text = Text("Sliding Window", font_size=22, color=YELLOW, font="Sans")
        sliding_text.to_edge(DOWN, buff=0.8)
        arrow_left = Arrow(window.get_left(), window.get_left() + LEFT * 1, color=YELLOW)
        
        self.play(Write(sliding_text), GrowArrow(arrow_left))
        self.wait(1.5)
        
        # Fade out
        self.play(
            FadeOut(window),
            FadeOut(window_label),
            FadeOut(messages),
            FadeOut(counter),
            FadeOut(sliding_text),
            FadeOut(arrow_left),
            FadeOut(title)
        )
        self.wait(0.5)


class TemperatureSampling(Scene):
    """
    Temperature & Sampling Strategies
    Shows how temperature affects token selection randomness
    """
    def construct(self):
        # Title
        title = Text("Temperature Sampling", font_size=48, color=BLUE_B, font="Sans")
        subtitle = Text("Controlling LLM Creativity", font_size=24, color=BLUE_D, font="Sans")
        subtitle.next_to(title, DOWN, buff=0.2)
        
        self.play(Write(title))
        self.play(FadeIn(subtitle, shift=UP))
        self.wait(0.8)
        self.play(
            title.animate.to_edge(UP).scale(0.6),
            FadeOut(subtitle)
        )
        
        # Create axes for probability distribution
        axes = Axes(
            x_range=[0, 5, 1],
            y_range=[0, 1, 0.2],
            x_length=8,
            y_length=4,
            axis_config={"color": BLUE_D},
            tips=False
        ).shift(DOWN * 0.5)
        
        x_label = Text("Token Options", font_size=18, color=BLUE_C, font="Sans")
        x_label.next_to(axes, DOWN, buff=0.3)
        y_label = Text("Probability", font_size=18, color=BLUE_C, font="Sans")
        y_label.next_to(axes, LEFT, buff=0.3).shift(UP * 1)
        
        self.play(Create(axes), Write(x_label), Write(y_label))
        
        # Token labels
        tokens = ["the", "a", "my", "our", "this"]
        token_labels = VGroup()
        for i, token in enumerate(tokens):
            label = Text(token, font_size=14, color=WHITE, font="Sans")
            label.move_to(axes.c2p(i + 0.5, -0.15))
            token_labels.add(label)
        
        self.play(Write(token_labels))
        self.wait(0.5)
        
        # Temperature scenarios
        temperatures = [
            (0.1, "Low Temp: Deterministic", [0.85, 0.08, 0.04, 0.02, 0.01], BLUE),
            (0.7, "Medium Temp: Balanced", [0.45, 0.25, 0.15, 0.10, 0.05], GREEN),
            (1.5, "High Temp: Creative", [0.25, 0.22, 0.20, 0.18, 0.15], RED)
        ]
        
        for temp, label_text, probs, color in temperatures:
            # Temperature label
            temp_label = Text(label_text, font_size=22, color=color, font="Sans", weight=BOLD)
            temp_label.to_corner(UR, buff=0.8)
            
            # Create bars
            bars = VGroup()
            for i, prob in enumerate(probs):
                bar = Rectangle(
                    width=0.6,
                    height=prob * 3.5,
                    fill_color=color,
                    fill_opacity=0.7,
                    stroke_color=color,
                    stroke_width=2
                )
                bar.move_to(axes.c2p(i + 0.5, prob / 2))
                bars.add(bar)
            
            # Animate
            self.play(Write(temp_label), run_time=0.5)
            self.play(
                LaggedStart(*[GrowFromEdge(bar, DOWN) for bar in bars], lag_ratio=0.1),
                run_time=1
            )
            self.wait(1.5)
            
            # Highlight most likely token
            highlight = bars[0].copy().set_color(YELLOW).set_stroke(YELLOW, width=4)
            self.play(Create(highlight), run_time=0.4)
            self.play(FadeOut(highlight), run_time=0.4)
            self.wait(0.5)
            
            # Clear for next
            if temp != 1.5:  # Don't clear on last iteration
                self.play(
                    FadeOut(bars),
                    FadeOut(temp_label),
                    run_time=0.5
                )
        
        self.wait(1)
        
        # Final explanation
        explanation = Text(
            "Higher temp = more random = creative",
            font_size=18,
            color=YELLOW,
            font="Sans"
        )
        explanation.to_edge(DOWN, buff=0.8)
        self.play(Write(explanation))
        self.wait(2)
        
        # Fade out
        self.play(
            FadeOut(axes),
            FadeOut(x_label),
            FadeOut(y_label),
            FadeOut(token_labels),
            FadeOut(bars),
            FadeOut(temp_label),
            FadeOut(explanation),
            FadeOut(title)
        )
        self.wait(0.5)
