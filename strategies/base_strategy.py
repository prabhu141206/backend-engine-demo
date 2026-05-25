"""
Base Strategy
=============

Defines common interface for all strategies.

All strategies must implement:
- on_tick()

Purpose
-------
Provides strategy plugability.
"""


class BaseStrategy:

    def on_tick(self, tick):

        raise NotImplementedError(
            "Strategy must implement on_tick()"
        )