import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(page_title="Investment Decision Simulator", layout="wide")
st.title("📊 Investment Decision Simulator")

# -----------------------------
# Load local Excel data
# -----------------------------
file_path = r"C:\Users\Cynth\invest stimulation\data.xlsx"
df = pd.read_excel(file_path, index_col=0, parse_dates=True)

# -----------------------------
# User selects assets and date range
# -----------------------------
tickers = st.sidebar.multiselect(
    "Select Assets",
    df.columns.tolist(),
    default=["AAPL", "BND"]
)

start_date = st.sidebar.date_input("Start Date", pd.to_datetime("2021-01-01"))
end_date = st.sidebar.date_input("End Date", pd.to_datetime("2023-01-01"))
initial_investment = st.sidebar.number_input("Initial Investment ($)", 1000, 100000, 10000)

# -----------------------------
# User sets portfolio weights
# -----------------------------
weights = []
st.sidebar.subheader("Adjust Portfolio Weights (Total = 1)")
for ticker in tickers:
    w = st.sidebar.slider(f"{ticker} Weight", 0.0, 1.0, round(1/len(tickers), 2), 0.01)
    weights.append(w)

# Normalize weights to sum to 1
total_weight = sum(weights)
if total_weight == 0:
    weights = [1/len(weights)] * len(weights)
else:
    weights = [w / total_weight for w in weights]

# -----------------------------
# Filter data by selected dates and assets
# -----------------------------
price_data = df.loc[start_date:end_date, tickers]

# -----------------------------
# Portfolio calculation
# -----------------------------
normed = price_data / price_data.iloc[0]  # Normalize to start at 1
portfolio_value = (normed @ weights) * initial_investment

# Risk metrics
returns = portfolio_value.pct_change().dropna()
volatility = returns.std() * np.sqrt(252)  # Annualized volatility
cummax = portfolio_value.cummax()
drawdown = (portfolio_value - cummax) / cummax
max_drawdown = drawdown.min()

# -----------------------------
# Visualization
# -----------------------------
st.subheader("📈 Cumulative Portfolio Returns")
st.line_chart(portfolio_value)

st.subheader("📊 Risk Metrics")
st.write(f"Annualized Volatility: {volatility:.2%}")
st.write(f"Maximum Drawdown: {max_drawdown:.2%}")

st.subheader("💡 Portfolio Weights")
st.bar_chart(pd.DataFrame(weights, index=tickers, columns=["Weight"]))


