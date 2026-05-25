"""
API Simulator
=============

Purpose
-------
Simulates frontend API requests.

This component acts as temporary
entry point into backend system.

Future:
-------
Will later become real FastAPI layer.
"""


class APISimulator:

    def __init__(self, session_manager):

        self.session_manager = (
            session_manager
        )

    def start_user_session(
        self,
        user_id,
        strategy_name,
        symbols
    ):

        """
        Simulate frontend request:
        start trading session.
        """

        print(
            f"\n[API] "
            f"Request received for "
            f"user={user_id}"
        )

        self.session_manager.start_session(
            user_id=user_id,
            strategy_name=strategy_name,
            symbols=symbols
        )