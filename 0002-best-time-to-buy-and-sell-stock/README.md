# 121. Best Time to Buy and Sell Stock

**Difficulty:** Easy  
**Topics:** Array, Greedy

🔗 [Solve on LeetCode](https://leetcode.com/problems/best-time-to-buy-and-sell-stock/)

## Approach

Track the minimum stock price seen so far. For each price, calculate the profit if I sell on that day and update the maximum profit.

## Complexity

- **Time:** O(n)
- **Space:** O(1)

## Solution

See [`solution.py`](solution.py).
