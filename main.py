# Stock Market Analysis - Brazil (PETR4 vs ITUB4)

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# -----------------------------
# 1. Download data
# -----------------------------
tickers = ['PETR4.SA', 'ITUB4.SA']

data = yf.download(tickers, start='2025-01-01', end='2025-06-27')

# -----------------------------
# 2. Extract closing prices
# -----------------------------
petro = data['Close']['PETR4.SA']
itau = data['Close']['ITUB4.SA']
dias = data.index

# -----------------------------
# 3. Basic analysis
# -----------------------------
print("Petro stats:")
print(petro.describe())

print("\nItaú stats:")
print(itau.describe())

# -----------------------------
# 4. Line chart
# -----------------------------
plt.figure(figsize=(12, 6))
plt.plot(dias, petro, label='Petrobras', linestyle='--')
plt.plot(dias, itau, label='Itaú')

plt.title('Stock Prices Comparison (2025)')
plt.xlabel('Date')
plt.ylabel('Price (R$)')
plt.legend()
plt.grid()
plt.show()

# -----------------------------
# 5. Histogram of variation
# -----------------------------
plt.figure(figsize=(12, 6))

plt.hist(petro.diff(), bins=50, alpha=0.5, label='Petrobras')
plt.hist(itau.diff(), bins=50, alpha=0.5, label='Itaú')

plt.title('Daily Variation Distribution')
plt.legend()
plt.grid()
plt.show()
