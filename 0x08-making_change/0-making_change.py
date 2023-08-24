#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a table to store the minimum number of coins foe each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(1, total + 1):
        for coin in coins:
            if i - coin >= 0:
                dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    return dp[total]


# Test the function
coins = [1, 2, 5]
total = 11

print(makeChange(coins, total))  # Output: 3
