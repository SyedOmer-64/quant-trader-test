def calculate_position_size(df, target_vol=0.02):
    df["vol"] = df["close"].pct_change().rolling(20).std()
    df["size"] = target_vol / df["vol"]
    df["size"] = df["size"].clip(upper=1.0)  # Avoid leverage
    df["size"] = df["size"].fillna(0)
    return df