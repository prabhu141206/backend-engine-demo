"""
Symbol Router
==============

Purpose
-------
Central tick distribution component.

This router receives market ticks and forwards them
to all interested runtime listeners.

Architecture Role
-----------------
Acts as the bridge between:
    MarketDataManager -> Runtime Contexts

Responsibilities
----------------
- Maintain symbol -> listener mapping
- Register listeners
- Unregister listeners
- Route ticks to listeners

Non Responsibilities
--------------------
Router must NOT:
- know users
- know strategies
- know websocket internals
- contain trading logic
- process indicators

Design Principle
----------------
Router is intentionally lightweight.
It behaves like a packet switch in networking systems.
"""


class SymbolRouter:

    def __init__(self):

        """
        Stores all symbol listeners.

        Structure:
        {
            "NIFTY": [listener1, listener2],
            "BANKNIFTY": [listener3]
        }
        """

        self.listeners = {}

    def register(self, symbol, listener):

        """
        Register a listener for a symbol.

        Parameters
        ----------
        symbol : str
            Market symbol.

        listener : object
            Any object implementing:
                on_tick(tick)

        Example
        -------
        router.register("NIFTY", context)
        """

        # Create listener list if symbol appears first time
        if symbol not in self.listeners:
            self.listeners[symbol] = []

        # Add listener to symbol
        self.listeners[symbol].append(listener)

        print(f"[Router] Registered listener for {symbol}")

    def unregister(self, symbol, listener):

        """
        Remove listener from symbol mapping.
        """

        # Ignore if symbol does not exist
        if symbol not in self.listeners:
            return

        # Remove listener safely
        if listener in self.listeners[symbol]:
            self.listeners[symbol].remove(listener)

        # Cleanup empty symbols
        if not self.listeners[symbol]:
            del self.listeners[symbol]

        print(f"[Router] Unregistered listener for {symbol}")

    def route_tick(self, tick):

        """
        Route incoming tick to all listeners
        subscribed to the tick symbol.

        Tick Example
        ------------
        {
            "symbol": "NIFTY",
            "price": 24500
        }
        """

        # Extract symbol from tick
        symbol = tick["symbol"]

        # No listeners interested in symbol
        if symbol not in self.listeners:
            return

        # Forward tick to all listeners
        for listener in self.listeners[symbol]:

            listener.on_tick(tick)




