---
name: quadrant-one-drafting-and-viewport-autoscale
description: Restrict 2D Cartesian drafting grids, rendering pipelines, and camera pan strictly to Quadrant I (+x >= 0, +y >= 0) with locked (0, 0) origin, hardware-clipped pattern blitting, dynamic visible-candle vertical auto-fit, and timeframe fractal swing lookbacks.
---

# Quadrant I Drafting & Viewport Auto-Scale Architecture

## Overview
In financial, mathematical, and technical charting engines, displaying negative price space ($y < 0$) or negative forward time ($x < 0$) consumes unnecessary memory, inflates GPU rasterization workloads, and distorts candlestick scaling.

This skill formalizes the engineering methodology to:
1. Restrict camera movement and coordinate engines strictly to **Quadrant I ($+x \ge 0, +y \ge 0$)** anchored at a fixed origin `(0, 0)`.
2. Cull negative quadrants across 4-tier canvas rendering pipelines.
3. Dynamically auto-fit vertical price scales around the active/visible candle slice during horizontal sliding with $+10\%$ upper ceiling headroom.
4. Scale swing detection lookbacks fractally based on timeframe bar density.

---

## 1. Mathematical Camera Pan Bounds for Quadrant I

In a Cartesian coordinate system mapped to an HTML5 raster canvas:
* In Cartesian world space, $(worldX = 0, worldY = 0)$ is the origin.
* In screen space, $(0, 0)$ is top-left, and $(pan.x, pan.y)$ is the screen coordinate of the origin $(worldX = 0, worldY = 0)$.
* Conversion formulas:
  $$\text{screenX} = pan.x + worldX \cdot zoom$$
  $$\text{screenY} = pan.y - worldY \cdot zoom$$

When four-sided rulers exist with thickness $\text{leftOffset}$ and $\text{bottomOffset}$:
* The usable drafting viewport begins horizontally at $\text{screenX} = \text{leftOffset}$.
* The usable drafting viewport ends vertically at $\text{screenY} = \text{screenHeight} - \text{bottomOffset}$.

### The Clamping Theorems

#### Horizontal Clamp (Eliminating $x < 0$):
For any screen point $\text{screenX} \ge \text{leftOffset}$, we require $worldX = \frac{\text{screenX} - pan.x}{zoom} \ge 0$.
The minimum value of $\text{screenX}$ is $\text{leftOffset}$.
$$\frac{\text{leftOffset} - pan.x}{zoom} \ge 0 \implies pan.x \le \text{leftOffset}$$

#### Vertical Clamp (Eliminating $y < 0$):
For any screen point $\text{screenY} \le \text{screenHeight} - \text{bottomOffset}$, we require $worldY = \frac{pan.y - \text{screenY}}{zoom} \ge 0$.
The maximum value of $\text{screenY}$ is $\text{screenHeight} - \text{bottomOffset}$.
$$\frac{pan.y - (\text{screenHeight} - \text{bottomOffset})}{zoom} \ge 0 \implies pan.y \ge \text{screenHeight} - \text{bottomOffset}$$

### Implementation:
```typescript
export function clampPanToQuadrant1(
  pan: Point2D,
  screenHeight: number,
  showLeftAxis: boolean = true,
  showBottomAxis: boolean = true
): Point2D {
  const leftOffset = showLeftAxis ? 84 : 0;
  const bottomOffset = showBottomAxis ? 32 : 0;

  // Prevent camera from panning right into negative time:
  const clampedX = Math.min(leftOffset, Math.round(pan.x));

  // Prevent camera from panning down into negative price:
  const minPanY = Math.round(screenHeight - bottomOffset);
  const clampedY = Math.max(minPanY, Math.round(pan.y));

  return { x: clampedX, y: clampedY };
}
```

---

## 2. Multi-Tier Negative Quadrant Culling Pipeline

Even with camera clamping, rendering subroutines must guarantee that no objects or tile patterns are generated or rasterized outside Quadrant I.

### Layer 1: Hardware-Clipped Pattern Tiling
Do not fill the whole canvas with repeated grid patterns. Fill the background with paper, then clip pattern blits strictly to the Quadrant I rectangle:

```typescript
// 1. Fill entire canvas with clean unpatterned parchment
ctx.fillStyle = theme.paperBackground;
ctx.fillRect(0, 0, width, height);

// 2. Compute Quadrant I bounding rectangle
const q1Left = Math.max(0, Math.round(pan.x));
const q1Bottom = Math.min(height, Math.round(pan.y));
const q1Width = Math.max(0, width - q1Left);
const q1Height = Math.max(0, q1Bottom);

// 3. Clip and blit pattern strictly in Quadrant I
if (q1Width > 0 && q1Height > 0) {
  ctx.save();
  ctx.beginPath();
  ctx.rect(q1Left, 0, q1Width, q1Height);
  ctx.clip();
  ctx.fillStyle = pattern;
  ctx.fillRect(0, 0, width, height);
  ctx.restore();
}
```

### Layer 2: Directional Axis Rays
Never stroke Cartesian zero-axes across the full viewport:
* **Horizontal $X$-Axis Line ($Y = 0$)**: Starts at $\max(0, axisX)$ and extends rightward to $width$.
* **Vertical $Y$-Axis Line ($X = 0$)**: Starts at $0$ and extends downward strictly to $\min(height, axisY)$.

```typescript
const axisY = Math.round(pan.y);
const axisX = Math.round(pan.x);
const startAxisX = Math.max(0, axisX);

ctx.beginPath();
// X-axis (Price = 0)
if (axisY >= 0 && axisY <= height && startAxisX < width) {
  ctx.moveTo(startAxisX, axisY);
  ctx.lineTo(width, axisY);
}
// Y-axis (Time = 0)
if (axisX >= 0 && axisX <= width && axisY > 0) {
  ctx.moveTo(axisX, 0);
  ctx.lineTo(axisX, Math.min(height, axisY));
}
ctx.stroke();
```

### Layer 3: Axis Track Tick Culling
Ensure time rulers never render negative column numbers ($T < 0$) and price rulers never render negative rows:
```typescript
const effectiveStartCol = Math.max(0, startCol);
for (let col = effectiveStartCol; col <= endCol; col++) {
  // Render time ticks and labels strictly for col >= 0
}

const effectiveStartRow = Math.max(0, startRow);
for (let row = effectiveStartRow; row <= endRow; row++) {
  // Render price ticks and labels strictly for row >= 0
}
```

---

## 3. Active-Candle Vertical Auto-Fit on Horizontal Slide

When navigating through historical data (drag, trackpad pan, arrow keys, or scrubber), fixed vertical scales either push candles off-screen or compress high-priced candles into a thin horizontal line.

### Execution Protocol:
1. **Calculate Visible Column Bounds**:
   ```typescript
   const leftWorldX = (0 - currentPanX) / zoom;
   const rightWorldX = (screenW - currentPanX) / zoom;
   const minVisCol = Math.min(leftWorldX, rightWorldX) / baseUnit;
   const maxVisCol = Math.max(leftWorldX, rightWorldX) / baseUnit;
   ```
2. **Filter Visible Slice with Margin**:
   Include a 2-bar margin; if panning over a gap, fall back to the 10 nearest bars.
3. **Compute Extremes & $+10\%$ Upper Ceiling**:
   ```typescript
   const localCeiling = Math.round(localMaxHigh * 1.10 * 100) / 100;
   const priceSpan = Math.max(1, localCeiling - localMinLow);
   ```
4. **Harmonic Scale Quantization**:
   Snap `priceSpan / numGridSquares` to the closest Gann harmonic ladder $[0.01, \dots, 10000]$.
5. **Vertical Centering Inside Quadrant I**:
   Center the midpoint of $[localMinLow, localCeiling]$ on the canvas center, clamping $\text{pan.y} \ge \text{screenHeight} - \text{bottomOffset}$.

---

## 4. Timeframe Fractality for Swing Detectors

A 3-day swing detector must dynamically adapt its bar lookback across different resolutions:
$$\text{lookbackBars} = \text{Days} \times \frac{\text{Trading Minutes per Day}}{\text{Bar Interval Minutes}}$$

| Timeframe | Intraday Minutes | Lookback for 3 Days |
| :--- | :--- | :--- |
| **1m** | 375 bars/day | **1,125 bars** |
| **5m** | 75 bars/day | **225 bars** |
| **15m** | 25 bars/day | **75 bars** |
| **1D** | 1 bar/day | **3 bars** |
| **1W** | 1 bar/week | **1 bar** |

Recalculate dynamically on timeframe switch to eliminate stale swing state while preserving harmonic scale invariants.
