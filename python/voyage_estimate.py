"""Shipping Voyage Estimate Tool.

This script calculates a simplified voyage estimate for shipping operations.
It is designed as a portfolio project for shipping, freight and commodity trading roles.
"""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Dict, Any

import pandas as pd


def calculate_voyage_estimate(row: pd.Series) -> Dict[str, Any]:
    """Calculate voyage economics from one row of input assumptions."""
    freight_revenue = float(row["freight_revenue"])
    sea_days = float(row["sea_days"])
    port_days = float(row["port_days"])
    daily_consumption = float(row["daily_consumption"])
    bunker_price = float(row["bunker_price"])
    port_costs = float(row["port_costs"])
    canal_costs = float(row["canal_costs"])
    other_costs = float(row["other_costs"])
    commission_rate = float(row["commission_rate"])

    total_days = sea_days + port_days
    bunker_cost = sea_days * daily_consumption * bunker_price
    commission = freight_revenue * commission_rate
    total_voyage_costs = bunker_cost + port_costs + canal_costs + other_costs + commission
    profit_loss = freight_revenue - total_voyage_costs
    tce = profit_loss / total_days if total_days else 0

    return {
        "voyage_name": row.get("voyage_name", "Unnamed voyage"),
        "freight_revenue": freight_revenue,
        "total_days": total_days,
        "bunker_cost": bunker_cost,
        "port_costs": port_costs,
        "canal_costs": canal_costs,
        "other_costs": other_costs,
        "commission": commission,
        "total_voyage_costs": total_voyage_costs,
        "profit_loss": profit_loss,
        "tce_per_day": tce,
    }


def run_estimate(input_path: str | Path, output_path: str | Path) -> pd.DataFrame:
    """Run voyage estimate from a CSV file and save results."""
    input_path = Path(input_path)
    output_path = Path(output_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    df = pd.read_csv(input_path)
    results = [calculate_voyage_estimate(row) for _, row in df.iterrows()]
    result_df = pd.DataFrame(results)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    result_df.to_csv(output_path, index=False)

    return result_df


def print_summary(result_df: pd.DataFrame) -> None:
    """Print a clear business summary."""
    for _, row in result_df.iterrows():
        print("\nVoyage Estimate Summary")
        print("-----------------------")
        print(f"Voyage: {row['voyage_name']}")
        print(f"Freight revenue: {row['freight_revenue']:,.2f} USD")
        print(f"Total voyage days: {row['total_days']:,.2f}")
        print(f"Bunker cost: {row['bunker_cost']:,.2f} USD")
        print(f"Total voyage costs: {row['total_voyage_costs']:,.2f} USD")
        print(f"Profit/Loss: {row['profit_loss']:,.2f} USD")
        print(f"TCE: {row['tce_per_day']:,.2f} USD/day")

        if row["profit_loss"] > 0:
            print("Interpretation: the voyage is profitable under the current assumptions.")
        else:
            print("Interpretation: the voyage is loss-making under the current assumptions.")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run a simplified shipping voyage estimate.")
    parser.add_argument("--input", required=True, help="Path to input CSV file.")
    parser.add_argument("--output", default="outputs/voyage_estimate_results.csv", help="Path to output CSV file.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    result = run_estimate(args.input, args.output)
    print_summary(result)
    print(f"\nResults saved to: {Path(args.output).resolve()}")
