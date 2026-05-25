"""
Strategy Factory
================

Purpose
-------
Creates strategy instances dynamically.

This allows strategies to remain:
- pluggable
- configurable
- decoupled from infrastructure
"""

from strategies.dummy_strategy import DummyStrategy


class StrategyFactory:

    @staticmethod
    def create_strategy(strategy_name):

        """
        Create strategy instance from strategy name.
        """

        strategies = {

            "DUMMY": DummyStrategy,
        }

        strategy_class = strategies.get(strategy_name)

        if not strategy_class:

            raise ValueError(
                f"Unknown strategy: {strategy_name}"
            )

        return strategy_class()