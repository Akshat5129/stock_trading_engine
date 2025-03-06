# Real-Time Stock Trading Engine

A real-time stock trading engine for matching buy and sell orders. It adheres to strict constraints, specifically avoiding the use of dictionaries, maps, or equivalent data structures. The engine is designed to handle concurrent access from multiple threads, simulating a real-world environment with multiple stockbrokers.

## Features

*   **Order Matching:** Matches buy and sell orders based on price and quantity. A buy order must have a price greater than or equal to the lowest available sell price for a match to occur.
*   **Scalable Ticker Support:** Supports 1,024 different stock tickers.
*   **Random Order Generation:** Simulates realistic stock trading by generating random buy and sell orders with varying prices, quantities, and tickers.
*   **Performance:** The `match_order` function is designed to have a time complexity of O(n), where 'n' is the total number of orders.
  
## Design

The stock trading engine is composed of the following classes:

*   **`Order`:** Represents a single buy or sell order, containing information such as order type, ticker symbol, quantity, and price.
*   **`OrderBook`:** Manages the buy and sell orders for all tickers. It provides methods for adding orders (`add_order`) and matching orders (`match_order`).
    *   `buy_orders`: A list of lists, representing the buy orders for each ticker. `buy_orders[ticker]` holds a list of buy orders for that specific ticker. Orders are stored without using dictionary-like constructs.
    *   `sell_orders`: Similar to `buy_orders`, but holds sell orders.
    *   `lock`: A `threading.Lock` object used to synchronize access to the `buy_orders` and `sell_orders` lists, ensuring thread safety.

## Time Complexity

The `match_order` function aims for O(n) time complexity, where n is the total number of orders.  This is achieved by iterating through each ticker.  A trade-off is sorting buy/sell arrays using a traditional sorting algorithm with a time complexity of O(k log k) where k is the size of the individual buy or sell order array.

## Usage

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Akshat5129/stock_trading_engine.git
    cd stock_trading_engine
    ```

2.  **Run the simulation:**

    ```bash
    python stock_trading_engine.py
    ```

    This will start the stock trading engine simulation, which will generate random orders, match them, and print the details of the trades executed.

## Thread Safety

The `OrderBook` class uses a `threading.Lock` to ensure that only one thread can modify the order book at a time. This prevents race conditions and data corruption when multiple threads are adding or matching orders concurrently.

## Dependencies

*   Python 3.6+
*   `threading` (standard library)
*   `random` (standard library)
*   `time` (standard library)

## Future Enhancements

*   **More Realistic Implementation:** Implementation of more sophisticated order generation strategies that simulate real-world market behavior (e.g., price momentum).
*   **Order Cancellation:** Functionality to cancel existing orders can be added.
*   **Persistence:** Implementation of a mechanism to persist orders and trades to a database or file.
*   **Unit Tests:** Unit tests to ensure correctness and robustness can be added.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.
