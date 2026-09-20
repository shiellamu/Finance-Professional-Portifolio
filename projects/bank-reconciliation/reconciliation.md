# Bank Reconciliation

**Status: Practice project — all figures are fictional.**

Use `datasets/bank_reconciliation.csv` to practise transaction matching, exception identification and reconciliation controls.

## Objective

Reconcile book transactions to the bank statement, identify unmatched items, determine which items require cashbook adjustments, and document the final reconciliation.

## Process

1. Review the book and bank amounts.
2. Match transactions using references and amounts.
3. Identify timing differences.
4. Identify bank-only transactions.
5. Determine which items should be recorded in the cashbook.
6. Calculate the adjusted book balance.
7. Calculate the adjusted bank balance.
8. Confirm that the adjusted balances agree.
9. Document all reconciling items and proposed actions.

## Excel Classification Formula

You can use this as a starting point and test it against the data:

`=IF(C2=D2,"Matched",IF(AND(C2>0,D2=0),"Timing difference","Bank-only transaction"))`

Improve the classification if your analysis identifies cases that need more specific treatment.

## Your Tasks

- Build a transaction-matching worksheet.
- Identify every unmatched transaction.
- Separate timing differences from bank-only items.
- Calculate the total value of outstanding deposits.
- Calculate the total value of outstanding cheques.
- Calculate bank charges and bank interest requiring cashbook treatment.
- Prepare the reconciliation statement.
- Write a short control commentary explaining how the reconciliation reduces cash-management risk.

## Sample Exceptions

The fictional dataset includes examples such as:

- Deposit in transit
- Bank charge
- Outstanding cheque
- Bank interest

These are practice cases. Recalculate and verify the amounts yourself.

## Final Portfolio Deliverables

- Completed Excel reconciliation
- Reconciliation statement
- Exception log
- Proposed cashbook adjustments
- Short controls commentary

**Replace this fictional case with an approved real-world reconciliation example when appropriate.**
