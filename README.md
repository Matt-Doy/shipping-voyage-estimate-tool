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
