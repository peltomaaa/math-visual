# Project Architecture

This document explains the unique structure of this project and how the two pipelines work together.

## 🎯 Core Concept

**This is NOT a traditional web application with backend/frontend.**

Instead, it's a **dual-pipeline system**:

1. **Generation Pipeline** (`manimations/`) - Creates animations programmatically
2. **Showcase Pipeline** (`webapp/`) - Displays animations interactively

Think of it like a **publishing workflow**: you write scripts that generate content, then publish that content through a webapp.

## 📐 Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                   Generation Pipeline                        │
│                    (manimations/)                            │
│                                                              │
│  Python Scripts          Manim Engine         Video Files   │
│  ┌─────────────┐       ┌────────────┐      ┌─────────────┐ │
│  │ai_visual_   │──────▶│  Render    │─────▶│ .mp4 files  │ │
│  │simple.py    │       │  1080p60   │      │ in media/   │ │
│  └─────────────┘       └────────────┘      └─────────────┘ │
│                                                   │          │
└───────────────────────────────────────────────────┼──────────┘
                                                    │
                                            Manual Copy
                                                    │
                                                    ▼
┌─────────────────────────────────────────────────────────────┐
│                    Showcase Pipeline                         │
│                       (webapp/)                              │
│                                                              │
│  Video Assets         React Gallery        User Browser    │
│  ┌─────────────┐    ┌──────────────┐    ┌───────────────┐ │
│  │ public/     │───▶│  App.jsx     │───▶│ Interactive   │ │
│  │ videos/     │    │  + metadata  │    │ experience    │ │
│  └─────────────┘    └──────────────┘    └───────────────┘ │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

## 🔄 The Workflow

### Creating a New Animation

```bash
# 1. GENERATION PIPELINE
cd manimations/

# Write Python code
vim ai_visual_simple.py

# Generate video locally
manim -qh ai_visual_simple.py MyAnimation
# Output: media/videos/ai_visual_simple/1080p60/MyAnimation.mp4

# 2. TRANSFER TO SHOWCASE
cp media/videos/ai_visual_simple/1080p60/MyAnimation.mp4 \
   ../webapp/public/videos/

# 3. SHOWCASE PIPELINE
cd ../webapp/

# Add metadata
vim src/App.jsx  # Add to animations array

# Preview locally
pnpm dev

# 4. DEPLOYMENT
pnpm build
# Deploy dist/ to static host (Vercel, Netlify, etc.)
```

### What Gets Committed to Git?

```
✅ manimations/*.py          # Source code (200 KB)
❌ manimations/media/        # Build artifacts (500+ MB)
✅ webapp/src/               # React source (500 KB)
✅ webapp/public/videos/     # Deployed assets (40 MB)
❌ webapp/node_modules/      # Dependencies (200+ MB)
```

**Why?** The Python scripts are the **source of truth**. Anyone can regenerate videos. But the webapp needs pre-built videos for deployment.

## 🏗️ Directory Structure Deep Dive

### Generation Pipeline (`manimations/`)

```
manimations/
├── ai_visual_simple.py       # 6 AI/ML animation classes
├── animations.py              # Core math animations
├── improved_animations.py    # Enhanced versions
├── stunning_animations.py    # Advanced visualizations
├── pyproject.toml            # Python dependencies (manim, numpy)
├── .venv/                    # Virtual environment (gitignored)
└── media/                    # Generated outputs (gitignored)
    ├── videos/
    │   └── ai_visual_simple/
    │       └── 1080p60/
    │           ├── ContextWindow.mp4
    │           ├── GradientDescent.mp4
    │           └── ...
    ├── Tex/                  # LaTeX render cache
    └── texts/                # Text render cache
```

**Key Technologies:**
- **Manim Community** - Animation framework
- **Python 3.13** - Programming language
- **NumPy** - Mathematical computations
- **FFmpeg** - Video encoding

### Showcase Pipeline (`webapp/`)

```
webapp/
├── src/
│   ├── App.jsx               # Main component
│   │   ├── animations[]      # Metadata array (17 entries)
│   │   ├── Modal component   # Video player
│   │   └── Gallery grid      # Card layout
│   ├── App.css               # Dark theme styling
│   └── main.jsx              # React entry point
├── public/
│   └── videos/               # Deployed MP4 files
│       ├── ContextWindow.mp4
│       ├── GradientDescent.mp4
│       └── ... (17 total)
├── index.html                # HTML shell
├── package.json              # Dependencies (React, KaTeX, icons)
└── vite.config.js            # Build configuration
```

**Key Technologies:**
- **React 19.2** - UI framework
- **Vite 7.1** - Build tool
- **React-KaTeX** - Math formula rendering
- **React-Icons** - Icon library

## 🔑 Key Design Decisions

### Why Two Separate Pipelines?

1. **Separation of Concerns**
   - Generation is compute-intensive, done once
   - Showcase is lightweight, delivered to users

2. **Different Skillsets**
   - Python developers can contribute animations
   - Web developers can improve UI/UX
   - No need to know both!

3. **Independent Scaling**
   - Generate animations on powerful local machine
   - Deploy webapp to CDN for global distribution

4. **Version Control Efficiency**
   - Track Python source (small, text)
   - Don't track video renders (large, binary)
   - Webapp gets committed videos (needed for deployment)

### Why Manual Copy Instead of Automation?

**Considered approaches:**

❌ **Automated Pipeline**: Generate → Copy → Update metadata
- Adds complexity
- Requires build scripts
- Harder to debug

❌ **On-Demand Generation**: Generate videos in production
- Too slow (Manim takes minutes per video)
- Requires Python environment in deployment
- Unreliable (dependencies, FFmpeg)

✅ **Manual Copy** (Current approach):
- Simple and transparent
- Developer controls when videos update
- Pre-built videos = fast webapp loading
- Git tracks exactly what's deployed

### Why Keep Videos in Git?

**Debate:** Should `webapp/public/videos/` be gitignored?

**Pros of tracking:**
- ✅ Complete deployable package
- ✅ Easy clone-and-deploy for contributors
- ✅ Git history shows video updates
- ✅ No build step needed for webapp

**Cons:**
- ❌ Large files (but only 40 MB for 17 videos)
- ❌ Binary diffs (but rarely change)

**Decision:** Track them. 40 MB is acceptable, and it makes deployment dead simple.

## 🚀 Deployment Strategies

### Option 1: Static Hosting (Recommended)

**Platforms:** Vercel, Netlify, Cloudflare Pages

```bash
cd webapp/
pnpm build
# Upload dist/ folder
```

**Pros:**
- Free tier available
- Automatic HTTPS
- Global CDN
- Zero configuration

### Option 2: GitHub Pages

```bash
cd webapp/
pnpm build
# Configure base path in vite.config.js
# Push dist/ to gh-pages branch
```

### Option 3: Self-Hosted

```bash
cd webapp/
pnpm build
# Deploy dist/ to nginx/apache
```

## 🔄 Development Modes

### Animation Development

```bash
# Work only in manimations/
cd manimations/
source .venv/bin/activate

# Edit Python
vim ai_visual_simple.py

# Quick test (480p15)
manim -ql ai_visual_simple.py MyAnimation

# Final render (1080p60)
manim -qh ai_visual_simple.py MyAnimation

# Preview video
open media/videos/.../MyAnimation.mp4
```

**You don't need to run the webapp to work on animations!**

### Webapp Development

```bash
# Work only in webapp/
cd webapp/

# Start dev server
pnpm dev

# Edit React
vim src/App.jsx

# See changes instantly
```

**You don't need Python/Manim to work on the webapp!**

### Full-Stack Development

```bash
# Terminal 1: Animation generation
cd manimations/
source .venv/bin/activate
manim -ql ai_visual_simple.py MyAnimation

# Terminal 2: Webapp preview
cd webapp/
pnpm dev

# After rendering:
cp manimations/media/videos/.../MyAnimation.mp4 webapp/public/videos/
# Refresh browser
```

## 📊 Performance Characteristics

### Generation Pipeline

- **Render Time**: 30 seconds to 5 minutes per animation
- **CPU Usage**: High (Manim is compute-intensive)
- **Output Size**: 2-4 MB per video (1080p60, 10-15 seconds)
- **Frequency**: Rarely (only when improving animations)

### Showcase Pipeline

- **Build Time**: 5-10 seconds
- **Bundle Size**: ~500 KB (JS + CSS)
- **Page Load**: < 1 second (before videos)
- **Video Streaming**: Progressive (HTML5 video element)

## 🎨 Why This Architecture Works

1. **Manim is for creation, not delivery**
   - Perfect for programmatic animation generation
   - Not suitable for real-time rendering in browsers

2. **React is for presentation, not computation**
   - Excellent for interactive galleries
   - Not designed for heavy video rendering

3. **Videos are the bridge**
   - Standard format (MP4)
   - Works everywhere (browsers, mobile, desktop)
   - Good quality/size tradeoff

4. **Git manages both intelligently**
   - Source code: Small, text, version well
   - Deployed assets: Moderate size, needed for production
   - Build artifacts: Excluded (too large, regeneratable)

## 🔮 Future Considerations

### Potential Enhancements

1. **Automation**: Script to copy videos and update metadata
2. **CI/CD**: GitHub Actions to render on push
3. **CDN**: Offload videos to dedicated video hosting
4. **Database**: Store animation metadata in JSON file
5. **API**: Separate metadata from React code

### When to Split Further

If the project grows to 100+ animations:
- Move videos to external CDN (reduce git repo size)
- Generate metadata JSON automatically
- Consider separate content management system

For now (17 animations), current architecture is optimal.

---

**Philosophy:** Keep it simple until complexity is justified. Two pipelines, one repository, zero magic.
