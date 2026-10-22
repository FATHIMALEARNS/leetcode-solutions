def max_profit(prices):
  if not prices:
    return 0
  min_price = prices[0]    # Track lowest buy price
  max_profit = 0           # Track highest profit
  
  for price in prices:
    if price < min_price:
      min_price = price     # Update lowest buy price
    elif price - min_price > max_profit:
      max_profit = price - min_price    # Update max profit
  return max_profit
