# Q9: System Design - Quant Trading Architecture

## 🔧 Overview

This section outlines the architecture of the automated trading system, including components for backtesting, signal generation, execution, and risk management.

## 🧩 Components

1. **Data Layer**  
   - Market data (OHLCV)
   - Preprocessing pipeline

2. **Signal Generation**  
   - Model-based strategies (e.g., Granger Causality, Kelly)

3. **Backtesting Engine**  
   - Vectorized backtester implemented in Python

4. **Execution Layer**  
   - Simulated market order execution
   - Slippage and latency simulation

5. **Risk Management**  
   - Position sizing via Kelly Criterion
   - Exposure limits

6. **Monitoring & Logging**  
   - Log PnL, drawdowns, Sharpe, etc.

---

## 🖼️ Diagram

(Optionally, draw and include an architecture diagram here or use ASCII art.)
