import pandas as pd
import matplotlib.pyplot as plt

INPUT = "../../datasets/finance_transactions.csv"
OUTPUT = "monthly_finance_summary.csv"

df = pd.read_csv(INPUT, parse_dates=["date"])
df["amount"] = pd.to_numeric(df["amount"], errors="raise")
df["month"] = df["date"].dt.to_period("M").astype(str)
summary = df.pivot_table(index="month", columns="type", values="amount", aggfunc="sum", fill_value=0).reset_index()
if "Income" not in summary: summary["Income"] = 0
if "Expense" not in summary: summary["Expense"] = 0
summary["contribution"] = summary["Income"] - summary["Expense"]
summary.to_csv(OUTPUT, index=False)
print("Total income: ${:,.2f}".format(df.loc[df["type"]=="Income","amount"].sum()))
print("Total expenses: ${:,.2f}".format(df.loc[df["type"]=="Expense","amount"].sum()))
print(summary)
ax = summary.plot(x="month", y=["Income","Expense","contribution"], kind="bar")
ax.set_title("Monthly Finance Performance")
ax.set_ylabel("Amount")
plt.tight_layout()
plt.savefig("monthly_finance_performance.png", dpi=160)
plt.close()