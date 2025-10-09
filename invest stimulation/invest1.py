import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Investment Decision Simulator", layout="wide")
st.title("Investment Decision Simulator")

file_path = r"C:\Users\Cynth\invest stimulation\data.xlsx"
df = pd.read_excel(file_path, index_col=0, parse_dates=True)

tickers = st.sidebar.multiselect(
    "Select Assets",
    df.columns.tolist(),
    default=["AAPL", "BND"]
)

start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2021-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-01-01"))
initial_investment = st.sidebar.number_input("Initial Investment ($)", 1000, 100000, 10000)

weights = []
st.sidebar.subheader("Adjust Portfolio Weights (Total = 1)")
for ticker in tickers:
    w = st.sidebar.slider(f"{ticker} Weight", 0.0, 1.0, round(1/len(tickers), 2), 0.01)
    weights.append(w)

total_weight = sum(weights)
if total_weight == 0:
    weights = [1/len(weights)] * len(weights)
else:
    weights = [w / total_weight for w in weights]

price_data = df.loc[start_date:end_date, tickers]

normed = price_data / price_data.iloc[0]
portfolio_value = (normed @ weights) * initial_investment

returns = portfolio_value.pct_change().dropna()
volatility = returns.std() * np.sqrt(252)
cummax = portfolio_value.cummax()
drawdown = (portfolio_value - cummax) / cummax
max_drawdown = drawdown.min()

st.subheader("Cumulative Portfolio Returns")
st.line_chart(portfolio_value)

st.subheader("Risk Metrics")
st.write(f"Annualized Volatility: {volatility:.2%}")
st.write(f"Maximum Drawdown: {max_drawdown:.2%}")

st.subheader("Portfolio Weights")
st.bar_chart(pd.DataFrame(weights, index=tickers, columns=["Weight"]))


