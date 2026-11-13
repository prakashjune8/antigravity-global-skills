---
name: continuous-river-flow-data-streaming
description: High-frequency FIFO sliding window streaming architecture rendering multi-session 1-minute OHLCV market data like a flowing river inside a fixed rectangular frame with zero memory accumulation and dynamic day boundary markers.
---

# Continuous River Flow Data Streaming Architecture

## 1. Architectural Philosophy & The River Paradigm
In high-frequency quantitative visualizers, traditional charting models either append endlessly (causing DOM/Matplotlib memory explosion) or abruptly wipe the canvas at session boundaries (breaking human cognitive continuity). 

The **River Flow Architecture** treats financial time-series as an endless continuous stream flowing through a **fixed rectangular viewport**:
1. **Constant Bounded Window ($W$)**: Exactly two full trading sessions (e.g., $W = 750$ 1-minute candles for NSE Nifty 50, where each session is 375 minutes from 09:15 to 15:30 IST).
2. **Fixed Horizontal Viewport Coordinates**: The x-axis limits are strictly locked to `[-0.8, W - 0.2]`.
3. **Physical Drift Illusion**: As new incoming candles enter at the far right ($x = W - 1$), the oldest candles at $x = 0$ drop off into the left boundary. Every existing candle shifts left by $k$ units on each tick.
4. **Drifting Session Boundaries**: When the active slice spans multiple calendar days, an interactive vertical boundary line (`⚡ [Date] OPEN (09:15)`) moves smoothly from right to left like a boat drifting downstream.

---

## 2. Mathematical Formalism

### 2.1 Sliding Cursor & Slicing Equation
Given a multi-year 1-minute dataset $\mathcal{D} = \{b_0, b_1, \dots, b_{N-1}\}$ with $N$ rows, and a fixed window size $W = 750$:

$$\text{start\_idx} = \max(0, \text{cursor} - W)$$

$$\mathcal{S}_{\text{visible}} = \mathcal{D}[\text{start\_idx} : \text{cursor}]$$

On each tick with step $\Delta \in \{1, 4, 15\}$:
$$\text{cursor}_{t+1} = \begin{cases} 
\text{cursor}_t + \Delta, & \text{if } \text{cursor}_t + \Delta \le N \\
W, & \text{if } \text{cursor}_t + \Delta > N \quad \text{(Seamless wrap-around)}
\end{cases}$$

### 2.2 Day Boundary Separation Index
$$\mathcal{K} = \left\{ i \in [1, W-1] \;\middle|\; \text{date}(b_i) \neq \text{date}(b_{i-1}) \right\}$$

For each boundary $k \in \mathcal{K}$:
- Draw vertical separator at $x = k - 0.5$.
- Annotate with open timestamp and date badge.

---

## 3. High-Performance Vectorized Rendering Implementation

```python
import numpy as np
import pandas as pd
from matplotlib.collections import LineCollection, PolyCollection

def render_river_slice(ax, slice_df: pd.DataFrame, window_bars: int = 750, is_streaming: bool = True):
    ax.clear()
    n_bars = len(slice_df)
    indices = np.arange(n_bars)

    opens = slice_df["open"].to_numpy(dtype=float)
    highs = slice_df["high"].to_numpy(dtype=float)
    lows = slice_df["low"].to_numpy(dtype=float)
    closes = slice_df["close"].to_numpy(dtype=float)

    bullish = closes >= opens
    bull_color = "#10b981"
    bear_color = "#ef4444"

    # 1. High-Speed Vectorized Wicks
    wick_segs = [((i, l), (i, h)) for i, l, h in zip(indices, lows, highs)]
    wick_colors = [bull_color if b else bear_color for b in bullish]
    ax.add_collection(LineCollection(wick_segs, colors=wick_colors, linewidths=1.0, alpha=0.9))

    # 2. Vectorized Candle Bodies
    width = 0.32
    green_verts = [((i - width, o), (i - width, c), (i + width, c), (i + width, o)) for i, o, c in zip(indices[bullish], opens[bullish], closes[bullish])]
    red_verts = [((i - width, c), (i - width, o), (i + width, o), (i + width, c)) for i, o, c in zip(indices[~bullish], opens[~bullish], closes[~bullish])]
    if green_verts:
        ax.add_collection(PolyCollection(green_verts, facecolors=bull_color, edgecolors=bull_color, linewidths=0.6))
    if red_verts:
        ax.add_collection(PolyCollection(red_verts, facecolors=bear_color, edgecolors=bear_color, linewidths=0.6))

    # 3. Drifting Day Boundaries
    if "timestamp" in slice_df.columns and n_bars > 1:
        dates = pd.to_datetime(slice_df["timestamp"]).dt.date
        day_splits = np.where(dates.values[1:] != dates.values[:-1])[0] + 1
        y_max = float(np.max(highs))
        for split_idx in day_splits:
            split_date = dates.iloc[split_idx]
            ax.axvline(split_idx - 0.5, color="#818cf8", linestyle="--", linewidth=1.2, alpha=0.75, zorder=3)
            ax.text(split_idx, y_max, f" ⚡ {split_date.strftime('%d %b %Y')} OPEN", color="#a5b4fc", fontsize=8, fontweight="bold", va="top")

    # 4. Viewport Locking
    if is_streaming:
        ax.set_xlim(-0.8, window_bars - 0.2)
    else:
        ax.set_xlim(-0.8, n_bars - 0.2)

    y_min, y_max = float(np.min(lows)), float(np.max(highs))
    padding = (y_max - y_min) * 0.12 if y_max > y_min else 10.0
    ax.set_ylim(y_min - padding, y_max + padding)
```

---

## 4. Institutional Guarantees
1. **$O(1)$ Memory Consumption**: Memory footprint remains flat over thousands of hours of playback because the rendered array slice length is permanently clamped at $W$.
2. **Smooth Psychological Flow**: Eliminates screen flashing and eye-strain while preserving historical context across inter-day transitions.
3. **Full Overlay Alignment**: Gann Cardinal/Fixed price rays, 180° midpoints, and Spencer True Solar Noon lines dynamically recalculate and glide smoothly in synchronization with the current flow.
