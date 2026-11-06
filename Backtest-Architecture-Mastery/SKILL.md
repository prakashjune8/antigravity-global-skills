---
name: Backtest-Architecture-Mastery
description: Institutional backtesting architecture, event-driven state machines, MFE/MAE excursion analysis, Indian exchange cost modeling, and quant tear sheet generation.
---

# Backtest Architecture Mastery: Institutional Quantitative Verification

## 1. Architectural Philosophy & Comparative Synthesis
This skill synthesizes the architectural paradigms of the world's leading institutional backtesting platforms:
- **QuantConnect LEAN**: Pluggable reality models (slippage, transaction fees, margin/buying power checks, network latency simulation, and order event dispatchers).
- **AmiBroker**: Vectorized array-processing for rapid exploratory parameter grids and walk-forward matrix evaluation.
- **NinjaTrader**: Tick/minute replay state machine with strictly non-anticipative queue fills (bid/ask trade-through) and automated bracket management (ATM).
- **Zipline / VectorBT**: Clean columnar multi-timeframe alignment, pipeline abstractions, and memory-contiguous NumPy/Polars data structures.

## 2. Preventing Biases (Zero-Hallucination Execution)
1. **Look-Ahead Bias Elimination**:
   - Indicator and signal calculations at timestamp $t$ may *only* consume data up to bar close $t-1$.
   - A signal generated on bar $t$ can only be filled on or after bar $t+1$ Open (or intra-bar only via strictly chronological intra-bar ticks).
2. **In-Sample (IS) vs. Out-of-Sample (OOS) Partitioning**:
   - Strict temporal data segregation to prevent curve-fitting and data-snooping bias:
     - **In-Sample (IS) Training/Optimization Window**: `2020-01-01` to `2023-12-31` (4 years covering crash, recovery, and consolidation).
     - **Out-of-Sample (OOS) Validation Window**: `2024-01-01` to `2025-12-31` (2 years blind forward test).
   - Parameters calibrated on IS must never be re-fitted on OOS; OOS metrics serve as the definitive benchmark of strategy decay and edge robustness.
3. **Survivorship Bias Mitigation**:
   - Use point-in-time constituent universes or continuous futures rollover stitched by open interest / volume rather than naive front-month stitching.
4. **Network Latency Simulation**:
   - Institutional reality modeling requires simulating deterministic and stochastic transit delays between order dispatch and exchange matching:
     $$t_{\text{matching}} = t_{\text{dispatch}} + \Delta t_{\text{latency}}, \quad \Delta t_{\text{latency}} \sim \mathcal{U}(50\text{ms}, 200\text{ms})$$
   - Orders triggered on 1-minute bar closes are delayed into the subsequent bar auction matching queue.
5. **Indian Exchange Friction Modeling**:
   - Securities Transaction Tax (STT / CTT): $0.0125\%$ on intraday equity/futures turnover (sell side for equity futures, delivery rates for cash).
   - Exchange Turnover Fees: NSE $\approx 0.0019\%$, MCX $\approx 0.0021\%$.
   - SEBI Turnover Charges: $₹10$ per crore ($0.0001\%$).
   - GST: $18\%$ on (Brokerage + Exchange Turnover + SEBI charges).
   - Stamp Duty: $0.002\%$ on buy side.
   - Slippage Model: Volatility-adjusted Half-Spread + Impact Slippage:
     $$\text{Fill Price} = P_{\text{mid}} \pm \left(\frac{\text{Spread}}{2} + \sigma_{\text{intraday}} \times \sqrt{\frac{\text{Order Qty}}{\text{Bar Volume}}}\right)$$

## 3. Mathematical MFE & MAE Formulation
For a long trade $i$ entered at $P_{\text{entry}}$ at time $t_0$ and exited at $t_{\text{exit}}$:
$$\text{MFE}_i = \max_{t_0 \le t \le t_{\text{exit}}} \left(P_t - P_{\text{entry}}\right)$$
$$\text{MAE}_i = \min_{t_0 \le t \le t_{\text{exit}}} \left(P_t - P_{\text{entry}}\right) \quad (\text{negative value represents drawdown})$$
For a short trade $i$:
$$\text{MFE}_i = \max_{t_0 \le t \le t_{\text{exit}}} \left(P_{\text{entry}} - P_t\right)$$
$$\text{MAE}_i = \min_{t_0 \le t \le t_{\text{exit}}} \left(P_{\text{entry}} - P_t\right)$$

- **Stop-Loss Noise Surviving Test**: If $|\text{MAE}_i| \ge \text{Stop-Loss}$ before reaching Target 1, the stop is prematurely triggered by market noise. A valid Gann harmonic level must demonstrate an MAE cluster strictly constrained within the noise floor ($\le 18\text{ points}$ on Nifty).

## 4. Derivatives & Options Expansion Architecture (Phase 2 Stubs)
- **Nifty Weekly Options Chain Architecture**:
  - Strike spacing: $50\text{ pts}$ on Nifty 50, $100\text{ pts}$ on Bank Nifty.
  - Expiry cadence: Thursday weekly expiries (NSE circular compliant).
- **Greeks Computation Engine**:
  - Black-Scholes-Merton (BSM) analytical formula and Bjerksund-Stensland approximation for American options.
  - Outputs: Delta ($\Delta$), Gamma ($\Gamma$), Vega ($\mathcal{V}$), Theta ($\Theta$), Rho ($\rho$), and Implied Volatility (IV via Newton-Raphson inversion).

## 5. Institutional Quant Tear Sheet Metrics
1. **Total Return & CAGR**: Cumulative compounded equity growth.
2. **Maximum Drawdown (MDD %)**:
   $$\text{MDD} = \max_{\tau \le t} \left(\frac{\text{Peak}_\tau - \text{Equity}_t}{\text{Peak}_\tau}\right)$$
3. **Win Rate & Profit Factor**:
   $$\text{Profit Factor} = \frac{\sum \text{Gross Profits}}{\sum |\text{Gross Losses}|}$$
4. **Expectancy per Trade**:
   $$\mathbb{E} = (\text{Win Rate} \times \overline{\text{Win}}) - (\text{Loss Rate} \times \overline{\text{Loss}})$$
5. **Sharpe & Sortino Ratios**: Risk-adjusted returns against risk-free rate ($6.5\%$ RBI repo) with downside deviation penalty.
6. **Time-in-Market Exposure**: Ratio of holding period to total session duration ($375\text{ mins}$ on NSE).
