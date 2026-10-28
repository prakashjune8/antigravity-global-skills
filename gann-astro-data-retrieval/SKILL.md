---
name: gann-astro-data-retrieval
description: >-
  Query NASA JPL Horizons REST API for high-precision geocentric planetary coordinates, ecliptic longitude/latitude, and right ascension/declination across historical and future dates. Use when calculating astronomical ephemerides or tracking planetary aspects.
---

# NASA JPL Horizons Ephemeris Data Retrieval & Celestial Mechanics

## Overview
Originated from the Gann Ephemeris project (`D:\ephemeris`), this skill defines the protocol for querying NASA JPL Horizons REST API to obtain geocentric, apparent ecliptic coordinates for astronomical and financial harmonic calculations.

---

## 1. NASA JPL Horizons REST API Configuration
- **Endpoint**: `https://ssd.jpl.nasa.gov/api/horizons.api`
- **Center**: `'500@399'` (Geocentric, Earth center).
- **Ephemeris Type**: `OBSERVER`
- **Quantity Code**: `QUANTITIES='1'` (Astrometric / Apparent Ecliptic Longitude and Latitude).
- **Body Identifiers**:
  - Sun: `'10'`
  - Moon: `'301'`
  - Mercury: `'199'`
  - Venus: `'299'`
  - Mars: `'499'`
  - Jupiter: `'599'`
  - Saturn: `'699'`
  - Uranus: `'799'`
  - Neptune: `'899'`
  - Pluto: `'999'`

---

## 2. Parsing Ecliptic Coordinates
NASA JPL returns text-delimited tables between `$$SOE` (Start of Ephemeris) and `$$EOE` (End of Ephemeris):
- Extract **ObsSub-LON** (Apparent Ecliptic Longitude $\lambda$, $0^\circ \le \lambda < 360^\circ$).
- Extract **ObsSub-LAT** (Apparent Ecliptic Latitude $\beta$).
- Extract daily motion / speed in longitude ($d\lambda / dt$). Identify retrograde stations when velocity flips from positive to negative.
