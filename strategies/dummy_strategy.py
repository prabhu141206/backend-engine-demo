"""
Dummy Strategy
==============

Temporary fake strategy used for
architecture testing.

Purpose
-------
Validate strategy execution flow.
"""

from strategies.base_strategy import BaseStrategy


class DummyStrategy(BaseStrategy):

    def on_tick(self, tick):

        print(
            f"[DummyStrategy] "
            f"Processing tick: {tick}"
        )