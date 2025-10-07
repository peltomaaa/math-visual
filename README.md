# Mathematical Animations

A beautiful showcase of mathematical concepts through animated visualizations, powered by [Manim](https://www.manim.community/) and React.

![Mathematical Animations](https://img.shields.io/badge/Manim-Community-blue)
![React](https://img.shields.io/badge/React-18-61dafb)
![Vite](https://img.shields.io/badge/Vite-7-646cff)

## ✨ Features

- **6 Unique Mathematical Animations** - From fractals to fluid dynamics
- **Interactive Playback** - Hover over cards to play animations
- **Sleek Dark UI** - Modern, minimalist design with gradient accents
- **Fully Responsive** - Works seamlessly on desktop and mobile
- **Fast Performance** - Built with Vite for lightning-fast development

## 🎨 Animations Showcase

| Animation | Category | Description |
|-----------|----------|-------------|
| **Fractal Tree** | Fractals | Recursive branching structure with natural patterns |
| **Fluid Particles** | Physics | Wave propagation through particle grid |
| **Fibonacci Spiral** | Number Theory | Golden ratio rectangles sequence |
| **Wave Interference** | Physics | Sine waves combining constructively |
| **Geometric Transformations** | Geometry | Morphing polygons to circles |
| **Vector Field** | Vector Calculus | Circular flow visualization |

## 🚀 Quick Start

### Prerequisites

- Python 3.13+
- Node.js 18+
- [uv](https://github.com/astral-sh/uv) (Python package manager)
- [Manim dependencies](https://docs.manim.community/en/stable/installation.html)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/math-visual.git
   cd math-visual
   ```

2. **Set up Manim environment**
   ```bash
   cd manimations
   uv sync
   ```

3. **Install frontend dependencies**
   ```bash
   cd ../frontend
   npm install
   ```

4. **Start the development server**
   ```bash
   npm run dev
   ```

5. Open [http://localhost:5173](http://localhost:5173)

## 📁 Project Structure

```
math-visual/
├── manimations/          # Python Manim animations
│   ├── animations.py     # Core animation scenes
│   ├── advanced_animations.py
│   └── media/           # Rendered video outputs
│
├── frontend/            # React frontend
│   ├── src/
│   │   ├── App.jsx     # Main application
│   │   ├── App.css     # Styling
│   │   └── main.jsx
│   ├── public/
│   │   └── videos/     # Animation video files
│   └── package.json
│
└── README.md
```

## 🎬 Creating New Animations

1. **Write a Manim scene** in `manimations/animations.py`:
   ```python
   from manim import *

   class MyAnimation(Scene):
       def construct(self):
           circle = Circle()
           self.play(Create(circle))
   ```

2. **Render the animation**:
   ```bash
   cd manimations
   uv run manim -qm animations.py MyAnimation
   ```

3. **Copy to frontend**:
   ```bash
   cp media/videos/animations/720p30/MyAnimation.mp4 ../frontend/public/videos/
   ```

4. **Add to React app** in `frontend/src/App.jsx`:
   ```javascript
   {
     id: 7,
     title: 'My Animation',
     description: 'Description here',
     video: '/videos/MyAnimation.mp4',
     category: 'Category'
   }
   ```

## 🛠️ Tech Stack

### Animations
- **Manim Community** - Mathematical animation engine
- **Python 3.13** - Programming language
- **NumPy** - Numerical computations
- **Cairo** - Graphics library

### Frontend
- **React 18** - UI framework
- **Vite 7** - Build tool
- **CSS3** - Styling with custom properties

## 📸 Screenshots

> Interactive cards with hover-to-play animations

> Gradient text header with sleek minimal design

> Responsive grid layout adapting to screen sizes

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-animation`)
3. Commit your changes (`git commit -m 'Add amazing animation'`)
4. Push to the branch (`git push origin feature/amazing-animation`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🙏 Acknowledgments

- [3Blue1Brown](https://www.3blue1brown.com/) - For creating Manim
- [Manim Community](https://www.manim.community/) - For maintaining the community edition
- All contributors and supporters

## 📧 Contact

For questions or suggestions, feel free to open an issue or reach out!

---

**Made with ❤️ using Manim & React**
