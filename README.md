# Retail Price Optimisation

Price optimization involves using historical data to determine the ideal price for a product or service, aiming to maximize profitability while balancing efficient pricing, profit objectives, and customer satisfaction.This project focuses on analysing retail sales data and optimising product pricing strategies using machine learning techniques.

## Project Overview

This project:
- Cleans and prepares retail transaction data
- Engineers relevant pricing and demand features
- Trains predictive models to estimate sales/profit impact
- Compares baseline vs optimised pricing strategies
- Quantifies potential uplift in revenue/profit

The notebook contains the full exploratory analysis, modelling pipeline, and optimisation logic.

## Repository Structure

```
.
├── notebooks/
│   └── retail_price_optimization.ipynb
├── data/
│   ├── raw/          # place original dataset here (git-ignored)
│   └── processed/
├── reports/
│   └── figures/
├── src/              # optional production scripts
├── requirements.txt
├── LICENSE
└── .gitignore
```

## Setup

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## How to Run

Open:

```
notebooks/retail_price_optimization.ipynb
```

Ensure your dataset is placed inside:

```
data/raw/
```

## Portfolio Write-Up (Problem → Approach → Result)

**Problem:** Retailers need data-driven pricing strategies to maximise revenue and profit while remaining competitive.

**Approach:** Clean transactional data, engineer demand-related features, train predictive models, and simulate optimised pricing scenarios to estimate uplift.

**Result:** The project quantifies the projected improvement in total profit under optimised pricing compared to baseline pricing, demonstrating measurable business impact.

**Credits:** 
- The tutorial reference: “Retail Price Optimization” Kaggle Notebook
https://www.kaggle.com/code/harshsingh2209/retail-price-optimization/input

- The dataset source on Kaggle:
https://www.kaggle.com/datasets/suddharshan/retail-price-optimization
