import threading
import random
import time

NUM_TICKERS = 1024
ORDER_TYPES = ["Buy", "Sell"]
MAX_QUANTITY = 100
MAX_PRICE = 100

class Order:
    def __init__(self, order_type, ticker, quantity, price):
        self.order_type = order_type
        self.ticker = ticker
        self.quantity = quantity
        self.price = price

    def __str__(self):
        return f"Order: {self.order_type}, Ticker: {self.ticker}, Quantity: {self.quantity}, Price: {self.price}"


class OrderBook:
    def __init__(self):
        self.buy_orders = [[] for _ in range(NUM_TICKERS)]
        self.sell_orders = [[] for _ in range(NUM_TICKERS)]
        self.lock = threading.Lock()
    def add_order(self, order_type, ticker, quantity, price):
        order = Order(order_type, ticker, quantity, price)

        with self.lock:
            if order_type == "Buy":
                self.buy_orders[ticker].append(order)
            else:
                self.sell_orders[ticker].append(order)
            print(f"Added order: {order}")

    def match_order(self):
        with self.lock:
            for ticker in range(NUM_TICKERS):
                buy_orders = self.buy_orders[ticker]
                sell_orders = self.sell_orders[ticker]

                buy_orders.sort(key=lambda x: x.price, reverse=True)
                sell_orders.sort(key=lambda x: x.price)

                buy_index = 0
                sell_index = 0

                while buy_index < len(buy_orders) and sell_index < len(sell_orders):
                    buy_order = buy_orders[buy_index]
                    sell_order = sell_orders[sell_index]

                    if buy_order.price >= sell_order.price:
                        trade_quantity = min(buy_order.quantity, sell_order.quantity)
                        print(f"Matched: Buy {buy_order.price} Sell {sell_order.price} for Ticker {ticker}, Quantity: {trade_quantity}")
                        buy_order.quantity -= trade_quantity
                        sell_order.quantity -= trade_quantity

                        if buy_order.quantity == 0:
                            buy_index += 1
                        if sell_order.quantity == 0:
                            sell_index += 1
                        self.buy_orders[ticker] = [order for order in self.buy_orders[ticker] if order.quantity > 0]
                        self.sell_orders[ticker] = [order for order in self.sell_orders[ticker] if order.quantity > 0]
                        buy_orders = self.buy_orders[ticker]
                        sell_orders = self.sell_orders[ticker]

                    elif buy_order.price < sell_order.price:
                        buy_index += 1
                    else:
                        sell_index += 1

def random_order_generator(order_book, num_orders=100):
    for _ in range(num_orders):
        order_type = random.choice(ORDER_TYPES)
        ticker = random.randint(0, NUM_TICKERS - 1)
        quantity = random.randint(1, MAX_QUANTITY)
        price = random.randint(1, MAX_PRICE)

        order_book.add_order(order_type, ticker, quantity, price)
        time.sleep(random.uniform(0.01, 0.1))

def trading_simulation(order_book, num_threads=5):
    threads = []
    for _ in range(num_threads):
        thread = threading.Thread(target=random_order_generator, args=(order_book,))
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    print("Order generation complete. Starting matching...")


    for _ in range(5):
        order_book.match_order()
        time.sleep(1)
    print("Matching complete.")

if __name__ == "__main__":
    order_book = OrderBook()
    trading_simulation(order_book)