# Mathematical Animations

Interactive visualizations of mathematics and AI concepts, built with **Manim** and **React**.

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python](https://img.shields.io/badge/python-3.13-blue.svg)
![React](https://img.shields.io/badge/react-19.2.0-61dafb.svg)

## 🎯 Overview

This project uses a **dual-pipeline architecture**:
- **Generation Pipeline** (`manimations/`) - Python scripts using [Manim Community](https://www.manim.community/) to programmatically generate mathematical animations
- **Showcase Webapp** (`webapp/`) - Interactive React gallery for browsing and learning from the animations

Together, they create an educational platform featuring **17 high-quality animations** covering topics from AI/ML to fractals, chaos theory, and calculus.

### ✨ Features

- **6 AI & Machine Learning Animations**: Attention mechanisms, neural networks, gradient descent, vector embeddings, context windows, and temperature sampling
- **11 Mathematics & Physics Animations**: Fractals, chaos theory, Fourier analysis, vector fields, and more
- **Interactive Webapp**: Click any animation to view detailed explanations with LaTeX formulas
- **High-Quality Renders**: All animations rendered at 1080p60 using Manim
- **Responsive Design**: Beautiful dark theme with smooth animations and hover effects
- **Educational Content**: Each visualization includes detailed mathematical explanations
- **Open Source**: Full Python source code for generating every animation

## 🏗️ Project Architecture

This is **not** a traditional web app with backend/frontend. Instead:

```
math-visual/
├── manimations/           # Animation Generation Pipeline (Python + Manim)
│   ├── ai_visual_simple.py      # Generate AI/ML animations
│   ├── animations.py             # Generate core math animations  
│   ├── stunning_animations.py   # Generate advanced visualizations
│   └── media/                    # Rendered outputs (gitignored)
│
└── webapp/                # Showcase Application (React)
    ├── src/App.jsx              # Animation gallery + modal viewer
    ├── public/videos/           # Deployed video files
    └── dist/                     # Production build (gitignored)
```

**The Flow:**
1. Write Python → Generate animations with Manim → Export MP4s
2. Copy videos → Webapp public folder → Add metadata to gallery
3. Users browse webapp → Watch animations → Learn concepts

## 🎨 Animation Categories

### AI & Machine Learning (6 animations)
1. **Attention Mechanism** - Transformer self-attention visualization with query/key/value matrices
2. **Neural Network Activation** - Forward propagation through layers with ReLU activation
3. **Gradient Descent** - Optimization algorithm finding minimum loss on a loss surface
4. **Vector Embeddings** - Semantic similarity in vector space (RAG concept)
5. **Context Window** - LLM conversation memory management with token limits
6. **Temperature Sampling** - Controlling LLM creativity vs determinism in text generation

### Mathematics & Physics (11 animations)
- **Fractals**: Fractal Tree, Mandelbrot Set visualization, Mandelbrot Zoom
- **Chaos Theory**: Lorenz Attractor, Double Pendulum
- **Fourier Analysis**: Fourier Circles, Fourier Epicycles, Fourier Series Drawing
- **Physics**: Wave Interference, Particle System, Fluid Particles
- **Calculus**: Vector Field, Vector Field Flow, Geometric Transformations
- **Number Theory**: Fibonacci Spiral, Sorting Visualization

## 🚀 Getting Started

### Prerequisites

- **Python 3.13+** with `uv` or `pip`
- **Node.js 18+** with `pnpm` (or npm)
- **FFmpeg** (for Manim video rendering)

### Installation

#### 1. Clone the Repository

```bash
git clone https://github.com/peltomaaa/math-visual.git
cd math-visual
```

#### 2. Set Up Manim Environment

```bash
cd manimations

# Create virtual environment
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

# Install dependencies
pip install manim

# Verify installation
manim --version
```

#### 3. Set Up Webapp

```bash
cd ../webapp

# Install dependencies
pnpm install  # or: npm install

# Start development server
pnpm dev  # or: npm run dev
```

The webapp will be available at `http://localhost:5173`

## 📁 Project Structure

```text
math-visual/
├── manimations/              # Animation Generation Pipeline
│   ├── ai_visual_simple.py   # AI/ML animations (6 scenes)
│   ├── animations.py         # Core math animations
│   ├── improved_animations.py
│   ├── stunning_animations.py
│   ├── .venv/               # Python virtual environment
│   └── media/               # Rendered video outputs (gitignored)
│       └── videos/
│           └── */1080p60/   # High-quality MP4 files
│
├── webapp/                  # Showcase Application
│   ├── src/
│   │   ├── App.jsx          # Main component with animations data
│   │   ├── App.css          # Styling and animations
│   │   └── main.jsx         # Entry point
│   ├── public/
│   │   └── videos/          # Deployed animation videos
│   └── package.json
│
├── docs/                    # Documentation
│   ├── ARCHITECTURE.md      # Detailed architecture explanation
│   ├── CONTRIBUTING.md      # Contribution guidelines
│   ├── GIT_STRATEGY.md      # Git workflow & what to commit
│   └── GITHUB_ENHANCEMENTS.md  # Repository improvement ideas
│
├── README.md
└── BACKLOG.md              # Issue tracker & planned features
```

## 🎬 Creating New Animations

### 1. Write the Manim Scene

Add your scene to `manimations/ai_visual_simple.py` or create a new file:

```python
from manim import *

class MyAnimation(Scene):
    def construct(self):
        title = Text("My Animation", font_size=48, color=BLUE_B, font="Sans")
        self.play(Write(title))
        self.wait(1)
```

### 2. Render the Animation

```bash
cd manimations
source .venv/bin/activate

# Render at 1080p60 (high quality)
manim -qh your_file.py MyAnimation

# Output will be in: media/videos/your_file/1080p60/MyAnimation.mp4
```

### 3. Copy to Webapp

```bash
cp media/videos/your_file/1080p60/MyAnimation.mp4 ../webapp/public/videos/
```

### 4. Add to React App

Edit `webapp/src/App.jsx` and add your animation to the `animations` array:

```javascript
{
  id: 18,
  title: "My Animation",
  description: "Short description for card",
  video: "/videos/MyAnimation.mp4",
  category: "AI & Machine Learning", // or other category
  formula: "E = mc^2", // LaTeX formula
  explanation: "Detailed explanation...",
  mathConcept: "Key Concept Name",
}
```

## 🛠️ Tech Stack

### Animation Generation

- **Manim Community** - Mathematical animation framework
- **Python 3.13** - Programming language
- **FFmpeg** - Video encoding

### Showcase Webapp

- **React 19.2** - UI framework
- **Vite 7.1** - Build tool and dev server
- **React-KaTeX** - LaTeX formula rendering
- **React-Icons** - Icon library
- **CSS3** - Styling with modern features

## 📝 Development Workflow

### Adding Animations

1. Write Manim scene in `manimations/`
2. Test render: `manim -ql scene.py SceneName` (low quality, faster)
3. Final render: `manim -qh scene.py SceneName` (1080p60)
4. Copy MP4 to `webapp/public/videos/`
5. Add metadata to `webapp/src/App.jsx`

### Webapp Development

1. Run dev server: `pnpm dev`
2. Edit components in `src/`
3. Hot reload reflects changes instantly
4. Build for production: `pnpm build`

## 🎯 Best Practices

### Manim Animations

- Always specify `font="Sans"` for Text objects (prevents letter spacing issues)
- Keep labels short and simple (detailed explanations go in React UI)
- Use `font_size=18-24` for readable labels at 1080p
- Render at `-qh` (1080p60) for final version
- Test with `-ql` (480p15) during development for faster iteration

### React Integration

- Provide detailed explanations (200-300 words) in the `explanation` field
- Include LaTeX formulas showing key mathematical concepts
- Use descriptive titles and concise descriptions
- Maintain consistent ID numbering

## � Documentation

- **[ARCHITECTURE.md](./docs/ARCHITECTURE.md)** - Deep dive into the dual-pipeline architecture
- **[CONTRIBUTING.md](./docs/CONTRIBUTING.md)** - How to contribute animations or improve the webapp
- **[GIT_STRATEGY.md](./docs/GIT_STRATEGY.md)** - What files to commit and why
- **[GITHUB_ENHANCEMENTS.md](./docs/GITHUB_ENHANCEMENTS.md)** - Ideas for improving this repository
- **[BACKLOG.md](./BACKLOG.md)** - Known issues and planned features

## � License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🙏 Acknowledgments

- [Manim Community](https://www.manim.community/) - Amazing mathematical animation framework
- [3Blue1Brown](https://www.3blue1brown.com/) - Inspiration for mathematical visualizations

## 🔗 Links

- **Manim Docs**: https://docs.manim.community/
- **React Docs**: https://react.dev/

---

Made with ❤️ and mathematics

