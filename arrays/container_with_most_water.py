"""
Container With Most Water

Given n non-negative integers a1, a2, ..., an where each represents a point at coordinate (i, ai).
Find two lines that together with x-axis form a container such that the container contains the most water.

LeetCode Problem #11
Time Complexity: O(n)
Space Complexity: O(1)
"""

def maxArea(height):
    """
    Find the maximum area of container with two lines.
    
    Args:
        height: List[int] - list of integers representing heights
    
    Returns:
        int - maximum area
    
    Approach:
        - Use two pointers, one at the start and one at the end
        - Calculate the area between the two lines
        - Move the pointer pointing to the shorter line inward
        - Keep track of the maximum area seen so far
    """
    max_area = 0
    left = 0
    right = len(height) - 1
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        # Update max area
        max_area = max(max_area, current_area)
        
        # Move the pointer pointing to the shorter line
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


# Alternative approach using brute force (O(n^2))
def maxArea_bruteforce(height):
    """
    Brute force approach - try all pairs
    
    Time Complexity: O(n^2)
    Space Complexity: O(1)
    """
    max_area = 0
    
    for i in range(len(height)):
        for j in range(i + 1, len(height)):
            width = j - i
            current_height = min(height[i], height[j])
            current_area = width * current_height
            max_area = max(max_area, current_area)
    
    return max_area


# Test cases
if __name__ == "__main__":
    # Test case 1: Standard case
    test1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
    print(f"Test 1: {test1}")
    print(f"Two Pointer Result: {maxArea(test1)}")
    print(f"Brute Force Result: {maxArea_bruteforce(test1)}")
    print(f"Expected: 49\n")
    
    # Test case 2: Small array
    test2 = [1, 1]
    print(f"Test 2: {test2}")
    print(f"Two Pointer Result: {maxArea(test2)}")
    print(f"Brute Force Result: {maxArea_bruteforce(test2)}")
    print(f"Expected: 1\n")
    
    # Test case 3: Different heights
    test3 = [2, 3, 4, 5, 18, 17, 6]
    print(f"Test 3: {test3}")
    print(f"Two Pointer Result: {maxArea(test3)}")
    print(f"Brute Force Result: {maxArea_bruteforce(test3)}")
    print(f"Expected: 17\n")
    
    # Test case 4: Single element (edge case)
    test4 = [1, 0, 0]
    print(f"Test 4: {test4}")
    print(f"Two Pointer Result: {maxArea(test4)}")
    print(f"Brute Force Result: {maxArea_bruteforce(test4)}")
    print(f"Expected: 2\n")
    
    print("\n--- Algorithm Analysis ---")
    print("Two Pointer Approach:")
    print("- Time: O(n) - single pass with two pointers")
    print("- Space: O(1) - only constant space for pointers")
    print("\nBrute Force Approach:")
    print("- Time: O(n^2) - checking all pairs")
    print("- Space: O(1) - constant space")
