# https://leetcode.com/problems/median-of-two-sorted-arrays/
class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Ensure nums1 is the smaller array
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        total = m + n
        half = (total + 1) // 2
        low, high = 0, m

        i = 0
        j = 0

        while low <= high:
            i = (low + high) // 2
            j = half - i

            nums1LeftMax = float("-inf") if i == 0 else nums1[i - 1]
            nums1RightMin = float("inf") if i == m else nums1[i]
            nums2LeftMax = float("-inf") if j == 0 else nums2[j - 1]
            nums2RightMin = float("inf") if j == n else nums2[j]

            if nums1LeftMax <= nums2RightMin and nums2LeftMax <= nums1RightMin:
                # Correct partition found
                if total % 2:
                    return max(nums1LeftMax, nums2LeftMax)
                else:
                    return (max(nums1LeftMax, nums2LeftMax) + min(nums1RightMin, nums2RightMin)) / 2.0
            elif nums1LeftMax > nums2RightMin:
                high = i - 1
            else:
                low = i + 1

        raise ValueError("Input arrays are not valid.")
