from data_loader import load_ohlcv_data
from signal_generator import generate_signal
from position_sizing import calculate_position_size
from execution import simulate_execution
from metrics import sharpe, drawdown, cagr, hit_rate, turnover
from plot import plot_equity_curve

# 1. Load data
df = load_ohlcv_data(symbol="AAPL", interval="1m", start="2023-01-01")

# 2. Generate signal
df = generate_signal(df)

# 3. Position sizing
df = calculate_position_size(df)

# 4. Simulate execution
df = simulate_execution(df)

# 5. Print performance
print("Sharpe Ratio:", sharpe(df["pnl"]))
print("Max Drawdown:", drawdown(df["pnl"]))
print("CAGR:", cagr(df["pnl"]))
print("Turnover:", turnover(df))
print("Hit Rate:", hit_rate(df))

# 6. Plot
plot_equity_curve(df)
