import pandas as pd

def generate_signal(df, lookback=20, threshold=1.0):
    df["mean"] = df["close"].rolling(lookback).mean()
    df["std"] = df["close"].rolling(lookback).std()
    df["z_score"] = (df["close"] - df["mean"]) / df["std"]
    df["signal"] = (df["z_score"] < -threshold).astype(int)  # Long-only
    return df
