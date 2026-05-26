"""Bunker price sensitivity analysis for the Shipping Voyage Estimate Tool."""

from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

from voyage_estimate import calculate_voyage_estimate


def run_bunker_sensitivity(
    input_path: str | Path,
    output_path: str | Path,
    chart_path: str | Path,
    min_price: int = 400,
    max_price: int = 800,
    step: int = 50,
) -> pd.DataFrame:
    """Run TCE sensitivity analysis across bunker price scenarios."""
    input_path = Path(input_path)
    output_path = Path(output_path)
    chart_path = Path(chart_path)

    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")

    base_df = pd.read_csv(input_path)
    if base_df.empty:
        raise ValueError("Input file is empty.")

    base_row = base_df.iloc[0].copy()
    scenarios = []

    for bunker_price in range(min_price, max_price + 1, step):
        row = base_row.copy()
        row["bunker_price"] = bunker_price
        estimate = calculate_voyage_estimate(row)
        estimate["bunker_price"] = bunker_price
        scenarios.append(estimate)

    sensitivity_df = pd.DataFrame(scenarios)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    sensitivity_df.to_csv(output_path, index=False)

    chart_path.parent.mkdir(parents=True, exist_ok=True)
    plt.figure(figsize=(10, 5))
    plt.plot(sensitivity_df["bunker_price"], sensitivity_df["tce_per_day"], marker="o")
    plt.title("TCE Sensitivity to Bunker Price")
    plt.xlabel("Bunker price (USD/ton)")
    plt.ylabel("TCE (USD/day)")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig(chart_path, dpi=150)
    plt.close()

    return sensitivity_df


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run bunker price sensitivity analysis.")
    parser.add_argument("--input", required=True, help="Path to input CSV file.")
    parser.add_argument("--output", default="outputs/bunker_sensitivity.csv", help="Path to output CSV file.")
    parser.add_argument("--chart", default="charts/bunker_sensitivity.png", help="Path to output chart.")
    parser.add_argument("--min-price", type=int, default=400, help="Minimum bunker price scenario.")
    parser.add_argument("--max-price", type=int, default=800, help="Maximum bunker price scenario.")
    parser.add_argument("--step", type=int, default=50, help="Bunker price step.")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    df = run_bunker_sensitivity(
        input_path=args.input,
        output_path=args.output,
        chart_path=args.chart,
        min_price=args.min_price,
        max_price=args.max_price,
        step=args.step,
    )

    print("\nBunker Sensitivity Summary")
    print("--------------------------")
    print(df[["bunker_price", "profit_loss", "tce_per_day"]].to_string(index=False))
    print(f"\nSensitivity table saved to: {Path(args.output).resolve()}")
    print(f"Chart saved to: {Path(args.chart).resolve()}")
