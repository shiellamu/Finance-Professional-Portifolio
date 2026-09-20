# Bank Reconciliation

All figures are fictional.

## Process

Start with the book balance, identify timing differences, record bank-only items in the cashbook, investigate exceptions, then confirm adjusted balances agree.

## Sample exceptions

- DEP-002: $3,200 deposit in transit
- BANK-FEE: $85 bank charge
- CHQ-015: $980 outstanding cheque
- CHQ-016: $2,100 outstanding cheque
- BANK-INT: $42 bank interest

## Excel classification

=IF(C2=D2,"Matched",IF(AND(C2>0,D2=0),"Timing difference","Bank-only transaction"))

This demonstrates reconciliation controls and exception review.