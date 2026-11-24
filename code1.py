
def rod_cutting(price, n):
    # Create DP array
    dp = [0] * (n + 1)

    # Calculate maximum profit
    for i in range(1, n + 1):
        max_profit = 0

        for j in range(1, i + 1):
            max_profit = max(
                max_profit,
                price[j - 1] + dp[i - j]
            )

        dp[i] = max_profit

    return dp[n]


# Main program
price = [2, 5, 7, 8, 10]
n = 5

result = rod_cutting(price, n)

print("Maximum Profit:", result)
