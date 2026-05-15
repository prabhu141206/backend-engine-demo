import random
import time


class TickGenerator:

    def __init__(self):
        self.base_prices = {
            "NIFTY": 24500,
            "BANKNIFTY": 52500
        }

    def generate_tick(self, symbol):

        base_price = self.base_prices[symbol]

        movement = random.randint(-20, 20)

        new_price = base_price + movement

        self.base_prices[symbol] = new_price

        return {
            "symbol": symbol,
            "price": new_price,
            "timestamp": time.time()
        }