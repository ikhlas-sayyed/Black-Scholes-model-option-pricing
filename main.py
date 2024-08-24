import numpy as np
from scipy.stats import norm
import yfinance as yf

import yfinance as yf

stock_symbol = input("Enter stock symbol ")#"RELIANCE.NS"
data = yf.download(stock_symbol, start="2023-01-01", end="2023-08-01")

data['Daily Return'] = data['Adj Close'].pct_change()

volatility = data['Daily Return'].std() * np.sqrt(252)
print(f"Annualized Volatility: {volatility:.2%}")

def black_scholes(S, K, T, r, sigma, option_type='call'):
    d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = d1 - sigma * np.sqrt(T)

    if option_type == 'call':
        option_price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
    elif option_type == 'put':
        option_price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
    return option_price


S = live_price = yf.Ticker(stock_symbol).history(period="1d")['Close'].iloc[-1]  # Current stock price 
print(f"Current Stock Price: ₹{S:.2f}")
K = int(input("Enter Strike price "))  # Strike price (Example)
T = int(input("Enter days of expration ")) / 365  # Time to expiration 
r = 0.05  # Risk-free interest rate (5%)
sigma = volatility  # Volatility calculated from historical data

# Calculate option price
call_price = black_scholes(S, K, T, r, sigma, option_type='call')
put_price = black_scholes(S, K, T, r, sigma, option_type='put')

print(f"Call Option Price: ₹{call_price:.2f}")
print(f"Put Option Price: ₹{put_price:.2f}")
