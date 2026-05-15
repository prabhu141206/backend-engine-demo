import time

from Websocket.fake_websocket import FakeWebSocket
from core.symbol_router import SymbolRouter


class DummyListener:

    def __init__(self, name):
        self.name = name

    def on_tick(self, tick):

        print(f"{self.name} received {tick}")


router = SymbolRouter()


listener1 = DummyListener("STRATEGY-1")
listener2 = DummyListener("STRATEGY-2")


router.register("NIFTY", listener1)
router.register("NIFTY", listener2)


ws = FakeWebSocket()

ws.register_tick_callback(router.route_tick)

ws.subscribe("NIFTY")

ws.start()


while True:
    time.sleep(1)