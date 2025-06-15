import pandas as pd

def load_ohlcv_data(file_path=None, symbol="AAPL", start="2023-01-01", interval="1m"):
    if file_path:
        df = pd.read_csv(file_path, parse_dates=["datetime"])
    else:
        import yfinance as yf
        df = yf.download(symbol, start=start, interval=interval)
        df.reset_index(inplace=True)
        df.rename(columns={"Datetime": "datetime"}, inplace=True)
    
    df = df[["datetime", "Open", "High", "Low", "Close", "Volume"]]
    df.columns = [col.lower() for col in df.columns]
    df.dropna(inplace=True)
    return df
