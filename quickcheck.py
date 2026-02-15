"""Quick sanity check for the dataset (beginner-friendly).

Usage:
  python -m src.quickcheck --data data/raw/<your_file>.csv
"""

from __future__ import annotations

import argparse
from pathlib import Path

import pandas as pd


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data", type=str, required=True)
    args = parser.parse_args()

    df = pd.read_csv(Path(args.data))
    print("Shape:", df.shape)
    print("\nColumns:")
    for c in df.columns:
        print(" -", c)

    print("\nMissing values (top 15):")
    print(df.isna().sum().sort_values(ascending=False).head(15))

    print("\nHead:")
    print(df.head(5).to_string(index=False))


if __name__ == "__main__":
    main()
