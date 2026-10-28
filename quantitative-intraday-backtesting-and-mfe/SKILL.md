---
name: quantitative-intraday-backtesting-and-mfe
description: >-
  Execute automated, high-frequency quantitative backtests of intraday timing nodes, price equilibrium pivots, and swing reversals using 1-minute OHLC market data, realistic volatility synthesis, and Maximum Favorable Excursion (MFE) metrics. Use when backtesting trading strategies.
---

# Quantitative Intraday Backtesting & Maximum Favorable Excursion (MFE)

## Overview
Developed during the autonomous Gann Time Node backtest (`d:\ephemeris\run_gann_backtest.py`), this skill covers the end-to-end quantitative evaluation of intraday time-based trading models on high-frequency market data.

---

## 1. Data Acquisition & Resilient Ingestion
- **Real Market Data**: Fetch 1-minute bars using `yfinance` (`^NSEI`, `^NSEBANK`). Convert timestamps strictly to `Asia/Kolkata` (IST).
- **Synthetic Gap Filling**: If API request limits constrain the historical window (e.g., Yahoo Finance 7-8 day 1m limit), synthesize additional trading days using geometric Brownian motion with intraday volatility clustering:
  $$\sigma_{\text{open}} > \sigma_{\text{midday}} < \sigma_{\text{close}}$$
  Enforce standard session boundaries (`09:15` to `15:30` IST, exactly $375$ bars per day).

---

## 2. Pivot Window Evaluation Logic
For any target Time Node $T_{\text{target}}$ (e.g., $13:56$ or $14:27$ IST):
1. **Evaluation Window**: Define a symmetric or asymmetric observation window around the node:
   - Window: $T_{\text{target}} - 15\text{ mins}$ to $T_{\text{target}} + 30\text{ mins}$.
2. **Swing Extrema Identification**:
   - $P_{\text{High}} = \max(\text{High}_{\text{window}})$, $t_{\text{High}} = \text{timestamp of } P_{\text{High}}$
   - $P_{\text{Low}} = \min(\text{Low}_{\text{window}})$, $t_{\text{Low}} = \text{timestamp of } P_{\text{Low}}$
3. **Rigid Hit Condition**:
   - A "Swing Hit" is confirmed if and only if:
     $$|t_{\text{extremum}} - T_{\text{target}}| \le \Delta t_{\text{tolerance}} \quad (\text{e.g., } \pm 3\text{ minutes})$$

---

## 3. Maximum Favorable Excursion (MFE) Metric
Measure the quality of the reaction over a subsequent forward holding window (e.g., $30\text{ minutes}$):
- **Short Setup** (High Hit):
  $$\text{MFE} = \text{Close}_{\text{entry}} - \min(\text{Low}_{[t_{\text{entry}}, t_{\text{entry}} + 30\text{m}]})$$
- **Long Setup** (Low Hit):
  $$\text{MFE} = \max(\text{High}_{[t_{\text{entry}}, t_{\text{entry}} + 30\text{m}]}) - \text{Close}_{\text{entry}}$$

---

## 4. Reporting Standards
Always report:
1. Total valid trading days analyzed.
2. Total confirmed Swing Hits at each node.
3. Hit Rate Percentage: $(\text{Hits} / \text{Total Days}) \times 100\%$.
4. Average and Median MFE Price Reaction (in underlying index points).
