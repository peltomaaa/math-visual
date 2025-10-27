import { useState } from "react";
import { InlineMath, BlockMath } from "react-katex";
import "katex/dist/katex.min.css";
import "./App.css";
import { RiRobot2Line, RiFunctionLine } from "react-icons/ri";

const animations = [
  {
    id: 12,
    title: "Attention Mechanism",
    description: "How transformers understand relationships between words",
    video: "/videos/AttentionMechanism.mp4",
    category: "AI & Machine Learning",
    formula:
      "\\text{Attention}(Q,K,V) = \\text{softmax}\\left(\\frac{QK^T}{\\sqrt{d_k}}\\right)V",
    explanation:
      "The attention mechanism is the core technology behind modern Large Language Models like ChatGPT and Claude. It calculates how much each word should 'pay attention' to every other word in a sentence. The Query (Q) represents what we're looking for, Keys (K) represent available information, and Values (V) contain the actual data. The softmax function converts these into probability weights, creating the attention matrix that shows word relationships. This allows AI to understand context: in 'The cat sat on the mat,' attention helps the model connect 'cat' with 'sat' (the action) more strongly than with 'mat.'",
    mathConcept: "Self-Attention & Transformers",
  },
  {
    id: 13,
    title: "Neural Network",
    description: "Signals propagating through layers of neurons",
    video: "/videos/NeuralNetworkActivation.mp4",
    category: "AI & Machine Learning",
    formula: "a^{(l)} = \\sigma(W^{(l)}a^{(l-1)} + b^{(l)})",
    explanation:
      "Neural networks are the foundation of modern AI, inspired by the human brain. Each circle represents a neuron, and lines show weighted connections between them. Information flows from left (input layer) through hidden layers to the right (output layer). At each neuron, inputs are multiplied by weights, summed, and passed through an activation function σ (sigma) - commonly sigmoid, ReLU, or tanh. This activation function introduces non-linearity, allowing networks to learn complex patterns. During training, the network adjusts weights through backpropagation to minimize prediction errors. The animation shows forward propagation: how data flows through the network to make predictions.",
    mathConcept: "Forward Propagation & Activation",
  },
  {
    id: 14,
    title: "Gradient Descent",
    description: "Optimization algorithm finding the minimum loss",
    video: "/videos/GradientDescent.mp4",
    category: "AI & Machine Learning",
    formula: "\\theta_{t+1} = \\theta_t - \\alpha \\nabla_\\theta J(\\theta_t)",
    explanation:
      "Gradient descent is how AI models learn - it's the optimization engine behind neural networks, LLMs, and most machine learning. Imagine rolling a ball down a hill to find the lowest point; that's gradient descent finding the minimum of a loss function J. The gradient ∇J is the slope (direction of steepest ascent), so moving opposite to it (downhill) reduces error. The learning rate α controls step size: too large and you overshoot the minimum; too small and learning is slow. The algorithm repeatedly calculates the gradient, updates parameters θ (weights), and gradually converges to optimal values where the model makes its best predictions. This is the fundamental learning mechanism that powers AI.",
    mathConcept: "Optimization & Learning",
  },
  {
    id: 15,
    title: "Vector Embeddings",
    description: "Semantic relationships in vector space for RAG systems",
    video: "/videos/EmbeddingSpace.mp4",
    category: "AI & Machine Learning",
    formula:
      "\\text{similarity}(\\vec{v}_1, \\vec{v}_2) = \\frac{\\vec{v}_1 \\cdot \\vec{v}_2}{||\\vec{v}_1|| \\, ||\\vec{v}_2||}",
    explanation:
      "Vector embeddings are how AI represents meaning as numbers, powering RAG (Retrieval-Augmented Generation), vector databases, and semantic search. Each word or document is converted into a high-dimensional vector (typically 384-1536 dimensions), where semantic similarity = geometric proximity. Words with similar meanings cluster together: 'cat,' 'dog,' 'kitten' form an animal cluster; 'car,' 'truck,' 'vehicle' form a vehicle cluster. The formula shows cosine similarity: measuring the angle between vectors to find semantic closeness. In RAG systems, your query is embedded, then a vector database (like Pinecone, Weaviate, or Chroma) quickly finds the most similar document chunks using efficient nearest-neighbor search. This enables AI to retrieve relevant context before generating responses.",
    mathConcept: "Vector Space & Semantic Similarity",
  },
  {
    id: 16,
    title: "Context Window",
    description: "How LLMs manage conversation memory and token limits",
    video: "/videos/ContextWindow.mp4",
    category: "AI & Machine Learning",
    formula:
      "\\text{Context} = [m_1, m_2, ..., m_n] \\quad \\text{where} \\quad \\sum \\text{tokens}(m_i) \\leq L",
    explanation:
      "The context window is the 'working memory' of an LLM - the maximum amount of text it can process at once, measured in tokens. When you chat with ChatGPT or Claude, every message (both yours and the AI's) consumes tokens from this limited window. Modern models range from 4K tokens (GPT-3.5 early) to 200K+ tokens (Claude 3.5 Sonnet, GPT-4 Turbo). Once the window fills up, older messages get pruned in a 'sliding window' fashion - the AI literally forgets early parts of the conversation. This is why LLMs can't remember what you said 100 messages ago. The formula shows the constraint: sum of all message tokens must stay under the limit L. This limitation is why RAG (Retrieval-Augmented Generation) exists: instead of cramming everything into context, we store information in vector databases and retrieve only relevant chunks when needed. Understanding context windows is crucial for building AI agents and chatbots that handle long conversations effectively.",
    mathConcept: "Memory Management & Token Limits",
  },
  {
    id: 17,
    title: "Temperature Sampling",
    description: "Controlling randomness and creativity in LLM outputs",
    video: "/videos/TemperatureSampling.mp4",
    category: "AI & Machine Learning",
    formula:
      "P_i = \\frac{e^{z_i/T}}{\\sum_j e^{z_j/T}} \\quad \\text{where } T = \\text{temperature}",
    explanation:
      "Temperature controls how 'creative' or 'random' an LLM's responses are by adjusting the probability distribution over next tokens. At low temperature (T=0.1), the model becomes deterministic - it almost always picks the highest-probability token, giving consistent, focused outputs. This is ideal for factual tasks, code generation, or when you want reproducible results. At medium temperature (T=0.7), the default for most chatbots, there's balanced randomness - the model considers alternative tokens but still favors likely ones. High temperature (T=1.5+) flattens the distribution, making the model sample from less likely tokens, producing creative, diverse, sometimes surprising outputs - great for brainstorming or creative writing. The formula shows how temperature T scales logits (z) before softmax: higher T spreads probability more evenly. This is why the same prompt gives different responses each time - temperature introduces controlled randomness. API providers let you tune this parameter alongside top-p (nucleus sampling) and top-k for fine-grained control over generation behavior.",
    mathConcept: "Probability Distribution & Sampling",
  },
  {
    id: 1,
    title: "Fractal Tree",
    description:
      "Recursive branching structure showing natural fractal patterns",
    video: "/videos/FractalTree.mp4",
    category: "Fractals",
    formula: "\\text{Branch}(n) = 2 \\cdot \\text{Branch}(n-1)",
    explanation:
      "Each branch splits into two smaller branches at angle θ = π/6, with length scaling by 0.7. The fractal dimension demonstrates self-similarity across scales.",
    mathConcept: "Recursive Functions & Fractals",
  },
  {
    id: 2,
    title: "Mandelbrot Set",
    description: "Infinite complexity emerging from simple iteration",
    video: "/videos/MandelbrotZoomSpectacular.mp4",
    category: "Fractals",
    formula: "z_{n+1} = z_n^2 + c",
    explanation:
      "The Mandelbrot set contains all complex numbers c for which the iterative sequence remains bounded. Points are colored based on escape time, revealing intricate boundary structures.",
    mathConcept: "Complex Dynamics",
  },
  {
    id: 3,
    title: "Lorenz Attractor",
    description: "Chaotic system exhibiting the butterfly effect",
    video: "/videos/LorenzAttractorPath.mp4",
    category: "Chaos Theory",
    formula:
      "\\frac{dx}{dt} = \\sigma(y-x), \\frac{dy}{dt} = x(\\rho-z)-y, \\frac{dz}{dt} = xy-\\beta z",
    explanation:
      "A system of three differential equations modeling atmospheric convection. Despite being deterministic, tiny changes in initial conditions lead to vastly different trajectories.",
    mathConcept: "Differential Equations & Chaos",
  },
  {
    id: 4,
    title: "Fourier Series Drawing",
    description: "Complex shapes emerge from rotating circles",
    video: "/videos/FourierEpicyclesAnimated.mp4",
    category: "Calculus",
    formula: "f(t) = \\sum_{n=1}^{\\infty} A_n \\sin(n\\omega t + \\phi_n)",
    explanation:
      "Any periodic function can be represented as a sum of sine and cosine waves. Each rotating circle represents a frequency component in the Fourier decomposition.",
    mathConcept: "Fourier Analysis",
  },
  {
    id: 5,
    title: "Double Pendulum",
    description: "Three pendulums diverge showing sensitive dependence",
    video: "/videos/DoublePendulumChaos.mp4",
    category: "Physics",
    formula: "m\\ell^2\\ddot{\\theta} + mg\\ell\\sin(\\theta) = 0",
    explanation:
      "Three double pendulums with nearly identical starting positions quickly diverge due to chaotic dynamics. Small differences amplify exponentially over time.",
    mathConcept: "Nonlinear Dynamics",
  },
  {
    id: 6,
    title: "Bubble Sort",
    description: "Step-by-step visualization of sorting algorithm",
    video: "/videos/SortingVisualization.mp4",
    category: "Computer Science",
    formula: "T(n) = O(n^2)",
    explanation:
      "Bubble sort compares adjacent elements and swaps them if they are in the wrong order. The algorithm has quadratic time complexity in the worst and average case.",
    mathConcept: "Algorithm Complexity",
  },
  {
    id: 7,
    title: "Fibonacci Spiral",
    description: "Golden ratio rectangles forming the iconic sequence",
    video: "/videos/FibonacciSpiral.mp4",
    category: "Number Theory",
    formula: "F_n = F_{n-1} + F_{n-2}, \\quad \\phi = \\frac{1+\\sqrt{5}}{2}",
    explanation:
      "The Fibonacci sequence appears throughout nature. The ratio of consecutive terms converges to the golden ratio φ ≈ 1.618.",
    mathConcept: "Recursive Sequences",
  },
  {
    id: 8,
    title: "Fluid Particles",
    description:
      "Wave propagation through a particle grid with spiral dynamics",
    video: "/videos/FluidParticles.mp4",
    category: "Physics",
    formula: "\\nabla^2 \\phi = \\frac{\\partial^2 \\phi}{\\partial t^2}",
    explanation:
      "Particles follow wave equations creating interference patterns. The spiral motion emerges from radial displacement functions.",
    mathConcept: "Wave Equations",
  },
  {
    id: 9,
    title: "Wave Interference",
    description: "Two sine waves combining through constructive interference",
    video: "/videos/WaveInterference.mp4",
    category: "Physics",
    formula: "y(x,t) = A_1\\sin(kx-\\omega t) + A_2\\sin(kx-\\omega t + \\phi)",
    explanation:
      "When two waves overlap, their amplitudes add. Constructive interference occurs when waves are in phase, destructive when out of phase.",
    mathConcept: "Superposition Principle",
  },
  {
    id: 10,
    title: "Geometric Transformations",
    description: "Morphing shapes from triangles to circles",
    video: "/videos/GeometricTransformations.mp4",
    category: "Geometry",
    formula: "\\lim_{n \\to \\infty} P_n = \\text{Circle}",
    explanation:
      "As the number of sides increases, regular polygons approach a circle. This demonstrates the concept of limits in geometry.",
    mathConcept: "Limits & Continuity",
  },
  {
    id: 11,
    title: "Vector Field Flow",
    description: "Flowing particles in a circular vector field",
    video: "/videos/VectorFieldFlowEnhanced.mp4",
    category: "Vector Calculus",
    formula: "\\vec{F}(x,y) = (-y, x)",
    explanation:
      "This vector field represents rotational flow. Particles follow the vector field lines, creating beautiful spiral trajectories.",
    mathConcept: "Vector Fields & Curl",
  },
];

function AnimationCard({ animation, onClick }) {
  const [isPlaying, setIsPlaying] = useState(false);
  const isAI = animation.category === "AI & Machine Learning";

  return (
    <div
      className={`animation-card ${isAI ? "ai-card" : ""}`}
      onClick={onClick}
    >
      <div className="video-container">
        <video
          src={animation.video}
          loop
          muted
          playsInline
          onMouseEnter={(e) => {
            e.target.play();
            setIsPlaying(true);
          }}
          onMouseLeave={(e) => {
            e.target.pause();
            e.target.currentTime = 0;
            setIsPlaying(false);
          }}
          className={isPlaying ? "playing" : ""}
        />
        <div className="category-badge">{animation.category}</div>
      </div>
      <div className="card-content">
        <h3>{animation.title}</h3>
        <p>{animation.description}</p>
      </div>
    </div>
  );
}

function AnimationModal({ animation, onClose }) {
  const [playbackRate, setPlaybackRate] = useState(1);
  const [isPlaying, setIsPlaying] = useState(true);
  const [showPlayIcon, setShowPlayIcon] = useState(false);
  const videoRef = useState(null)[1];

  const handlePlaybackChange = (rate) => {
    setPlaybackRate(rate);
    const video = document.querySelector(".modal-video");
    if (video) {
      video.playbackRate = rate;
    }
  };

  const togglePlayPause = () => {
    const video = document.querySelector(".modal-video");
    if (video) {
      if (video.paused) {
        video.play();
        setIsPlaying(true);
      } else {
        video.pause();
        setIsPlaying(false);
      }
      // Show icon briefly
      setShowPlayIcon(true);
      setTimeout(() => setShowPlayIcon(false), 600);
    }
  };

  if (!animation) return null;

  return (
    <div className="modal-overlay" onClick={onClose}>
      <div className="modal-content" onClick={(e) => e.stopPropagation()}>
        <button className="modal-close" onClick={onClose}>
          ×
        </button>

        <div className="modal-layout">
          {/* Left side - Video */}
          <div className="modal-left">
            <div className="modal-video-container" onClick={togglePlayPause}>
              <video
                ref={videoRef}
                src={animation.video}
                className="modal-video"
                autoPlay
                loop
                muted
                playsInline
              />
              <div
                className={`play-pause-indicator ${showPlayIcon ? "show" : ""}`}
              >
                {isPlaying ? (
                  <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M6 4h4v16H6V4zm8 0h4v16h-4V4z" />
                  </svg>
                ) : (
                  <svg viewBox="0 0 24 24" fill="currentColor">
                    <path d="M8 5v14l11-7z" />
                  </svg>
                )}
              </div>
            </div>

            <div className="modal-controls">
              <label>Speed:</label>
              <div className="speed-buttons">
                {[0.5, 0.75, 1, 1.5, 2].map((rate) => (
                  <button
                    key={rate}
                    className={playbackRate === rate ? "active" : ""}
                    onClick={() => handlePlaybackChange(rate)}
                  >
                    {rate}x
                  </button>
                ))}
              </div>
            </div>
          </div>

          {/* Right side - Info */}
          <div className="modal-right">
            <h2>{animation.title}</h2>
            <div className="category-pill">{animation.category}</div>

            <div className="math-section">
              <h3>Formula</h3>
              <div className="formula-box">
                <BlockMath math={animation.formula} />
              </div>
            </div>

            <div className="explanation-section">
              <h3>Explanation</h3>
              <p>{animation.explanation}</p>
            </div>

            <div className="concept-section">
              <h3>Key Concept</h3>
              <p className="concept-highlight">{animation.mathConcept}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

function App() {
  const [selectedAnimation, setSelectedAnimation] = useState(null);

  // Separate AI and non-AI animations
  const aiAnimations = animations.filter(
    (a) => a.category === "AI & Machine Learning"
  );
  const mathAnimations = animations.filter(
    (a) => a.category !== "AI & Machine Learning"
  );

  return (
    <div className="app">
      <header className="header">
        <h1 className="title">
          <span className="gradient-text">AI in Motion</span>
        </h1>
      </header>

      <main className="main">
        {/* AI & Machine Learning Section */}
        <section className="animation-section">
          <div className="section-header-wrapper">
            <h2 className="section-header">
              <RiRobot2Line className="section-icon" />
              <span>AI & Machine Learning</span>
            </h2>
            <div className="section-line"></div>
          </div>
          <div className="animations-grid">
            {aiAnimations.map((animation, index) => (
              <AnimationCard
                key={animation.id}
                animation={animation}
                onClick={() => setSelectedAnimation(animation)}
                style={{ "--card-index": index }}
              />
            ))}
          </div>
        </section>

        {/* Mathematics Section */}
        <section className="animation-section">
          <div className="section-header-wrapper">
            <h2 className="section-header">
              <RiFunctionLine className="section-icon" />
              <span>Mathematics & Physics</span>
            </h2>
            <div className="section-line"></div>
          </div>
          <div className="animations-grid">
            {mathAnimations.map((animation, index) => (
              <AnimationCard
                key={animation.id}
                animation={animation}
                onClick={() => setSelectedAnimation(animation)}
                style={{ "--card-index": index }}
              />
            ))}
          </div>
        </section>
      </main>

      <footer className="footer">
        <p>Created with Manim • By Samuel and his team of Agents ッ</p>
      </footer>

      {selectedAnimation && (
        <AnimationModal
          animation={selectedAnimation}
          onClose={() => setSelectedAnimation(null)}
        />
      )}
    </div>
  );
}

export default App;
