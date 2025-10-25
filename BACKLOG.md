# Project Backlog

This document tracks known issues, planned improvements, and feature requests for the Mathematical Animations project.

---

## 🐛 Known Issues

### High Priority

#### AI-001: Context Window Animation Issues
**Status**: Open  
**Category**: Manim Animation  
**File**: `manimations/ai_visual_simple.py` - `ContextWindow` class

**Description**:  
The Context Window animation has some unspecified visual or technical issues that need investigation and fixing.

**Steps to Reproduce**:  
1. Render the animation: `manim -qh ai_visual_simple.py ContextWindow`
2. Review the output video

**Expected Behavior**:  
Animation should clearly demonstrate:
- Message bubbles sliding through the context window
- Token counter updating accurately
- Pruning behavior when limit is reached
- Smooth transitions between states

**Notes**:  
- Currently rendered at 1080p60
- Animation has 28 steps and runs for ~11 seconds
- Need to identify specific visual glitches or timing issues

---

#### AI-002: Temperature Sampling Animation Issues
**Status**: Open  
**Category**: Manim Animation  
**File**: `manimations/ai_visual_simple.py` - `TemperatureSampling` class

**Description**:  
The Temperature Sampling animation has some unspecified visual or technical issues that need investigation and fixing.

**Steps to Reproduce**:  
1. Render the animation: `manim -qh ai_visual_simple.py TemperatureSampling`
2. Review the output video

**Expected Behavior**:  
Animation should clearly demonstrate:
- Three temperature scenarios (0.1, 0.7, 1.5)
- Probability distributions shown as bar charts
- Visual differences between deterministic and creative outputs
- Smooth highlighting effects on selected words

**Notes**:  
- Currently rendered at 1080p60
- Animation has 32 steps and runs for ~13 seconds
- Need to identify specific visual glitches or timing issues

---

### Medium Priority

#### UI-003: Mobile Responsiveness Optimization
**Status**: Open  
**Category**: Frontend - CSS  
**File**: `webapp/src/App.css`

**Description**:  
While the app is responsive, there may be room for improvement on smaller mobile devices (< 375px width).

**Proposed Solution**:  
- Test on various device sizes
- Add additional breakpoint for very small screens
- Consider reducing padding/margins further
- Test modal behavior on mobile

---

#### UX-004: Animation Loading States
**Status**: Open  
**Category**: Frontend - React  
**File**: `webapp/src/App.jsx`

**Description**:  
Currently, there's no loading indicator when videos are buffering, which could lead to user confusion on slower connections.

**Proposed Solution**:  
- Add skeleton loaders or spinners for video cards
- Show loading state when modal video is buffering
- Consider lazy loading videos with Intersection Observer

---

#### A11Y-005: Accessibility Improvements
**Status**: Open  
**Category**: Frontend - Accessibility

**Description**:  
The app could benefit from enhanced accessibility features.

**Proposed Improvements**:  
- Add ARIA labels to video controls
- Ensure keyboard navigation works for modal
- Add focus trap in modal
- Improve color contrast ratios where needed
- Add skip-to-content link
- Test with screen readers

---

## ✨ Feature Requests

### High Priority

#### FEAT-006: Animation Search and Filter
**Status**: Planned  
**Category**: Frontend - Feature

**Description**:  
Add ability to search animations by title/description and filter by category or mathematical concept.

**Implementation Ideas**:  
- Add search input in header
- Add category filter buttons/dropdown
- Implement client-side filtering logic
- Add "Clear filters" button
- Show result count

**Benefits**:  
- Easier navigation with 17+ animations
- Better user experience for finding specific topics
- Scalable as more animations are added

---

#### FEAT-007: Animation Playlist Mode
**Status**: Idea  
**Category**: Frontend - Feature

**Description**:  
Allow users to queue multiple animations and watch them sequentially, like a playlist.

**Implementation Ideas**:  
- Add "Add to Playlist" button on each card
- Show playlist panel with queued animations
- Auto-advance to next animation when one finishes
- Allow reordering in playlist
- Save playlist to localStorage

**Benefits**:  
- Educational use case: create themed learning paths
- Better user engagement
- Reduces manual clicking

---

### Medium Priority

#### FEAT-008: Dark/Light Theme Toggle
**Status**: Idea  
**Category**: Frontend - UI

**Description**:  
Add theme toggle to switch between dark and light modes.

**Implementation Ideas**:  
- Add toggle button in header
- Define light theme CSS variables
- Save preference to localStorage
- Consider system preference detection (`prefers-color-scheme`)

**Notes**:  
- Current dark theme is well-designed
- Light theme would need careful color selection for readability
- Ensure animations look good in both themes

---

#### FEAT-009: Animation Download Feature
**Status**: Idea  
**Category**: Frontend - Feature

**Description**:  
Allow users to download animation MP4 files for offline viewing or educational use.

**Implementation Ideas**:  
- Add download button in modal
- Consider adding attribution/watermark option
- Add license information display
- Track download analytics (optional)

**Considerations**:  
- File sizes are large (1080p60 videos)
- May need to provide lower-quality versions
- Consider copyright/attribution requirements

---

#### FEAT-010: More AI Animations
**Status**: Planned  
**Category**: Manim Animation

**Description**:  
Create additional AI/ML concept animations to complement existing set.

**Potential Topics**:  
- Backpropagation step-by-step
- Convolutional Neural Networks (CNN) - filter sliding
- Recurrent Neural Networks (RNN) - sequence processing
- Dropout regularization
- Batch normalization
- Learning rate scheduling
- Transformer architecture overview
- Beam search decoding
- Reinforcement learning (Q-learning)
- Dimensionality reduction (PCA/t-SNE)

**Priority**:  
Start with most fundamental concepts, then advanced topics.

---

#### FEAT-011: Interactive Parameter Controls
**Status**: Idea  
**Category**: Frontend - Feature

**Description**:  
Allow users to adjust animation parameters and re-render in real-time.

**Implementation Ideas**:  
- Add sliders for key parameters (e.g., temperature in sampling)
- Use WebGL/Three.js for real-time rendering
- Or: Pre-render multiple versions and switch between them
- Show parameter values as they change

**Challenges**:  
- Real-time Manim rendering not feasible in browser
- Pre-rendering all combinations = huge file sizes
- May need to use different animation engine (Three.js, D3.js)

**Alternative**:  
Create simplified WebGL versions of select animations for interactivity.

---

## 🔧 Technical Debt

#### TECH-012: Refactor App.jsx Animations Data
**Status**: Open  
**Category**: Frontend - Code Quality  
**File**: `webapp/src/App.jsx`

**Description**:  
The `animations` array in App.jsx is getting large (17 items, 400+ lines). Consider extracting to separate data file.

**Proposed Solution**:  
- Create `src/data/animations.js`
- Export animations array from there
- Import in App.jsx
- Consider splitting by category

**Benefits**:  
- Better code organization
- Easier to maintain
- Could enable loading animations dynamically

---

#### TECH-013: Manim Code Duplication
**Status**: Open  
**Category**: Manim - Code Quality  
**Files**: `manimations/*.py`

**Description**:  
Multiple animation files have similar setup patterns and helper functions that could be extracted.

**Proposed Solution**:  
- Create `manimations/utils.py` with common helpers
- Extract shared text styling functions
- Create base classes for common animation patterns
- Standardize color schemes and fonts

**Benefits**:  
- DRY principle
- Easier to maintain consistent styling
- Faster to create new animations

---

#### TECH-014: Add Unit Tests
**Status**: Open  
**Category**: Testing

**Description**:  
Project currently has no automated tests.

**Proposed Tests**:  
- **Frontend**: Component rendering tests (React Testing Library)
- **Frontend**: Modal functionality tests
- **Frontend**: Animation data validation
- **Manim**: Test scenes render without errors
- **Manim**: Validate output file existence

**Tools**:  
- Vitest for webapp tests
- pytest for Python tests

---

## 📚 Documentation

#### DOC-015: Create CONTRIBUTING.md
**Status**: Planned  
**Category**: Documentation

**Description**:  
Add contributing guidelines for potential contributors.

**Should Include**:  
- Code style guidelines
- Commit message conventions
- PR process
- How to add new animations
- How to report bugs

---

#### DOC-016: Add Animation Creation Tutorial
**Status**: Planned  
**Category**: Documentation

**Description**:  
Create step-by-step tutorial for creating a new animation from scratch.

**Should Include**:  
- Manim basics for beginners
- Best practices for mathematical animations
- How to integrate with React app
- Troubleshooting common issues
- Example animation walkthrough

---

## 🚀 Performance

#### PERF-017: Optimize Video File Sizes
**Status**: Open  
**Category**: Performance

**Description**:  
1080p60 videos are large files. Consider optimization strategies.

**Proposed Solutions**:  
- Use more aggressive H.264 compression
- Provide multiple quality options (1080p, 720p, 480p)
- Lazy load videos only when needed
- Use video streaming instead of full download
- Consider WebM format as alternative

**Trade-offs**:  
- Smaller files = lower quality
- Multiple versions = more storage needed
- Streaming = more complex setup

---

#### PERF-018: Implement Code Splitting
**Status**: Open  
**Category**: Frontend - Performance  
**File**: `webapp/src/App.jsx`

**Description**:  
Currently, all code loads in single bundle. Consider splitting by route/feature.

**Proposed Solution**:  
- Use React.lazy() for modal component
- Split animations data if it gets larger
- Consider route-based code splitting if adding pages

**Benefits**:  
- Faster initial load time
- Better caching
- Smaller bundle size

---

## 🎨 UI/UX Enhancements

#### UX-019: Add Animation Preview on Hover
**Status**: Idea  
**Category**: Frontend - UX

**Description**:  
Currently, video only plays when card is hovered. Consider showing a preview thumbnail or GIF.

**Proposed Solution**:  
- Generate thumbnail from first frame
- Create low-quality GIF preview
- Show on hover before video loads
- Smooth transition to full video

---

#### UX-020: Keyboard Shortcuts
**Status**: Idea  
**Category**: Frontend - UX

**Description**:  
Add keyboard shortcuts for power users.

**Proposed Shortcuts**:  
- `Esc` - Close modal (already works?)
- `Space` - Play/Pause video in modal
- `Arrow keys` - Navigate between animations
- `/` - Focus search (if search implemented)
- `?` - Show keyboard shortcuts help

---

## 📊 Analytics & Monitoring

#### FEAT-021: Add Analytics
**Status**: Idea  
**Category**: Analytics

**Description**:  
If this becomes public, consider adding analytics to understand usage.

**Proposed Metrics**:  
- Most viewed animations
- Modal open rate
- Average time spent
- Device/browser breakdown
- Geographic distribution

**Privacy Considerations**:  
- Be transparent about data collection
- Use privacy-friendly analytics (Plausible, Fathom)
- No personal data collection
- Add privacy policy

---

## 🔐 Security

#### SEC-022: Add Content Security Policy
**Status**: Open  
**Category**: Security

**Description**:  
Add CSP headers to prevent XSS and other attacks if deploying publicly.

**Implementation**:  
- Add CSP meta tag or headers
- Whitelist trusted sources
- Test thoroughly

---

## Priority Legend

- **High Priority**: Should be addressed soon
- **Medium Priority**: Important but not urgent
- **Low Priority**: Nice to have
- **Idea**: Needs more discussion/planning

---

## Contributing to Backlog

When adding new items:

1. Use format: `CATEGORY-XXX: Title`
2. Include Status, Category, and File (if applicable)
3. Provide clear description
4. Add implementation ideas or proposed solutions
5. Note any trade-offs or considerations

---

*Last Updated: 2025*
