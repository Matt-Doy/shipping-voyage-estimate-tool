# Shipping Voyage Estimate Tool

> **Python · pandas · Excel · Shipping Operations**  
> Voyage P&L estimation · Freight cost modelling · Bunker consumption · Port costs · TCE calculation  
> *Built to demonstrate applied shipping economics for commodity trading and operations roles*

---

## Overview

This tool estimates the **financial performance of a shipping voyage** by modelling freight
revenues, bunker costs, port dues and canal fees across a defined route. It outputs a
simplified **Profit & Loss estimate** and **Time Charter Equivalent (TCE)** — the industry
standard metric for comparing voyage profitability across vessel types and routes.

Built as a portfolio project for roles in **shipping operations, commodity trading,
chartering, bunker procurement and maritime logistics**.

---

## What It Calculates

| Output | Description |
|---|---|
| **Gross Freight Revenue** | Worldscale rate × flat rate × cargo quantity |
| **Bunker Cost** | Voyage days × daily consumption × VLSFO/MGO price |
| **Port Dues & Canal Fees** | Per-port cost inputs (Suez, Panama, load/discharge) |
| **Voyage P&L** | Revenue minus all voyage costs |
| **TCE (Time Charter Equivalent)** | Net revenue per vessel-day — standard chartering metric |

---

## Business Context

In physical commodity trading and shipping, every cargo move starts with a **voyage
estimate** — can we make money on this trade? The TCE tells a charterer whether a voyage
is worth fixing versus the open market rate. Understanding voyage economics is fundamental
for:

- **Cargo operators** structuring FOB/CIF trades
- **Charterers** evaluating spot vs time charter decisions
- **Bunker traders** assessing the cost sensitivity of voyages to fuel price moves
- **Freight analysts** comparing route economics across vessel classes

A 10% move in bunker prices can swing voyage P&L by thousands of dollars per day.
This tool makes that sensitivity visible.

---

## Key Features

- Input vessel parameters: speed, daily consumption, vessel class (VLCC, Suezmax, Aframax, MR)
- Input route parameters: distance (nautical miles), load/discharge ports, canal transit
- Input market rates: Worldscale, VLSFO/MGO bunker price, port costs
- Compute voyage duration, bunker cost, total costs and net P&L
- Calculate TCE and compare against market benchmarks
- Sensitivity analysis: bunker price impact on TCE

---

## Repository Structure

```
shipping-voyage-estimate-tool/
│
├── src/
│   └── voyage_estimator.py     ← main estimation engine
│
├── notebooks/
│   └── voyage_estimate.ipynb   ← interactive walkthrough
│
├── data/
│   └── sample_routes.csv       ← sample route inputs
│
├── outputs/
│   └── sample_estimate.csv     ← example P&L output
│
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Quickstart

```bash
git clone https://github.com/Matt-Doy/shipping-voyage-estimate-tool.git
cd shipping-voyage-estimate-tool

python -m venv .venv
source .venv/bin/activate   # Mac/Linux
pip install -r requirements.txt

python src/voyage_estimator.py
```

---

## Tools

`Python` `pandas` `numpy` `Jupyter Notebook`

---

## Market Context

Key variables that drive voyage economics in practice:

- **VLSFO price** (currently ~$500-600/mt): largest single cost variable on long-haul voyages
- **Worldscale rates**: fluctuate with tonnage supply/demand — can move 20-30 WS points in a week
- **Canal fees**: Suez transit ~$500k-1M+ for VLCCs; significant route optionality question
- **Port turnaround time**: demurrage risk starts from NOR tender — every extra day costs

---

## Related Projects

→ [brent-wti-market-analysis](https://github.com/Matt-Doy/brent-wti-market-analysis) — crude oil price dynamics and spread analysis  
→ [commodity-trading-sql-analysis](https://github.com/Matt-Doy/commodity-trading-sql-analysis) — SQL queries for trade data  
→ [brazilian-soybean-export-dashboard](https://github.com/Matt-Doy/brazilian-soybean-export-dashboard) — South American commodity flows

---

## About

Built by **Mattéo Doyen** — Shipping & Trading Graduate (M2, IAE Nantes, 2026).  
[LinkedIn](https://www.linkedin.com/in/mattéo-doyen/) · [GitHub](https://github.com/Matt-Doy)
# Shipping Voyage Estimate Tool

## Overview

This project provides a simplified voyage estimate model for shipping operations and freight market analysis. It calculates bunker costs, port costs, canal costs, commissions, total voyage costs, profit/loss and Time Charter Equivalent (TCE).

The objective is to connect shipping market knowledge with practical Python and Excel/VBA automation skills.

## Business Context

Voyage estimation is a key task in shipping, chartering and freight trading. It helps compare the profitability of different voyages under several operational and market assumptions, including freight revenue, bunker prices, port days and vessel consumption.

This type of analysis is useful for:

- shipbroking;
- freight analysis;
- shipping operations;
- commodity logistics;
- chartering desks;
- maritime trading teams.

## Tools Used

- Python
- pandas
- numpy
- matplotlib
- Excel/VBA template logic

## Key Features

- Voyage cost calculation
- Bunker cost estimation
- Port and canal cost integration
- Commission calculation
- Profit and loss output
- TCE calculation
- Sensitivity analysis on bunker prices
- Scenario comparison
- Export of summary results

## Repository Structure

```text
shipping-voyage-estimate-tool/
|
├── python/
│   ├── voyage_estimate.py
│   └── sensitivity_analysis.py
|
├── excel_vba/
│   ├── voyage_estimate_vba.bas
│   └── excel_template_instructions.md
|
├── examples/
│   └── sample_voyage_case.csv
|
├── charts/
│   └── generated charts
|
├── outputs/
│   └── generated output files
|
├── README.md
├── requirements.txt
└── .gitignore
```

## How to Run

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Run the voyage estimate on the sample case:

```bash
python python/voyage_estimate.py --input examples/sample_voyage_case.csv --output outputs/voyage_estimate_results.csv
```

Run the bunker price sensitivity analysis:

```bash
python python/sensitivity_analysis.py --input examples/sample_voyage_case.csv --output outputs/bunker_sensitivity.csv --chart charts/bunker_sensitivity.png
```

## Main Formulas

### Bunker Cost

```text
Bunker Cost = Sea Days × Daily Consumption × Bunker Price
```

### Commission

```text
Commission = Freight Revenue × Commission Rate
```

### Total Voyage Costs

```text
Total Voyage Costs = Bunker Cost + Port Costs + Canal Costs + Other Costs + Commission
```

### Profit / Loss

```text
Profit / Loss = Freight Revenue - Total Voyage Costs
```

### Time Charter Equivalent

```text
TCE = Profit / Loss ÷ Total Voyage Days
```

## Sample Output

The model produces a table with:

- total voyage days;
- bunker cost;
- commission;
- total voyage costs;
- profit/loss;
- TCE per day.

## Business Interpretation

A higher bunker price reduces voyage profitability and lowers the TCE. The sensitivity analysis helps understand how exposed a voyage is to fuel price movements, which is particularly important in freight trading and chartering decisions.

## Future Improvements

Potential improvements include:

- adding laden and ballast legs;
- separating VLSFO and MGO consumption;
- adding port-by-port assumptions;
- adding demurrage/despatch calculation;
- adding a Streamlit dashboard;
- connecting to live bunker price data;
- building a complete Excel/VBA version.
