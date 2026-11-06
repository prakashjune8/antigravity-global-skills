---
name: high-frequency-time-series-parquet
description: High-frequency time-series data management using Apache Parquet, Polars, and Fastparquet/PyArrow for multi-year 1-minute OHLCV quantitative backtesting and ML feature stores.
---

# High-Frequency Time-Series Data Management (Apache Parquet & Polars)

## 1. Architectural Philosophy
For institutional quantitative finance, storing millions of high-frequency 1-minute intraday bars across multi-year histories in row-oriented databases (like SQLite) introduces crippling I/O latency, heavy serialization overhead, and inefficient memory layout. 

This skill establishes the columnar data engineering standard using **Apache Parquet with Snappy/ZSTD compression**, manipulated via **Polars / PyArrow**, achieving sub-10ms query execution across gigabyte-scale datasets with memory-mapped zero-copy scans.

## 2. Core Technical Specifications
- **Format**: Apache Parquet (Snappy or ZSTD level 3 compression).
- **Partitioning Strategy**: Partitioned by instrument and calendar year/month (`data/parquet/instrument=NIFTY50/year=2024/month=10.parquet`).
- **Data Types (Strict Schema)**:
  - `timestamp_ist`: `Datetime[ms, "Asia/Kolkata"]` (Primary monotonic index)
  - `open`: `Float64`
  - `high`: `Float64`
  - `low`: `Float64`
  - `close`: `Float64`
  - `volume`: `UInt64`
  - `open_interest`: `UInt64` (Optional for derivatives)
  - `cycle_angle`: `Float32` (Gann Sq9 price angle in [0, 360))

## 3. Implementation Blueprint with Polars
```python
import polars as pl
from pathlib import Path

def save_partitioned_ohlcv(df: pl.DataFrame, base_dir: Path, instrument: str):
    """Save 1-minute OHLCV data partitioned by year and month."""
    base_path = base_dir / f"instrument={instrument}"
    base_path.mkdir(parents=True, exist_ok=True)
    
    df.write_parquet(
        base_path,
        use_pyarrow=True,
        compression="zstd",
        compression_level=3,
        partition_by=["year", "month"]
    )

def query_slice(base_dir: Path, instrument: str, start_dt: str, end_dt: str) -> pl.DataFrame:
    """Lazy zero-copy query slice for high-frequency backtesting."""
    scan = pl.scan_parquet(base_dir / f"instrument={instrument}/**/*.parquet")
    return (
        scan.filter(
            (pl.col("timestamp_ist") >= pl.lit(start_dt).str.to_datetime()) &
            (pl.col("timestamp_ist") <= pl.lit(end_dt).str.to_datetime())
        )
        .sort("timestamp_ist")
        .collect()
    )
```

## 4. Key Rules
1. Never use SQLite for high-frequency 1-minute tick or bar ML feature pipelines.
2. Always store datetime with timezone metadata explicit (`Asia/Kolkata` for Indian markets).
3. Use dictionary encoding for categorical columns and Delta encoding for integer timestamps.
