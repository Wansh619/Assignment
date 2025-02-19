# Data Harmonization Engine

## Overview
This Python script harmonizes multi-source product catalog data into a standardized schema. It processes heterogeneous CSV files, maps columns to a predefined schema, cleans and normalizes data, and outputs a cleaned CSV file.

---

## Features
1. **Schema Mapping**: Maps varying column names (e.g., `price_usd`, `price (EUR)`) to a standardized format.
2. **Data Cleaning**: Handles missing fields, typos, duplicates, and unit conversions.
3. **Category Normalization**: Resolves ambiguous categories using fuzzy logic.
4. **Scalability**: Efficiently processes large datasets.

---

## Requirements
- Python 3.8+
- Libraries: `pandas`, `fuzzywuzzy`, `python-Levenshtein`

Install dependencies:
```bash
pip install pandas fuzzywuzzy python-Levenshtein