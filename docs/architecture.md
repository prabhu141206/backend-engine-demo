# Backend Engine Architecture

## Objective

Build scalable multi-user execution infrastructure
for algorithmic trading systems.

Current focus:
- session orchestration
- symbol routing
- runtime isolation
- shared websocket architecture

NOT:
- real trading
- broker execution
- PnL systems

---

## Runtime Hierarchy

Application
│
├── SessionManager
├── MarketDataManager
├── SymbolRouter
├── UserSession
├── StrategyRuntime
└── SymbolContext

---

## Core Principle

Execution isolation unit:

(user + strategy + symbol)

Represented by:
SymbolContext