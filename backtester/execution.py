def simulate_execution(df, cost=0.001, slippage=0.0005, latency=1):
    df["exec_price"] = df["close"].shift(latency) * (1 + slippage)
    df["trade"] = df["signal"].diff().fillna(0)
    df["executed"] = df["trade"] * df["exec_price"]
    df["pnl"] = df["signal"].shift(1) * df["close"].pct_change() * df["size"].shift(1)
    df["pnl"] -= abs(df["trade"]) * (cost + slippage)
    return df
