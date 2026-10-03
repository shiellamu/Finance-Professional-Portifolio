# Finance Data Analysis

**Portfolio project · Practice case · Fictional data**

## Business question

What patterns in transaction-level finance data can be surfaced through structured data preparation, aggregation and visualisation?

## Dataset

Source: `datasets/finance_transactions.csv`

The dataset contains transaction-level records with dates, departments, categories, descriptions, amounts and transaction types.

> **Public-safe note:** all figures are fictional and are provided for portfolio practice.

## Analysis scope

Use Python/pandas to:

- Load and validate the data
- Inspect data types, missing values and duplicates
- Convert amounts to numeric
- Create a month field
- Aggregate income and expenses by month
- Calculate monthly contribution
- Analyse expenses by department and category
- Identify useful management questions
- Export a clean summary dataset
- Create at least one decision-useful chart

## Python workflow

The companion script is:

`analysis.py`

It intentionally contains guided TODOs so the portfolio demonstrates your own analytical work rather than presenting a black-box result.

## Required portfolio evidence

1. Completed Python script
2. Clean monthly summary CSV
3. At least one saved chart
4. Short findings note
5. Data-quality checks
6. Methodology and limitations

## Suggested outputs

- Monthly income vs expense trend
- Monthly contribution
- Expense by department
- Expense by category
- Transaction count and value checks

## Skills demonstrated

Python · pandas · Data validation · Aggregation · Financial analysis · Data visualisation · Management insight

## Limitations

The dataset is small and synthetic. It does not represent a complete general ledger, chart of accounts or production finance system. Findings should be treated as analytical practice rather than operational conclusions.

**Next step:** complete the TODOs in `analysis.py`, validate the outputs, and document your own findings.
