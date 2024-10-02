#!/usr/bin/python3

def makeChange(coins, total):
    # Edge case: If total is 0 or less, return 0 immediately.
    if total <= 0:
        return 0
    
    # Initialize the dp array, with a large number representing an impossible case
    dp = [float('inf')] * (total + 1)
    
    # Base case: 0 coins are needed to make 0 amount
    dp[0] = 0
    
    # Loop through each coin in the list
    for coin in coins:
        for amount in range(coin, total + 1):
            # If it's possible to form the amount using this coin, update dp[amount]
            dp[amount] = min(dp[amount], dp[amount - coin] + 1)
    
    # If we were able to find a solution for the total, return it; otherwise return -1
    return dp[total] if dp[total] != float('inf') else -1

# Test cases
print(makeChange([1, 2, 25], 37))  # Output: 7
print(makeChange([1256, 54, 48, 16, 102], 1453))  # Output: -1

