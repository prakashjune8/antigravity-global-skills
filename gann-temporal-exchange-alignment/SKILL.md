---
name: gann-temporal-exchange-alignment
description: >-
  Convert Universal Time (UT/UTC) astronomical timestamps to Indian Standard Time (IST, UTC+05:30) and synchronize planetary events with Indian exchange trading sessions (NSE, BSE, MCX). Use when evaluating market timing triggers for Indian financial markets.
---

# Temporal Exchange Alignment: UTC to Indian Standard Time (IST)

## Overview
Originated from the Gann Ephemeris project, this skill establishes the exact temporal conversion and session alignment rules between Universal Time (UT/UTC) and Indian Standard Time (IST, UTC+05:30).

---

## 1. Mathematical Time Offset
$$\text{IST} = \text{UTC} + 5\text{ hours } 30\text{ minutes}$$
- Indian Standard Time does not observe Daylight Saving Time (DST). The offset remains invariant year-round.

---

## 2. Indian Exchange Session Definitions
1. **NSE / BSE Equity & Derivatives**:
   - Pre-Open: `09:00:00` to `09:08:00` IST
   - Regular Continuous Session: `09:15:00` to `15:30:00` IST
   - Total Continuous Duration: $375\text{ minutes}$ ($6.25\text{ hours}$)
2. **MCX Commodity Derivatives**:
   - Base Metals & Energy (Standard): `09:00:00` to `23:30:00` IST
   - US Daylight Saving Period: `09:00:00` to `23:55:00` IST
