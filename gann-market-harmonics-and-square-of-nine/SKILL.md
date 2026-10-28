---
name: gann-market-harmonics-and-square-of-nine
description: >-
  Apply W.D. Gann's Law of Vibration, Square of Nine spiral root derivations, planetary longitude-to-price conversions, and major harmonic aspect triggers (0°, 45°, 90°, 120°, 180°). Use when generating geometric price support/resistance levels and cycle timing nodes.
---

# W.D. Gann Market Harmonics & Square of Nine Mathematics

## Overview
Developed in the Gann Ephemeris and Academic Textbook engines, this skill details W.D. Gann's quantitative methodologies: the Square of Nine spiral, planetary longitude mapping, and aspect trigonometry.

---

## 1. Square of Nine Odd-Square Mathematical Derivation
The Gann Square of Nine begins at origin $1$ and expands outward in concentric rings.
Every full $360^\circ$ rotation increases the square root of the price by exactly $+2.0$:
$$\Delta \sqrt{P} = \frac{\theta}{180^\circ}$$
- **Angle from Price**:
  $$\theta(P) = [ (\sqrt{P} - 1.0) \pmod{2.0} ] \times 180^\circ \quad \text{where } 0^\circ \le \theta < 360^\circ$$
- **Price from Target Angle $\theta$**:
  $$P(k, \theta) = \left[ 2k + 1.0 + \frac{\theta \pmod{360^\circ}}{180^\circ} \right]^2$$
  where $k = \text{floor}\left[ \frac{\sqrt{P_{\text{ref}}} - 1.0 - \theta / 180^\circ}{2} \right]$.

---

## 2. Major Harmonic Aspects & Angular Harmonics
- **Conjunction ($0^\circ$)**: Planetary seeds, major trend initiator.
- **Semi-Square ($45^\circ$)**: Harmonic sub-pivot ($1/8$ circle).
- **Square ($90^\circ$)**: Major resistance / price-time squaring ($1/4$ circle).
- **Trine ($120^\circ$)**: Harmonic equilibrium ($1/3$ circle).
- **Opposition ($180^\circ$)**: Extreme price polarity / cycle reversal ($1/2$ circle).
