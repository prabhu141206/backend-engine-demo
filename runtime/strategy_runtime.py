"""
Strategy Runtime
================

Represents one strategy runtime
for one user.

Example
-------
User 101 EMA Runtime

Purpose
-------
Groups all SymbolContexts belonging
to one strategy.

Responsibilities
----------------
- manage symbol contexts
- own strategy-specific execution
- manage strategy lifecycle
"""


class StrategyRuntime:

    def __init__(
        self,
        strategy_name
    ):

        self.strategy_name = (
            strategy_name
        )

        # symbol -> SymbolContext
        self.symbol_contexts = {}

    def get_all_contexts(self):

        """
        Return all SymbolContexts.
        """

        return self.symbol_contexts.values()
    
    def add_context(
        self,
        symbol,
        context
    ):

        """
        Register SymbolContext.
        """

        self.symbol_contexts[
            symbol
        ] = context

    def get_context(
        self,
        symbol
    ):

        """
        Fetch SymbolContext.
        """

        return self.symbol_contexts.get(
            symbol
        )

    def stop(self):

        """
        Stop strategy runtime.
        """

        print(
            f"[StrategyRuntime] "
            f"Stopping "
            f"{self.strategy_name}"
        )