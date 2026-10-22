# 217. Contains Duplicate

**Difficulty:** Easy  
**Topics:** Array, Hash Table, Sorting

🔗 [Solve on LeetCode](https://leetcode.com/problems/contains-duplicate/)

## Approach

Use a set to keep track of the numbers already seen. If a number is already in the set, it means the array contains a duplicate, so return `True`. Otherwise, add the number to the set. If no duplicates are found, return `False`.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Solution

See [`solution.py`](solution.py).
