# Phase 1 Progress Documentation

# Objective

Current goal is NOT real trading.

Current goal is building scalable
multi-user execution infrastructure.

The system currently validates:

- multi-user sessions
- shared websocket architecture
- symbol routing
- isolated execution contexts
- lifecycle cleanup
- strategy plugability

Using:
- fake websocket
- fake ticks
- dummy strategy

---

# Current Architecture

Application
│
├── API Simulator
│
├── SessionManager
│
├── MarketDataManager
│
├── SymbolRouter
│
├── SubscriptionRegistry
│
├── UserSession
│
├── StrategyRuntime
│
├── SymbolContext
│
└── Strategy

---

# Current Runtime Hierarchy

UserSession
│
└── StrategyRuntime
       │
       ├── SymbolContext
       │      └── Strategy Instance
       │
       └── SymbolContext
              └── Strategy Instance

---

# Components Built

## 1. FakeWebSocket

Purpose:
Simulates live market feed.

Responsibilities:
- generate fake ticks
- maintain subscriptions
- execute callbacks

---

## 2. TickGenerator

Purpose:
Generate fake market ticks.

Example:

{
    "symbol": "NIFTY",
    "price": 24500
}

---

## 3. SymbolRouter

Purpose:
Route ticks to interested listeners.

Maintains:

{
    "NIFTY": [context1, context2]
}

Responsibilities:
- register listeners
- unregister listeners
- distribute ticks

---

## 4. SubscriptionRegistry

Purpose:
Prevent duplicate websocket subscriptions.

Maintains reference counts.

Example:

{
    "NIFTY": 3
}

Meaning:
3 runtime contexts require NIFTY.

---

## 5. MarketDataManager

Purpose:
Own global market infrastructure.

Responsibilities:
- websocket ownership
- subscription management
- registry coordination
- tick forwarding

Important:
Only ONE websocket globally.

---

## 6. UserSession

Purpose:
Represents one user runtime container.

Responsibilities:
- own strategy runtimes
- manage user lifecycle

---

## 7. StrategyRuntime

Purpose:
Represents one strategy runtime for one user.

Example:
User 101 EMA Runtime

Responsibilities:
- own SymbolContexts
- manage strategy-level execution

---

## 8. SymbolContext

Most important runtime object.

Represents:

(user + strategy + symbol)

Example:

(User 101 + EMA + NIFTY)

Responsibilities:
- isolated execution state
- receive routed ticks
- delegate execution to strategy

---

## 9. BaseStrategy

Purpose:
Defines common strategy interface.

Example:

class BaseStrategy:
    def on_tick(self, tick):
        pass

---

## 10. DummyStrategy

Purpose:
Temporary strategy used for
architecture testing.

---

## 11. StrategyFactory

Purpose:
Dynamically create strategies.

Example:

create_strategy("EMA")

---

## 12. SessionManager

Purpose:
Central orchestration layer.

Responsibilities:
- create sessions
- create runtimes
- create contexts
- register subscriptions
- manage cleanup

---

## 13. APISimulator

Purpose:
Simulate frontend API requests.

Acts as temporary application entry point.

---

# Current Execution Flow

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
MarketDataManager
    ↓
SubscriptionRegistry
    ↓
WebSocket Subscription
    ↓
Tick Generation
    ↓
Router
    ↓
SymbolContext
    ↓
Strategy Execution

---

# Multi-User Validation Completed

Successfully tested:

User 101 → NIFTY
User 202 → NIFTY
User 303 → BANKNIFTY
User 404 → NIFTY + BANKNIFTY

Validated:
- shared subscriptions
- shared websocket
- isolated execution
- multi-user routing

---

# Lifecycle Cleanup Validation Completed

Successfully validated:

- session stop
- router cleanup
- context removal
- subscription decrement
- runtime destruction

Example:

Stopping User 101:
- removes User 101 contexts
- keeps NIFTY subscription alive
  because other users still require it

This validates:
reference-count-based lifecycle management.

---

# Important Architectural Principles

## 1. Shared Market Feed

Only one websocket exists globally.

---

## 2. Decoupled Components

WebSocket does not know strategies.
Router does not know websocket internals.
Strategies do not know infrastructure.

---

## 3. Runtime Isolation

Execution isolation unit is:

(user + strategy + symbol)

represented by SymbolContext.

---

## 4. Strategy Plugability

Strategies are interchangeable plugins.

Future strategies:
- EMA
- ORB
- VWAP

should integrate without changing:
- router
- websocket
- orchestration

---

# Current Status

Current system is now functioning as:

mini event-driven execution engine infrastructure

NOT:
simple trading bot.

---

# Next Planned Steps

- EventBus
- ConfigLoader
- Fake DB integration
- Real API layer
- Runtime monitoring
- Broker websocket integration
- EMA strategy extraction
- Candle engine
- State machine