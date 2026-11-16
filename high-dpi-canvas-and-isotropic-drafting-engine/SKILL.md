---
name: high-dpi-canvas-and-isotropic-drafting-engine
description: Architect high-performance, hardware-accelerated 2D HTML5 canvas applications with 4-tier layer decoupling, offscreen pattern tiling, dirty-rectangle differential erasure, and strict isotropic aspect-ratio sentinels.
---

# High-DPI Canvas & Isotropic Drafting Engine

## Core Architectural Pillars

### 1. 4-Tier Decoupled Multi-Canvas Layering
To achieve locked 60 FPS under high-DPI (Retina / 4K) scaling, decouple canvas renders by frequency and mutation scope:

- **Layer 1 (`z-index: 10`) - Static Background & Master Grid Tile:**
  - OffscreenCanvas master tile (1 scaled major block = $96\text{px}\times\text{zoom}$).
  - Hardware pattern blit via `ctx.createPattern(tile, 'repeat')` with dynamic `DOMMatrix` translation.
  - Zero stroke loops during pan.
- **Layer 2 (`z-index: 20`) - Data Visualizations (Candlesticks, Swings, Volumes):**
  - Only redraws upon viewport pan, zoom, or underlying dataset changes.
- **Layer 3 (`z-index: 25`) - Fixed Orthogonal Axis Rulers & Corner Junctions:**
  - 4-sided ruler system (Top, Bottom, Left, Right) isolated from cursor movements.
- **Layer 4 (`z-index: 30`) - Dynamic Cursor Reticle, HUD Badges, and Watchdog:**
  - Redraws at 60 FPS strictly driven by mouse movement.

---

### 2. Microscopic Dirty-Rectangle Differential Redraw
Eliminate full-frame `ctx.clearRect(0, 0, width, height)` on cursor movements:

```typescript
interface DirtyRect {
  x: number;
  y: number;
  w: number;
  h: number;
}

// In the mouse/HUD render loop:
// 1. Erase only previous tick's bounding boxes
if (prevDirtyRectsRef.current) {
  for (const r of prevDirtyRectsRef.current) {
    ctx.clearRect(r.x, r.y, r.w, r.h);
  }
  prevDirtyRectsRef.current = null;
}

// 2. Render new crosshair lines & badges, tracking new bounds
const newDirtyRects: DirtyRect[] = [];
// Horizontal line:
newDirtyRects.push({ x: 0, y: Math.floor(cy) - 2, w: width, h: 5 });
// Vertical line:
newDirtyRects.push({ x: Math.floor(cx) - 2, y: 0, w: 5, h: height });
// Badge:
newDirtyRects.push({ x: bX - 3, y: bY - 14, w: bW + 6, h: bH + 6 });

prevDirtyRectsRef.current = newDirtyRects;
```

---

### 3. W.D. Gann K&E 8x8 Isotropic Ratio Sentinel
Enforce exact physical 1-inch and 1/8th-inch geometry with zero non-uniform distortion:

$$\text{Major Unit} = 8 \times \text{Base Unit} = 96\text{px} \quad (1.000\text{ inch at } 96\text{ DPI})$$
$$\text{Base Unit} = 12\text{px} \quad (0.125\text{ inch at } 96\text{ DPI})$$

```typescript
export function verifyKeEAspectRatio(baseUnit: number, majorUnit: number) {
  const expectedMajor = baseUnit * 8;
  const majorDeviation = Math.abs(majorUnit - expectedMajor);
  const baseDeviation = Math.abs(baseUnit - 12);
  const totalDeviation = Math.max(majorDeviation, baseDeviation);

  const isValid = totalDeviation < 0.001;
  return {
    isValid,
    baseUnit: isValid ? baseUnit : 12,
    majorUnit: isValid ? majorUnit : 96,
    subdivisions: 8,
    inchRatio: 0.125,
    deviation: totalDeviation,
    correctionApplied: !isValid,
  };
}
```

Canvas Backing Store Integrity Audit:
```typescript
export function auditCanvasBackingStore(canvas: HTMLCanvasElement, dpr: number = window.devicePixelRatio || 1) {
  const rect = canvas.getBoundingClientRect();
  const expectedW = Math.round(rect.width * dpr);
  const expectedH = Math.round(rect.height * dpr);
  const isDistorted = Math.abs(canvas.width - expectedW) > 1 || Math.abs(canvas.height - expectedH) > 1;
  return { isDistorted, expectedW, expectedH, actualW: canvas.width, actualH: canvas.height, dpr };
}
```

---

### 4. Portable Self-Bootstrapping Node/Vite/PyInstaller Toolchain
For isolated environments lacking system Node.js:
- Automatically downloads standalone portable Node.js binaries into `.tools/node/`.
- Executes `npm run build` (`tsc && vite build`) to generate static `dist/`.
- Bundles `dist/` and `desktop_app.py` via `pyinstaller --onefile --noconsole`.
