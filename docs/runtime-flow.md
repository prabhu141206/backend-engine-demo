# Runtime Flow

## Tick Flow

FakeWebSocket
    ↓
MarketDataManager
    ↓
SymbolRouter
    ↓
SymbolContext
    ↓
Strategy Instance

---

## Session Creation Flow

API Request
    ↓
SessionManager
    ↓
UserSession
    ↓
StrategyRuntime
    ↓
SymbolContext
    ↓
Router Registration
    ↓
Market Subscription