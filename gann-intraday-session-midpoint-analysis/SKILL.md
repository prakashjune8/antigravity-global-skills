---
name: gann-intraday-session-midpoint-analysis
description: >-
  Calculate intraday 50% price equilibrium levels, 180° temporal session midpoints, Spencer Equation of Time true solar noon, and micro-harmonic time nodes (90° at 13:56, 120° at 14:27 IST). Use when analyzing intraday swing pivots for Indian equity indices.
---

# Intraday Session Midpoint Analysis & 360° Time Harmonics

## Overview
Derived from W.D. Gann's *45 Years in Wall Street* and *The Basis of My Forecasting Method*, this skill covers intraday equilibrium squaring: 50% price midpoints, session temporal centers, and solar noon offsets.

---

## 1. The 50% Price Equilibrium Principle
Gann considered the $50\%$ division of any range the highest-gravity price pivot:
$$P_{50\%} = \frac{P_{\text{High}} + P_{\text{Low}}}{2}$$
When price crosses above $P_{50\%}$, the trend is bullish; when price trades below, the trend is bearish.

---

## 2. NSE Continuous Session 360° Time Harmonics (09:15 to 15:30 IST)
The $375$-minute NSE trading session is mapped onto the $360^\circ$ circle:
- **Session Open ($0^\circ$)**: `09:15:00` IST ($0\text{ mins}$)
- **$45^\circ$ Harmonic**: `11:45:00` IST ($150\text{ mins}$)
- **$50\%$ Equilibrium / $180^\circ$ Temporal Midpoint**: `12:22:30` IST ($187.5\text{ mins}$)
- **$90^\circ$ Squaring Node**: `13:56:15` IST ($281.25\text{ mins}$)
- **$120^\circ$ Trine Node**: `14:27:30` IST ($312.5\text{ mins}$)
- **Session Close ($360^\circ$)**: `15:30:00` IST ($375\text{ mins}$)

---

## 3. Spencer Equation of Time True Solar Noon
Solar noon deviates from mean clock noon ($12:00$) due to orbital eccentricity and axial obliquity:
$$\text{EoT} = 229.18 \times [0.000075 + 0.001868\cos(\Gamma) - 0.032077\sin(\Gamma) - 0.014615\cos(2\Gamma) - 0.040849\sin(2\Gamma)]$$
For Mumbai ($72.87^\circ\text{ E}$) / NSE Servers: True Solar Noon prints between `12:28` and `12:44` IST depending on the seasonal day of the year.
