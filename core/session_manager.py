"""
Session Manager
===============

Purpose
-------
Central orchestration layer for user sessions.

Responsibilities
----------------
- create user sessions
- create strategy runtimes
- create symbol contexts
- register contexts into router
- register market subscriptions
- manage lifecycle
"""

from runtime.user_session import UserSession

from runtime.strategy_runtime import (
    StrategyRuntime
)

from runtime.symbol_context import (
    SymbolContext
)

from strategies.strategy_factory import (
    StrategyFactory
)


class SessionManager:

    def __init__(
        self,
        router,
        market_data_manager
    ):

        self.router = router

        self.market_data_manager = (
            market_data_manager
        )

        # user_id -> UserSession
        self.sessions = {}

    def start_session(
        self,
        user_id,
        strategy_name,
        symbols
    ):

        """
        Start user session.
        """

        print(
            f"\n[SessionManager] "
            f"Starting session for "
            f"user={user_id}"
        )

        # -----------------------------
        # Create User Session
        # -----------------------------
        session = UserSession(user_id)

        # Store session
        self.sessions[user_id] = session

        # -----------------------------
        # Create Strategy Runtime
        # -----------------------------
        strategy_runtime = StrategyRuntime(
            strategy_name
        )

        # Register runtime into session
        session.add_strategy_runtime(
            strategy_name,
            strategy_runtime
        )

        # -----------------------------
        # Create Symbol Contexts
        # -----------------------------
        for symbol in symbols:

            # Create isolated strategy instance
            strategy = (
                StrategyFactory.create_strategy(
                    strategy_name
                )
            )

            # Create isolated runtime context
            context = SymbolContext(
                user_id=user_id,
                strategy=strategy,
                symbol=symbol
            )

            # Register context into runtime
            strategy_runtime.add_context(
                symbol,
                context
            )

            # Register context into router
            self.router.register(
                symbol,
                context
            )

            # Register market subscription
            self.market_data_manager.add_symbol(
                symbol
            )

        print(
            f"[SessionManager] "
            f"Session started for "
            f"user={user_id}"
        )

    def stop_session(self, user_id):

        """
        Stop user session and cleanup
        all runtime resources.
        """

        session = self.sessions.get(user_id)

        if not session:

            print(
                f"[SessionManager] "
                f"User session not found"
            )

            return

        print(
            f"\n[SessionManager] "
            f"Stopping session for "
            f"user={user_id}"
        )

        # --------------------------------
        # Cleanup Strategy Runtimes
        # --------------------------------
        for runtime in (
            session.strategy_runtimes.values()
        ):

            # Cleanup SymbolContexts
            for context in (
                runtime.get_all_contexts()
            ):

                symbol = context.symbol

                # Remove router listener
                self.router.unregister(
                    symbol,
                    context
                )

                # Remove market subscription
                self.market_data_manager.remove_symbol(
                    symbol
                )

            # Stop runtime
            runtime.stop()

        # Stop user session
        session.stop()

        # Remove session tracking
        del self.sessions[user_id]

        print(
            f"[SessionManager] "
            f"Session stopped for "
            f"user={user_id}"
        )