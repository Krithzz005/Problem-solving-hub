def max_profit(prices: list[int]) -> int:
    """Track minimum price seen so far and max profit."""
    min_price = float('inf')
    best = 0
    for p in prices:
        if p < min_price:
            min_price = p
        elif p - min_price > best:
            best = p - min_price
    return best
