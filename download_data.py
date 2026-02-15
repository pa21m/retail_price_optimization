"""Download the Kaggle dataset used by this project.

This mirrors the notebook's approach (kagglehub.dataset_download).

Usage:
  python -m src.download_data --out_dir data/raw

Notes:
- You may be prompted to authenticate Kagglehub depending on your environment.
- The script copies the first CSV found in the downloaded dataset folder into out_dir.
"""

from __future__ import annotations

import argparse
import shutil
from pathlib import Path

import kagglehub


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out_dir", type=str, default="data/raw")
    parser.add_argument("--dataset", type=str, default="suddharshan/retail-price-optimization")
    args = parser.parse_args()

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    path = Path(kagglehub.dataset_download(args.dataset))
    csv_files = sorted(path.glob("*.csv"))

    if not csv_files:
        raise FileNotFoundError(f"No CSV files found in downloaded dataset folder: {path}")

    src = csv_files[0]
    dst = out_dir / src.name
    shutil.copy(src, dst)

    print(f"Downloaded to: {path}")
    print(f"Copied CSV to:  {dst}")


if __name__ == "__main__":
    main()
