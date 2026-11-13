---
name: multi-timeframe-aggregation-and-interactive-drilldown
description: Hierarchical multi-timeframe OHLCV aggregation (Monthly, Weekly, Daily, Intraday) with dynamic windowing, Matplotlib canvas double-click coordinate mapping, and modal constraint drill-down.
---

# Multi-Timeframe (MTF) Aggregation & Interactive Drill-Down Architecture

## Overview
When analyzing multi-year high-frequency financial datasets (e.g. 300,000+ 1-minute bars), rendering the full raw series causes UI freezing, memory exhaustion, and unreadable chart compression. The **Multi-Timeframe (MTF) Drill-Down Architecture** enforces a strict hierarchical pyramid model:
1. **Macro View (Monthly & Weekly)**: Low candle counts (~12 to 52 bars/year) for long-term geometric trends.
2. **Intermediate View (Daily)**: Single-candle trading sessions (~248 bars/year) with NSE holiday and weekend exclusion.
3. **Micro View (1-Min Intraday)**: Sliced on-demand via user modal prompt or canvas double-click.

---

## 1. High-Performance OHLCV Resampling Engine

Given a continuous 1-minute time series indexed or columned with localized Indian Standard Time (`Asia/Kolkata`):

```python
import pandas as pd

class MultiTimeframeEngine:
    @classmethod
    def aggregate_timeframe(cls, df: pd.DataFrame, resolution: str) -> pd.DataFrame:
        """Aggregates 1-minute OHLCV data into Monthly, Weekly, or Daily candlesticks."""
        if df is None or df.empty:
            return pd.DataFrame(columns=["timestamp", "open", "high", "low", "close", "volume"])

        df_work = df.copy()
        if "timestamp" not in df_work.columns:
            if "timestamp_ist" in df_work.columns:
                df_work["timestamp"] = df_work["timestamp_ist"]
            elif isinstance(df_work.index, pd.DatetimeIndex):
                df_work["timestamp"] = df_work.index
            else:
                return df_work

        if not pd.api.types.is_datetime64_any_dtype(df_work["timestamp"]):
            df_work["timestamp"] = pd.to_datetime(df_work["timestamp"])

        # Localized naive timestamp prevents PeriodIndex timezone warnings
        ts = df_work["timestamp"]
        ts_naive = ts.dt.tz_localize(None) if ts.dt.tz is not None else ts

        res_clean = resolution.strip().lower()
        if "month" in res_clean:
            group_key = ts_naive.dt.to_period("M")
        elif "week" in res_clean:
            group_key = ts_naive.dt.to_period("W")
        elif "day" in res_clean or "daily" in res_clean:
            group_key = ts.dt.date  # Strictly excludes holidays and weekends
        else:
            return df_work

        agg_dict = {
            "timestamp": "first",
            "open": "first",
            "high": "max",
            "low": "min",
            "close": "last",
            "volume": "sum"
        }

        grouped = df_work.groupby(group_key, sort=True).agg(agg_dict).reset_index(drop=True)
        grouped.sort_values("timestamp", inplace=True)
        grouped.reset_index(drop=True, inplace=True)
        return grouped
```

---

## 2. Interactive Canvas Double-Click Coordinate Mapping

Binding the Matplotlib event loop directly to UI drill-down:

```python
def _build_canvas(self):
    self.fig = Figure(...)
    self.canvas = FigureCanvasTkAgg(self.fig, master=self)
    # Register double-click listener
    self.canvas.mpl_connect("button_press_event", self._on_canvas_click)

def _on_canvas_click(self, event):
    """Maps double-click x-coordinate in bar-index space to calendar date and drills down."""
    if not event.dblclick or event.inaxes != self.ax or event.xdata is None:
        return

    if self.current_timeframe not in ["Daily", "Weekly", "Monthly"]:
        return

    bar_idx = int(round(event.xdata))
    if self.current_slice is None or bar_idx < 0 or bar_idx >= len(self.current_slice):
        return

    clicked_bar = self.current_slice.iloc[bar_idx]
    ts = clicked_bar.get("timestamp")
    if ts is not None:
        target_date_str = pd.to_datetime(ts).strftime("%Y-%m-%d")
        self.drill_down_to_date(target_date_str)
```

---

## 3. Dynamic Modal Constraint Slicing

Support for flexible user boundary constraints (`YYYY-MM-DD`, `YYYY-MM`, or `YYYY`):

```python
def drill_down_to_constraint(self, constraint_str: str):
    c = constraint_str.strip()
    ts_col = self.raw_1m_df["timestamp"]
    sliced = pd.DataFrame()

    if len(c) == 10 and c.count("-") == 2:  # Day
        target_d = pd.to_datetime(c).date()
        sliced = self.raw_1m_df[ts_col.dt.date == target_d].copy().reset_index(drop=True)
    elif len(c) == 7 and c.count("-") == 1:  # Month
        sliced = self.raw_1m_df[ts_col.dt.strftime("%Y-%m") == c].copy().reset_index(drop=True)
    elif len(c) == 4 and c.isdigit():       # Year
        sliced = self.raw_1m_df[ts_col.dt.year == int(c)].copy().reset_index(drop=True)

    if not sliced.empty:
        self.intraday_slice_df = sliced
        self.active_df = sliced
        self.current_timeframe = "1-Min Intraday"
        self.timeframe_var.set("1-Min Intraday")
        self.render_window(0, min(150, len(sliced)))
```
