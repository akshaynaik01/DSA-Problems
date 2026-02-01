"""
Two Sum Problem
Given an array of integers nums and an integer target, 
return the indices of the two numbers that add up to target.
You may assume that each input has exactly one solution, 
and you cannot use the same element twice.

LeetCode Problem #1
Time Complexity: O(n)
Space Complexity: O(n)
"""

def twoSum(nums, target):
    """
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        List containing indices of two numbers that add up to target
    """
    # Dictionary to store value and its index
    num_map = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists in map
        if complement in num_map:
            return [num_map[complement], i]
        
        # Store current number and its index
        num_map[num] = i
    
    return []


# Test cases
if __name__ == "__main__":
    # Test 1
    nums1 = [2, 7, 11, 15]
    target1 = 9
    result1 = twoSum(nums1, target1)
    print(f"Input: nums = {nums1}, target = {target1}")
    print(f"Output: {result1}")  # Expected: [0, 1]
    
    # Test 2
    nums2 = [3, 2, 4]
    target2 = 6
    result2 = twoSum(nums2, target2)
    print(f"\nInput: nums = {nums2}, target = {target2}")
    print(f"Output: {result2}")  # Expected: [1, 2]
    
    # Test 3
    nums3 = [3, 3]
    target3 = 6
    result3 = twoSum(nums3, target3)
    print(f"\nInput: nums = {nums3}, target = {target3}")
    print(f"Output: {result3}")  # Expected: [0, 1]
