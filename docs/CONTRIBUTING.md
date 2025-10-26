# Contributing Guide

Thank you for your interest in contributing to Mathematical Animations! This guide will help you get started.

## 🎯 Project Structure

This project uses a **dual-pipeline architecture**:

- **`manimations/`** - Python scripts that **generate** animations using Manim
- **`webapp/`** - React application that **showcases** the animations

You don't need to work on both parts - you can contribute animations without touching the webapp, or improve the UI without generating new animations!

**Read more:** [ARCHITECTURE.md](./ARCHITECTURE.md) for a deep dive into the dual-pipeline design.

## 🚀 Quick Start for Contributors

### Setting Up Your Development Environment

1. **Fork and clone the repository**

   ```bash
   git clone https://github.com/YOUR_USERNAME/math-visual.git
   cd math-visual
   ```

2. **Set up the Manim environment**

   ```bash
   cd manimations
   python -m venv .venv
   source .venv/bin/activate  # Windows: .venv\Scripts\activate
   pip install manim
   ```

3. **Set up the webapp**

   ```bash
   cd ../webapp
   pnpm install  # or: npm install
   ```

4. **Start developing!**

   ```bash
   pnpm dev  # Webapp runs on localhost:5173
   ```

## 🎨 Adding a New Animation

### Step 1: Create the Manim Scene

Choose the appropriate file in `manimations/`:
- `ai_visual_simple.py` - For AI/ML concepts
- `animations.py` - For core math concepts
- Create a new file for new categories

Example animation:

```python
from manim import *

class MyNewConcept(Scene):
    def construct(self):
        # IMPORTANT: Always use font="Sans" to avoid letter spacing issues
        title = Text("My Concept", font_size=48, color=BLUE_B, font="Sans")
        
        # Keep labels short and simple
        label = Text("Simple Label", font_size=20, font="Sans")
        
        # Create your animation
        self.play(Write(title))
        self.wait(1)
        
        # Clean up
        self.play(FadeOut(title))
```

### Step 2: Test Your Animation

Start with low quality for fast iteration:

```bash
cd manimations
source .venv/bin/activate

# Low quality, fast render (480p15)
manim -ql your_file.py MyNewConcept

# Preview the output
open media/videos/your_file/480p15/MyNewConcept.mp4
```

### Step 3: Final Render

When satisfied, render at high quality:

```bash
# High quality (1080p60)
manim -qh your_file.py MyNewConcept
```

### Step 4: Copy to Webapp

```bash
cp media/videos/your_file/1080p60/MyNewConcept.mp4 ../webapp/public/videos/
```

### Step 5: Add to React App

Edit `webapp/src/App.jsx` and add to the `animations` array:

```javascript
{
  id: 18, // Next available ID
  title: "My New Concept",
  description: "Brief description for the card (1-2 sentences)",
  video: "/videos/MyNewConcept.mp4",
  category: "AI & Machine Learning", // or "Mathematics & Physics"
  
  // LaTeX formula - use \\ for backslashes
  formula: "f(x) = \\frac{1}{1 + e^{-x}}",
  
  // Detailed explanation (200-300 words)
  explanation: "This animation demonstrates... [detailed explanation with context, applications, and significance]",
  
  // Key mathematical concept
  mathConcept: "Sigmoid Function",
}
```

## 📝 Code Style Guidelines

### Manim (Python)

```python
# DO:
- Always use font="Sans" for Text objects
- Keep labels concise and readable
- Use descriptive class names (e.g., GradientDescent, not GD)
- Add comments explaining non-obvious mathematical concepts
- Use consistent color schemes (BLUE_B, GREEN_C, RED_C, etc.)
- Font sizes: 48 for titles, 20-24 for labels

# DON'T:
- Use default Text() without font parameter
- Create overly complex animations (keep to 10-15 seconds)
- Use Greek symbols that may not render well (α, β, etc.)
- Overlap labels with axes or other elements
```

### React (JavaScript)

```javascript
// DO:
- Use functional components with hooks
- Keep components simple and focused
- Use semantic HTML elements
- Add descriptive comments for complex logic
- Follow existing code structure

// DON'T:
- Introduce new dependencies without discussion
- Modify core styling without testing responsiveness
- Remove existing features
```

### CSS

```css
/* DO: */
- Use CSS custom properties (variables)
- Follow existing naming conventions
- Test on multiple screen sizes
- Use flexbox/grid for layouts
- Add comments for complex selectors

/* DON'T: */
- Use !important unless absolutely necessary
- Add vendor prefixes manually (Vite handles this)
- Remove existing responsive breakpoints
```

## 🎯 Best Practices

### Animation Design

1. **Start Simple**: Begin with basic shapes and movements
2. **Add Complexity Gradually**: Build up the visualization step by step
3. **Use Color Meaningfully**: Different colors should represent different concepts
4. **Mind the Timing**: Use `self.wait()` to let viewers absorb information
5. **Test on Different Screens**: Ensure text is readable at various sizes

### Mathematical Accuracy

1. **Verify Formulas**: Double-check all mathematical notation
2. **Cite Sources**: If explaining a specific algorithm or concept
3. **Be Educational**: Explanations should teach, not just describe
4. **Provide Context**: Connect to real-world applications

### Performance

1. **Optimize File Sizes**: High quality is important, but so is load time
2. **Test Video Loading**: Ensure videos play smoothly
3. **Check Bundle Size**: Use `pnpm build` and check output size

## 🐛 Reporting Bugs

When reporting issues, please include:

1. **Clear Description**: What went wrong?
2. **Steps to Reproduce**: How can we see the bug?
3. **Expected Behavior**: What should happen?
4. **Screenshots/Videos**: Visual aids help immensely
5. **Environment**: OS, browser, Node/Python versions

## 💡 Suggesting Features

See [BACKLOG.md](./BACKLOG.md) for planned features. Before suggesting new ones:

1. Check if it's already in the backlog
2. Describe the use case and benefits
3. Consider implementation complexity
4. Be open to discussion and alternatives

## 🔄 Pull Request Process

1. **Create a Branch**

   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Your Changes**
   - Follow code style guidelines
   - Test thoroughly
   - Update documentation if needed

3. **Commit with Clear Messages**

   ```bash
   git commit -m "Add: Temperature Sampling animation"
   git commit -m "Fix: Letter spacing in labels"
   git commit -m "Docs: Update README with new animation"
   ```

4. **Push to Your Fork**

   ```bash
   git push origin feature/your-feature-name
   ```

5. **Open a Pull Request**
   - Describe what changed and why
   - Reference any related issues
   - Add screenshots/videos if UI changed
   - Wait for review and address feedback

## ✅ PR Checklist

Before submitting:

- [ ] Code follows existing style guidelines
- [ ] Animations render without errors
- [ ] Videos are copied to `webapp/public/videos/`
- [ ] Animation metadata added to `App.jsx`
- [ ] No console errors in browser
- [ ] Tested on desktop and mobile
- [ ] Documentation updated (if needed)
- [ ] Commit messages are clear

## 🎓 Learning Resources

### Manim

- [Official Documentation](https://docs.manim.community/)
- [Example Gallery](https://docs.manim.community/en/stable/examples.html)
- [3Blue1Brown's Channel](https://www.youtube.com/c/3blue1brown) - Inspiration

### React

- [Official Docs](https://react.dev/)
- [React Hooks Reference](https://react.dev/reference/react)

### Mathematical Concepts

- [Khan Academy](https://www.khanacademy.org/) - Math fundamentals
- [Brilliant.org](https://brilliant.org/) - Interactive learning
- [BetterExplained](https://betterexplained.com/) - Intuitive explanations

## 🤝 Community

- Be respectful and constructive
- Help others learn
- Share knowledge generously
- Celebrate contributions of all sizes

## 📞 Getting Help

- **Issues**: Open a GitHub issue for bugs or questions
- **Discussions**: Use GitHub Discussions for general questions
- **Documentation**: Check README.md and this guide first

---

Thank you for contributing to making mathematics more accessible and beautiful! 🎨📐

