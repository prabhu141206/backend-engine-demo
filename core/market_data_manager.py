"""
Market Data Manager
===================

Purpose
-------
Centralized manager for market data infrastructure.

Responsibilities
----------------
- Own websocket connection
- Manage subscriptions
- Connect registry with websocket
- Forward ticks into router

This component acts as orchestration layer between:
- websocket
- router
- subscription registry
"""

from Websocket.fake_websocket import FakeWebSocket
from core.subscription_registry import SubscriptionRegistry


class MarketDataManager:

    def __init__(self, router):

        self.router = router

        self.registry = SubscriptionRegistry()

        self.websocket = FakeWebSocket()

        # Route websocket ticks into router
        self.websocket.register_tick_callback(
            self.router.route_tick
        )

    def add_symbol(self, symbol):

        """
        Register symbol usage in system.
        """

        should_subscribe = (
            self.registry.register_symbol(symbol)
        )

        if should_subscribe:

            self.websocket.subscribe(symbol)

    def remove_symbol(self, symbol):

        """
        Remove symbol usage from system.
        """

        should_unsubscribe = (
            self.registry.unregister_symbol(symbol)
        )

        if should_unsubscribe:

            self.websocket.unsubscribe(symbol)

    def start(self):

        """
        Start websocket system.
        """

        self.websocket.start()