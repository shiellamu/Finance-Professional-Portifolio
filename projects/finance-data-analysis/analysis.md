# Finance Data Analysis — Reproducible Practice Analysis

**Dataset:** `datasets/finance_transactions.csv`  
**Period:** January–April 2026  
**Status:** Fictional practice case

## Data-quality checks

- 16 transactions reviewed.
- No blank fields are present in the supplied records.
- Dates use a consistent ISO format.
- Amounts are positive transaction values.
- Transaction types are Income or Expense.
- The dataset is suitable for monthly, departmental and category aggregation.

## Monthly summary

| Month | Income | Expense | Contribution |
|---|---:|---:|---:|
| 2026-01 | 26,800 | 6,050 | 20,750 |
| 2026-02 | 23,300 | 7,400 | 15,900 |
| 2026-03 | 25,900 | 7,200 | 18,700 |
| 2026-04 | 17,400 | 10,220 | 7,180 |
| **Total** | **93,400** | **30,870** | **62,530** |

## Expense analysis

| Category | Expense |
|---|---:|
| Payroll | 8,800 |
| Marketing | 7,700 |
| Inventory | 10,600 |
| Utilities | 3,770 |
| **Total** | **30,870** |

Inventory is the largest expense category in this small sample, followed by payroll and marketing.

## Findings

- January records the highest monthly contribution at 20,750.
- April records the lowest contribution at 7,180.
- April combines the lowest monthly income in the dataset with the highest monthly expense.
- Inventory is the largest expense category over the four-month period.
- The dataset supports identifying April as an investigation point, but it does **not** establish why income fell or expenses increased.

## Management questions

Before drawing operational conclusions, investigate:

1. What caused the April reduction in sales and service income?
2. What drove the higher April expense level?
3. Were April inventory and marketing costs planned or exceptional?
4. Are there timing or cut-off effects?
5. Do transaction totals agree to the underlying ledger?

## Reproducibility

The companion `analysis.py` should reproduce the monthly summary, validate the data, export a CSV and generate at least one decision-useful chart.

## Portfolio evidence

- Completed Python script
- Reproducible monthly summary CSV
- Decision-useful chart
- Data-quality checks
- Findings note
- Methodology and limitations

> All figures are fictional. This project demonstrates analytical workflow rather than representing an actual organisation's financial results.
