# Component Responsibilities

## SymbolRouter

Responsibilities:
- route ticks
- maintain listeners

Must NOT:
- know users
- know strategies
- know websocket internals

---

## MarketDataManager

Responsibilities:
- websocket ownership
- subscriptions
- tick ingestion

Must NOT:
- contain strategy logic