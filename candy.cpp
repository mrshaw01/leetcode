// https://leetcode.com/problems/candy/

#include <algorithm>
#include <vector>

class Solution {
public:
  int candy(std::vector<int> &ratings) {
    int n = ratings.size();
    if (n == 1)
      return 1; // Only one child gets one candy

    int totalCandies = 0;
    int leftToRightCandies = 1;
    std::vector<int> leftToRight(
        n, 1); // Store left-to-right candies in a single array

    // First pass: left to right
    for (int i = 1; i < n; ++i) {
      if (ratings[i] > ratings[i - 1]) {
        leftToRight[i] = leftToRight[i - 1] + 1;
      }
    }

    // Second pass: right to left and accumulate total candies
    int rightToLeftCandies = 1;
    totalCandies += leftToRight[n - 1]; // Start with the last child's candies

    for (int i = n - 2; i >= 0; --i) {
      if (ratings[i] > ratings[i + 1]) {
        rightToLeftCandies++;
      } else {
        rightToLeftCandies = 1;
      }
      totalCandies += std::max(leftToRight[i],
                               rightToLeftCandies); // Maximum of both passes
    }

    return totalCandies;
  }
};
