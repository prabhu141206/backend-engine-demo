import time
import threading

from Websocket.tick_generator import TickGenerator


class FakeWebSocket:

    def __init__(self):

        self.tick_generator = TickGenerator()

        self.subscribed_symbols = set()

        self.running = False

        self.on_tick_callback = None

    def subscribe(self, symbol):

        self.subscribed_symbols.add(symbol)

        print(f"[WS] Subscribed: {symbol}")

    def unsubscribe(self, symbol):

        self.subscribed_symbols.discard(symbol)

        print(f"[WS] Unsubscribed: {symbol}")

    def register_tick_callback(self, callback):

        self.on_tick_callback = callback

    def start(self):

        self.running = True

        thread = threading.Thread(target=self._run_loop)

        thread.daemon = True

        thread.start()

    def stop(self):

        self.running = False

    def _run_loop(self):

        while self.running:

            for symbol in self.subscribed_symbols:

                tick = self.tick_generator.generate_tick(symbol)

                if self.on_tick_callback:

                    self.on_tick_callback(tick)

            time.sleep(1)