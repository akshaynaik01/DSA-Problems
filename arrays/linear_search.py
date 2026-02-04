"""
Linear Search Algorithm

Problem: Find the index of a target element in an array using linear search.
Time Complexity: O(n)
Space Complexity: O(1)

Description:
Linear search is a simple searching algorithm that checks every element in the array
sequentially until the target element is found or the end of the array is reached.
"""

def linear_search(arr, target):
    """
    Search for target in array using linear search.
    
    Args:
        arr: List of elements to search
        target: Element to find
    
    Returns:
        Index of target if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_all(arr, target):
    """
    Find all indices of target in array.
    
    Args:
        arr: List of elements to search
        target: Element to find
    
    Returns:
        List of indices where target is found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


# Test cases
if __name__ == "__main__":
    # Test case 1: Element exists
    arr1 = [4, 2, 8, 1, 9, 5]
    target1 = 8
    result1 = linear_search(arr1, target1)
    print(f"Test 1 - Search {target1} in {arr1}")
    print(f"Result: Index {result1}")
    print(f"Expected: 2\n")
    
    # Test case 2: Element doesn't exist
    arr2 = [4, 2, 8, 1, 9, 5]
    target2 = 7
    result2 = linear_search(arr2, target2)
    print(f"Test 2 - Search {target2} in {arr2}")
    print(f"Result: Index {result2}")
    print(f"Expected: -1\n")
    
    # Test case 3: Multiple occurrences
    arr3 = [1, 2, 3, 2, 4, 2, 5]
    target3 = 2
    result3 = linear_search_all(arr3, target3)
    print(f"Test 3 - Find all {target3} in {arr3}")
    print(f"Result: Indices {result3}")
    print(f"Expected: [1, 3, 5]\n")
    
    # Test case 4: Empty array
    arr4 = []
    target4 = 5
    result4 = linear_search(arr4, target4)
    print(f"Test 4 - Search {target4} in {arr4}")
    print(f"Result: Index {result4}")
    print(f"Expected: -1")
