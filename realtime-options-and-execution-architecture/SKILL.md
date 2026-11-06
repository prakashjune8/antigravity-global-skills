---
name: realtime-options-and-execution-architecture
description: Institutional real-time derivatives pricing, analytical Black-Scholes-Merton with continuous dividend yield, minute-level weekly expiry decay, Newton-Raphson IV inversion, mutex-guarded signal lockout state machines, and PyInstaller desktop executable bundling.
---

# Real-Time Options Pricing, Greeks & Execution Architecture

## 1. Overview
This skill codifies institutional engineering patterns for real-time options analytics, ultra-low-latency execution bridges, and standalone desktop application deployment for derivatives trading.

---

## 2. Core Quantitative Foundations

### A. Extended Black-Scholes-Merton (BSM) with Continuous Dividend Yield ($q$)
European index options on broad equity indices (e.g., NSE Nifty 50) pay continuous dividends. Valuation requires the Merton (1973) continuous yield adjustment:

$$d_1 = \frac{\ln(S/K) + \left(r - q + \frac{\sigma^2}{2}\right)T}{\sigma\sqrt{T}}$$
$$d_2 = d_1 - \sigma\sqrt{T}$$
$$C(S, K, T) = S e^{-qT} N(d_1) - K e^{-rT} N(d_2)$$
$$P(S, K, T) = K e^{-rT} N(-d_2) - S e^{-qT} N(-d_1)$$

- **Zero-Dependency Normal CDF via `math.erf`**:
  $$N(x) = \frac{1}{2} \left[1 + \text{erf}\left(\frac{x}{\sqrt{2}}\right)\right]$$
  Achieves IEEE 64-bit double precision ($10^{-15}$) without requiring heavy C-extensions or SciPy.

### B. Minute-Level Expiry Decay ($T$)
Intraday index options experience violent Gamma and Theta decay approaching weekly Thursday expiry at `15:30:00 IST`. $T$ must be modeled down to exact minutes:
$$T = \frac{\text{Minutes to Expiry}}{525,960.0 \text{ mins/year}}$$
Holiday calendar rolling: automatically shifts expiry date to Wednesday if Thursday is an exchange statutory holiday.

### C. Robust Implied Volatility Inversion
- **Brenner-Subrahmanyam Quadratic Seed**:
  $$\sigma_0 \approx \sqrt{\frac{2\pi}{T}} \frac{C_{\text{obs}}}{S}$$
- **Newton-Raphson Iteration**:
  $$\sigma_{k+1} = \sigma_k - \frac{C(\sigma_k) - C_{\text{obs}}}{\mathcal{V}(\sigma_k)}$$
- **Bisection Fail-Safe**: When $\mathcal{V}(\sigma) \to 0$ in deep ITM/OTM wings, automatically branch to bounded bisection on $\sigma \in [0.01, 3.00]$.

---

## 3. High-Frequency Execution Safety & Signal Lockout

### The Infinite Loop Hazard
When real-time signals hover at an exact harmonic price/time confluence node, event-driven loops risk dispatching dozens of duplicate bracket orders per second, exhausting margin and triggering liquidation.

### Mutex-Guarded Signal Lockout State Machine
1. Construct deterministic canonical key:
   $$\text{Lockout Key} = \text{SessionDate} + \text{"\_"} + \text{Symbol} + \text{"\_"} + \text{NodeID} + \text{"\_"} + \text{Side}$$
2. Guard dispatch with an re-entrant mutex (`threading.Lock`):
   ```python
   with self._mutex:
       if lockout_key in self.dispatched_signals:
           return False, "OMS LOCKOUT: Signal node already [EXECUTED] today."
       # Atomic mark under lock BEFORE network call
       self.dispatched_signals.add(lockout_key)
       self.executed_node_lockouts.add(lockout_key)
   ```
3. Guarantees race-condition immunity: exactly $1$ thread executes, while $N$ concurrent millisecond duplicates are violently rejected.

---

## 4. Bounded API Rate Limiting
Broker endpoints enforce hard request quotas (e.g. 10 req/s). Enforce a sliding-window token bucket:
```python
class APIRateLimiter:
    def __init__(self, max_requests_per_sec: float = 10.0, window_sec: float = 1.0):
        self.max_requests = max_requests_per_sec
        self.window_sec = window_sec
        self._timestamps = collections.deque()
        self._mutex = threading.Lock()

    def acquire(self) -> bool:
        with self._mutex:
            now = time.time()
            cutoff = now - self.window_sec
            while self._timestamps and self._timestamps[0] <= cutoff:
                self._timestamps.popleft()
            if len(self._timestamps) < self.max_requests:
                self._timestamps.append(now)
                return True
            return False
```

---

## 5. PyInstaller Standalone Windows Deployment

When compiling CustomTkinter applications into `--onefile --noconsole` binaries:
1. **Mandatory CustomTkinter Flag**:
   `--collect-all=customtkinter` (ships required JSON themes and fonts).
2. **Runtime Path Resolution (`sys._MEIPASS`)**:
   - Seed bundled read-only database (`.cache`) and preferences (`user_preferences.json`) to `%LOCALAPPDATA%\<App>\` on first boot.
   - Preserves user preferences and SQLite caches across sessions without bundle read-only crashes.
3. **Automated Desktop Shortcut Creation**:
   Automate via PowerShell COM `WScript.Shell` linking `dist/<App>.exe` directly to `[Environment]::Desktop`.
