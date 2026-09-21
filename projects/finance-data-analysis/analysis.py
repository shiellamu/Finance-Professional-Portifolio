import pandas as pd
import matplotlib.pyplot as plt

INPUT = "../../datasets/finance_transactions.csv"
OUTPUT = "monthly_finance_summary.csv"
CHART = "monthly_contribution.png"

df = pd.read_csv(INPUT, parse_dates=["date"])

# Data-quality checks
required = {"date", "department", "category", "description", "amount", "type"}
missing_columns = required.difference(df.columns)
if missing_columns:
    raise ValueError(f"Missing columns: {sorted(missing_columns)}")

df["amount"] = pd.to_numeric(df["amount"], errors="raise")
if df["amount"].isna().any():
    raise ValueError("Amount contains missing values.")
if df["date"].isna().any():
    raise ValueError("Date contains missing values.")
if df.duplicated().any():
    raise ValueError("Duplicate transaction rows detected.")

df["month"] = df["date"].dt.to_period("M").astype(str)

monthly = (
    df.assign(
        income=df["amount"].where(df["type"].eq("Income"), 0),
        expense=df["amount"].where(df["type"].eq("Expense"), 0),
    )
    .groupby("month", as_index=False)[["income", "expense"]]
    .sum()
)

monthly["contribution"] = monthly["income"] - monthly["expense"]
monthly.to_csv(OUTPUT, index=False)

# Decision-useful chart
ax = monthly.plot(
    x="month",
    y="contribution",
    kind="bar",
    legend=False,
    title="Monthly Contribution — Fictional Practice Dataset",
)
ax.set_xlabel("Month")
ax.set_ylabel("Contribution")
plt.tight_layout()
plt.savefig(CHART, dpi=160)
plt.close()

print("Monthly summary:")
print(monthly.to_string(index=False))

print("\nExpense by category:")
expense_by_category = (
    df.loc[df["type"].eq("Expense")]
    .groupby("category")["amount"]
    .sum()
    .sort_values(ascending=False)
)
print(expense_by_category.to_string())

print("\nChecks passed: schema, numeric amounts, dates, missing values and duplicate rows.")
