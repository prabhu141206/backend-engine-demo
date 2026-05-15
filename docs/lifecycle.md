# Runtime Lifecycle

## User Session Start

1. API receives user_id
2. SessionManager creates UserSession
3. StrategyRuntime initialized
4. SymbolContexts created
5. Router registration occurs
6. Subscription registry updated
7. Websocket subscribes if required

---

## User Session Stop

1. Contexts removed
2. Router cleanup
3. Registry counts reduced
4. Websocket unsubscribes if unused
5. Session destroyed