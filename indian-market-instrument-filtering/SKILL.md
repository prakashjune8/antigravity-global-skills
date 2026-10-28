---
name: indian-market-instrument-filtering
description: >-
  Filter and route Gann timing and price levels strictly to NSE broad indices (Nifty 50), MCX energy (Crude Oil, Natural Gas), and MCX base metals (Copper, Zinc, Aluminium, Lead), while enforcing an absolute, unbreakable exclusion of gold and silver instruments.
---

# Indian Market Instrument Filtering & Asset Routing

## Overview
Originated from the Gann Ephemeris trading system, this skill defines the strict eligibility rules for routing signals and harmonic levels across Indian exchanges.

---

## 1. Permitted Instrument Universe
Signals and calculators must only target:
1. **NSE Broad Indices**: Nifty 50 (`^NSEI`), Bank Nifty (`^NSEBANK`), FinNifty.
2. **NSE Index Derivatives**: Nifty 50 Options & Futures contracts.
3. **MCX Energy Futures**:
   - Crude Oil (`CRUDEOIL`)
   - Natural Gas (`NATURALGAS`)
4. **MCX Base Metal Futures**:
   - Copper (`COPPER`)
   - Zinc (`ZINC`)
   - Aluminium (`ALUMINIUM`)
   - Lead (`LEAD`)

---

## 2. Hard Exclusion Directive: Bullion
> **CRITICAL MANDATORY CONSTRAINT**:  
> Under NO circumstances may any gold or silver instrument (`GOLD`, `GOLDM`, `GOLDPETAL`, `SILVER`, `SILVERM`, `SILVERMIC`) be analyzed, backtested, listed, or displayed in alerts. Any reference to bullion must be strictly rejected or filtered at ingestion.
