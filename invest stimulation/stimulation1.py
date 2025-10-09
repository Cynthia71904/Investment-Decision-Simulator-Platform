import numpy as np
import pandas as pd

def calculate_portfolio(price_data, initial_investment):
    weights = np.array([1/price_data.shape[1]]*price_data.shape[1])
    returns = price_data.pct_change().dropna()
    portfolio_returns = (returns * weights).sum(axis=1)
    portfolio_value = (1 + portfolio_returns).cumprod() * initial_investment
    volatility = portfolio_returns.std() * np.sqrt(252)
    max_drawdown = (portfolio_value / portfolio_value.cummax() - 1).min()
    return portfolio_value, volatility, max_drawdown

