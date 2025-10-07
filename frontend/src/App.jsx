import { useState } from 'react'
import './App.css'

const animations = [
  {
    id: 1,
    title: 'Fractal Tree',
    description: 'Recursive branching structure showing natural fractal patterns',
    video: '/videos/FractalTree.mp4',
    category: 'Fractals'
  },
  {
    id: 2,
    title: 'Fluid Particles',
    description: 'Wave propagation through a particle grid with spiral dynamics',
    video: '/videos/FluidParticles.mp4',
    category: 'Physics'
  },
  {
    id: 3,
    title: 'Fibonacci Spiral',
    description: 'Golden ratio rectangles forming the iconic Fibonacci sequence',
    video: '/videos/FibonacciSpiral.mp4',
    category: 'Number Theory'
  },
  {
    id: 4,
    title: 'Wave Interference',
    description: 'Two sine waves combining through constructive interference',
    video: '/videos/WaveInterference.mp4',
    category: 'Physics'
  },
  {
    id: 5,
    title: 'Geometric Transformations',
    description: 'Morphing shapes from triangles to circles',
    video: '/videos/GeometricTransformations.mp4',
    category: 'Geometry'
  },
  {
    id: 6,
    title: 'Vector Field',
    description: 'Circular flow visualization of a 2D vector field',
    video: '/videos/VectorField.mp4',
    category: 'Vector Calculus'
  }
]

function AnimationCard({ animation }) {
  const [isPlaying, setIsPlaying] = useState(false)

  return (
    <div className="animation-card">
      <div className="video-container">
        <video
          src={animation.video}
          loop
          muted
          playsInline
          onMouseEnter={(e) => {
            e.target.play()
            setIsPlaying(true)
          }}
          onMouseLeave={(e) => {
            e.target.pause()
            e.target.currentTime = 0
            setIsPlaying(false)
          }}
          className={isPlaying ? 'playing' : ''}
        />
        <div className="category-badge">{animation.category}</div>
      </div>
      <div className="card-content">
        <h3>{animation.title}</h3>
        <p>{animation.description}</p>
      </div>
    </div>
  )
}

function App() {
  return (
    <div className="app">
      <header className="header">
        <h1 className="title">
          <span className="gradient-text">Mathematical</span> Animations
        </h1>
      </header>

      <main className="main">
        <div className="animations-grid">
          {animations.map((animation) => (
            <AnimationCard key={animation.id} animation={animation} />
          ))}
        </div>
      </main>

      <footer className="footer">
        <p>Created with Manim & React • Hover over animations to play</p>
      </footer>
    </div>
  )
}

export default App
