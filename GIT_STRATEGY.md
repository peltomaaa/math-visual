# Git Strategy

This document explains what files are tracked in version control and why.

## 🏗️ Project Architecture

This project uses a **dual-pipeline architecture**:

- **`manimations/`** - Generation pipeline (Python + Manim) that creates animations
- **`webapp/`** - Showcase application (React) that displays animations

The key insight: **Manim outputs are build artifacts** (like compiled code). We commit the source Python scripts, not the generated videos. The webapp gets pre-built videos for deployment.

## ✅ Files Included in Git

### Documentation
- `README.md` - Project overview
- `BACKLOG.md` - Issue tracker
- `CONTRIBUTING.md` - Contributor guide
- `LICENSE` - MIT license

### Manim Source Code
- `manimations/*.py` - All Python animation scripts
  - `ai_visual_simple.py` - AI/ML animations
  - `animations.py` - Core math animations
  - `improved_animations.py` - Enhanced visualizations
  - `stunning_animations.py` - Advanced animations
- `manimations/pyproject.toml` - Python dependencies
- `manimations/uv.lock` - Dependency lock file

### Webapp Application
- `webapp/src/` - React source code
  - `App.jsx` - Main component with animation data
  - `App.css` - Styling
  - `main.jsx` - Entry point
- `webapp/public/videos/` - **Deployed video files** (17 MP4s)
- `webapp/index.html` - HTML template
- `webapp/package.json` - Node dependencies
- `webapp/vite.config.js` - Build configuration

## ❌ Files Excluded from Git

### Manim Generated Files (Can be Regenerated)
- `manimations/media/` - **Entire directory ignored**
  - `media/videos/` - Rendered output videos
  - `media/images/` - Static image outputs
  - `media/Tex/` - LaTeX rendering cache
  - `media/texts/` - Text rendering cache
  - `partial_movie_files/` - Intermediate rendering frames

**Why excluded?** These are build artifacts generated from Python source. Anyone can regenerate them by running:
```bash
manim -qh ai_visual_simple.py ContextWindow
```

### Python Environment
- `manimations/.venv/` - Virtual environment
- `__pycache__/` - Python bytecode cache
- `*.pyc` - Compiled Python files

### Node Modules
- `webapp/node_modules/` - npm packages (10,000+ files)
- `webapp/pnpm-lock.yaml` - pnpm lock file (optional)
- `webapp/dist/` - Production build output

### OS & Editor Files
- `.DS_Store` - macOS metadata
- `.vscode/` - Editor settings (except extensions.json)
- `*.log` - Log files

## 📦 What Gets Deployed

### Production Webapp
When you run `pnpm build`, the webapp creates:
- Optimized JavaScript bundle
- Minified CSS
- Video files from `public/videos/`

These are deployed to a static host (Vercel, Netlify, etc.).

### Manim Videos
The workflow is:
1. Write Python animation → `ai_visual_simple.py`
2. Render locally → `media/videos/.../Animation.mp4`
3. Copy to webapp → `cp ... webapp/public/videos/`
4. Add metadata → Update `App.jsx`
5. Commit → **Only webapp video is tracked**

## 📊 Repository Size

**Without media files:** ~50 MB
- Python source: ~200 KB
- React code: ~500 KB  
- Webapp videos: ~40 MB (17 videos × 2-3 MB each)
- Dependencies (lock files): ~10 MB

**With media files (if not ignored):** ~500+ MB
- All Manim output directories
- Tex/Text caches
- Partial movie files

## 🎯 Benefits of This Strategy

1. **Faster Clones** - New contributors don't download gigabytes of generated files
2. **Smaller Diffs** - Only source code changes tracked, not binary video re-renders
3. **Reproducible** - Anyone can regenerate Manim outputs from source
4. **Clean History** - No accidentally committed huge media files

## 🔄 When to Update Videos

If you modify a Manim animation:

```bash
# 1. Edit the Python
vim manimations/ai_visual_simple.py

# 2. Re-render
cd manimations
manim -qh ai_visual_simple.py YourAnimation

# 3. Copy to webapp (overwrites old version)
cp media/videos/ai_visual_simple/1080p60/YourAnimation.mp4 ../webapp/public/videos/

# 4. Git will detect the change
git status
# Shows: modified: webapp/public/videos/YourAnimation.mp4

# 5. Commit
git add webapp/public/videos/YourAnimation.mp4
git commit -m "Update: Re-rendered YourAnimation with fixes"
```

## 🚨 Important Notes

- **Never commit** `manimations/media/` - It's in `.gitignore` for a reason
- **Do commit** `webapp/public/videos/*.mp4` - These are part of the deployed app
- If someone needs source renderings, they can regenerate from `.py` files
- Lock files (`package-lock.json`, `uv.lock`) should be committed for reproducibility

## 📝 Current Git Status

As of last check, the repository tracks:
- 7 modified files (docs, webapp code)
- 27 new files (new docs, videos, Python scripts)
- 0 media generation artifacts (successfully ignored)

---

*This strategy balances between keeping the repository lean and ensuring the deployed webapp has all necessary assets.*
