# Data

This project uses the **Retail Price Optimization** dataset from Kaggle.

- Dataset: https://www.kaggle.com/datasets/suddharshan/retail-price-optimization

## Option A — Download manually (simple)

1. Download the dataset from Kaggle.
2. Put the CSV file(s) into:

```
data/raw/
```

> `data/raw/` is git-ignored by default to avoid committing datasets to GitHub.

## Option B — Download via Python (matches the notebook)

This repo includes a helper script that uses `kagglehub` (the same approach used in the notebook):

```bash
pip install -r requirements.txt
python -m src.download_data --out_dir data/raw
```

This downloads the Kaggle dataset and copies the first CSV found into `data/raw/`.
