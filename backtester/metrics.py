import numpy as np

def sharpe(pnl, freq=252*390):
    return np.mean(pnl) / np.std(pnl) * np.sqrt(freq) if np.std(pnl) != 0 else 0

def drawdown(pnl):
    cumulative = (1 + pnl).cumprod()
    peak = cumulative.cummax()
    dd = (cumulative - peak) / peak
    return dd.min()

def cagr(pnl, freq=252*390):
    total_return = (1 + pnl).prod()
    n_periods = len(pnl) / freq
    return total_return ** (1/n_periods) - 1

def hit_rate(df):
    return (df["pnl"] > 0).sum() / (df["pnl"] != 0).sum()

def turnover(df):
    return abs(df["trade"]).sum() / df["size"].sum()
