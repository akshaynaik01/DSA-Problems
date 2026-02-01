"""
Maximum Subarray Problem
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum and return its sum.

LeetCode Problem #53
Also known as Kadane's Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxSubArray(nums):
    """
    Find the maximum sum of a contiguous subarray.
    
    Args:
        nums: List of integers
    
    Returns:
        Integer representing the maximum subarray sum
    """
    if not nums:
        return 0
    
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Either extend the existing subarray or start a new one
        current_sum = max(nums[i], current_sum + nums[i])
        # Update the maximum sum seen so far
        max_sum = max(max_sum, current_sum)
    
    return max_sum


# Test cases
if __name__ == "__main__":
    # Test 1: Normal case with positive and negative numbers
    nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result1 = maxSubArray(nums1)
    print(f"Input: {nums1}")
    print(f"Output: {result1}")  # Expected: 6 (subarray [4, -1, 2, 1])
    
    # Test 2: Single element
    nums2 = [5]
    result2 = maxSubArray(nums2)
    print(f"\nInput: {nums2}")
    print(f"Output: {result2}")  # Expected: 5
    
    # Test 3: All negative numbers
    nums3 = [-3, -2, -1]
    result3 = maxSubArray(nums3)
    print(f"\nInput: {nums3}")
    print(f"Output: {result3}")  # Expected: -1
    
    # Test 4: All positive numbers
    nums4 = [1, 2, 3, 4]
    result4 = maxSubArray(nums4)
    print(f"\nInput: {nums4}")
    print(f"Output: {result4}")  # Expected: 10
