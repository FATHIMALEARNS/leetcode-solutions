# 1. Two Sum

**Difficulty:** Easy  
**Topics:** Array, Hash Table

## Problem

Given an array of integers `nums` and an integer `target`, return the indices of the two numbers that add up to `target`.

You may assume that each input has exactly one solution, and you cannot use the same element twice.

## Approach

I used a hash map to store the numbers I have already seen along with their indices.

For each number:
1. Calculate its complement: `target - num`
2. Check if the complement already exists in the hash map.
3. If it exists, return the indices.
4. Otherwise, store the current number and its index.

## Complexity

- **Time:** O(n)
- **Space:** O(n)

## Solution

See [`solution.py`](solution.py)
