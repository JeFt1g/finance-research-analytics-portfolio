# Formulas

Debt-to-income = `monthly debt payments / monthly income`

Credit score starts at 600 and adjusts for income, debt-to-income, credit history, missed payments, existing debt, employment status, and loan amount relative to income.

Default probability = `1 / (1 + exp((credit_score - 620) / 55))`, plus penalties for missed payments, high debt-to-income, unemployment, and loan pressure.

Risk categories:

- Low risk: below 12%.
- Medium risk: 12% to below 25%.
- High risk: 25% to below 45%.
- Very high risk: 45% or above.

