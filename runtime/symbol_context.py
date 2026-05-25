"""
Symbol Context
==============

Represents isolated execution runtime for:

(user + strategy + symbol)
"""


class SymbolContext:

    def __init__(
        self,
        user_id,
        strategy,
        symbol
    ):

        self.user_id = user_id

        self.strategy = strategy

        self.symbol = symbol

    def on_tick(self, tick):

        """
        Receive routed tick from router.
        """

        print(
            f"[Context] "
            f"User={self.user_id} "
            f"received tick"
        )

        # Delegate tick to strategy
        self.strategy.on_tick(tick)