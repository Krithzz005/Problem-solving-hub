"""
Problem: Best Time to Buy and Sell Stock
Approach: Single pass min tracking
Time Complexity: O(n)
Space Complexity: O(1)
"""

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


if __name__ == '__main__':
    # Quick sanity check for Best Time to Buy and Sell Stock
    print('Tested best_time_to_buy_sell_stock.py (Best Time to Buy and Sell Stock)')
