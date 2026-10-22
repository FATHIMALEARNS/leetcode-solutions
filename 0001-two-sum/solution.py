def two_sum(nums, target):
    mp = {}  # hashmap to store: {number: index}
    
    # Loop through the list, getting both the index (i) and the value (num)
    for i, num in enumerate(nums):
        diff = target - num
        if diff in mp:
            return [mp[diff], i]
        mp[num] = i
