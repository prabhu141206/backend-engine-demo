"""
User Session
============

Represents runtime session for one user.

Purpose
-------
Acts as top-level execution container
for user-specific runtimes.

Responsibilities
----------------
- manage user runtime state
- own strategy runtimes
- manage user lifecycle

Future Responsibilities
-----------------------
- load configs
- manage user shutdown
- manage runtime cleanup
"""


class UserSession:

    def __init__(self, user_id):

        self.user_id = user_id

        # strategy_name -> runtime
        self.strategy_runtimes = {}

    def add_strategy_runtime(
        self,
        strategy_name,
        runtime
    ):

        """
        Register strategy runtime
        under user session.
        """

        self.strategy_runtimes[
            strategy_name
        ] = runtime

    def get_strategy_runtime(
        self,
        strategy_name
    ):

        """
        Fetch strategy runtime.
        """

        return self.strategy_runtimes.get(
            strategy_name
        )

    def stop(self):

        """
        Stop user session.

        Future:
        cleanup runtimes.
        """

        print(
            f"[UserSession] "
            f"Stopping session for "
            f"user={self.user_id}"
        )