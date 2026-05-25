import time

from core.symbol_router import SymbolRouter

from core.market_data_manager import (
    MarketDataManager
)

from core.session_manager import (
    SessionManager
)

from api.api_simulator import (
    APISimulator
)


# Create infrastructure
router = SymbolRouter()

market_manager = MarketDataManager(
    router
)

session_manager = SessionManager(
    router=router,
    market_data_manager=market_manager
)

api = APISimulator(
    session_manager
)


# Simulate frontend request
api.start_user_session(
    user_id=101,
    strategy_name="DUMMY",
    symbols=["NIFTY"]
)

api.start_user_session(
    user_id=202,
    strategy_name="DUMMY",
    symbols=["NIFTY"]
)


api.start_user_session(
    user_id=303,
    strategy_name="DUMMY",
    symbols=["BANKNIFTY"]
)


api.start_user_session(
    user_id=404,
    strategy_name="DUMMY",
    symbols=[
        "NIFTY",
        "BANKNIFTY"
    ]
)



# Start market infrastructure
market_manager.start()

# Let ticks flow for few seconds
time.sleep(5)

print("\n========== STOPPING USER 101 ==========")

session_manager.stop_session(101)

print("\n========== SESSION STOPPED ==========")

# Observe if ticks stop
time.sleep(5)


