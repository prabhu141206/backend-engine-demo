"""
Subscription Registry
=====================

Purpose
-------
Tracks active symbol subscriptions across the system.

This component prevents duplicate websocket subscriptions
by maintaining reference counts per symbol.

Example
-------
{
    "NIFTY": 2,
    "BANKNIFTY": 1
}

Meaning:
- NIFTY is required by 2 runtime contexts
- BANKNIFTY is required by 1 runtime context
"""


class SubscriptionRegistry:

    def __init__(self):

        # Stores active symbol reference counts
        #
        # Structure:
        # {
        #     "NIFTY": 2,
        #     "BANKNIFTY": 1
        # }
        self.subscriptions = {}

    def register_symbol(self, symbol):

        """
        Register symbol usage.

        Increases reference count for symbol.

        Parameters
        ----------
        symbol : str
            Market symbol.

        Returns
        -------
        bool

        True:
            Symbol appeared first time.
            Websocket SHOULD subscribe.

        False:
            Symbol already active.
            No websocket subscription needed.
        """

        # First appearance of symbol
        if symbol not in self.subscriptions:
            self.subscriptions[symbol] = 0

        # Increase active consumer count
        self.subscriptions[symbol] += 1

        print(
            f"[Registry] {symbol} count = "
            f"{self.subscriptions[symbol]}"
        )

        # First consumer requires websocket subscription
        return self.subscriptions[symbol] == 1

    def unregister_symbol(self, symbol):

        """
        Remove symbol usage.

        Decreases reference count.

        Parameters
        ----------
        symbol : str
            Market symbol.

        Returns
        -------
        bool

        True:
            No consumers left.
            Websocket SHOULD unsubscribe.

        False:
            Symbol still has active consumers.
        """

        # Ignore unknown symbols safely
        if symbol not in self.subscriptions:
            return False

        # Reduce active consumer count
        self.subscriptions[symbol] -= 1

        print(
            f"[Registry] {symbol} count = "
            f"{self.subscriptions[symbol]}"
        )

        # Final cleanup when no consumers remain
        if self.subscriptions[symbol] == 0:

            del self.subscriptions[symbol]

            return True

        return False