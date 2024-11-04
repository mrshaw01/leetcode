# https://leetcode.com/problems/candy

ratings = [0, 1, 2, 3, 2, 1]


def candy(ratings):
    n = len(ratings)
    candies = [1] * n  # Each child gets at least one candy initially

    # First pass: left to right
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1

    # Second pass: right to left
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)

    return sum(candies)


print(candy(ratings))
