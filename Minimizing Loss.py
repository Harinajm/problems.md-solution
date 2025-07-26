from typing import List, Tuple, Union

def minimize_loss(prices: List[int]) -> Union[Tuple[int, int, int], str]:
    """
    Calculates the minimum possible loss from buying and selling a house,
    where the house must be bought in one year and sold in a later year.


    Args:
        prices (list[int]): A list of distinct projected prices for a house.


    Returns:
        tuple[int, int, int] | str: A tuple containing the year to buy (1-based),
                                     the year to sell (1-based), and the minimum loss.
                                     Returns a string if no valid loss transaction is possible.
    """
    if not prices or len(prices) < 2:
        return "Not enough data to perform a transaction."


    # Create a list of tuples (price, original_year_index)
    # We use 1-based indexing for years as is common in such problems.
    prices_with_years = [(prices[i], i + 1) for i in range(len(prices))]


    # Sort the list based on price
    prices_with_years.sort()


    min_loss = float('inf')
    buy_year, sell_year = -1, -1


    # Iterate through the sorted list to find the minimum difference
    # between adjacent prices where the buy year comes before the sell year.
    for i in range(1, len(prices_with_years)):
        p_buy, y_buy = prices_with_years[i]
        p_sell, y_sell = prices_with_years[i-1]
       
        # A valid transaction requires buying before selling (y_buy < y_sell)
        # and the price must be a loss (p_buy > p_sell), which is guaranteed
        # by iterating through the sorted list.
        if y_buy < y_sell:
            loss = p_buy - p_sell
            if loss < min_loss:
                min_loss = loss
                buy_year = y_buy
                sell_year = y_sell


    if min_loss == float('inf'):
        return "No transaction resulting in a loss is possible."
   
    return (buy_year, sell_year, min_loss)


# --- Example Usage ---
if __name__ == "__main__":
    price_chart = [20, 15, 7, 2, 13]
   
    result = minimize_loss(price_chart)
   
    if isinstance(result, str):
        print(result)
    else:
        buy, sell, loss = result
        print(f"Price Chart: {price_chart}")
        print(f"Optimal Strategy to Minimize Loss:")
        print(f"  - Buy in Year:  {buy} (at price {price_chart[buy-1]})")
        print(f"  - Sell in Year: {sell} (at price {price_chart[sell-1]})")
        print(f"  - Minimum Loss: {loss}")


    print("-" * 20)
   
    price_chart_2 = [5, 10, 3]
    result_2 = minimize_loss(price_chart_2)
    if isinstance(result_2, str):
        print(result_2)
    else:
        buy, sell, loss = result_2
        print(f"Price Chart: {price_chart_2}")
        print(f"  - Buy in Year:  {buy} (at price {price_chart_2[buy-1]})")
        print(f"  - Sell in Year: {sell} (at price {price_chart_2[sell-1]})")
        print(f"  - Minimum Loss: {loss}")
