"""
Fibonacci Series - Dynamic Programming
Given an integer n, return the nth Fibonacci number.
Fibonacci series: 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
where F(n) = F(n-1) + F(n-2) with F(0)=0 and F(1)=1

LeetCode Problem #509
Time Complexity: O(n) for DP approaches
Space Complexity: O(1) for optimized DP or O(n) for memoization
"""

def fibonacciRecursive(n):
    """
    Fibonacci using naive recursion (Inefficient).
    Time Complexity: O(2^n)
    """
    if n <= 1:
        return n
    return fibonacciRecursive(n-1) + fibonacciRecursive(n-2)


def fibonacciMemo(n, memo=None):
    """
    Fibonacci using Memoization (Top-down DP).
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacciMemo(n-1, memo) + fibonacciMemo(n-2, memo)
    return memo[n]


def fibonacciTabulation(n):
    """
    Fibonacci using Tabulation (Bottom-up DP).
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if n <= 1:
        return n
    
    # Create a DP table
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    
    return dp[n]


def fibonacciOptimized(n):
    """
    Fibonacci using Space-Optimized DP.
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    if n <= 1:
        return n
    
    prev2 = 0  # F(0)
    prev1 = 1  # F(1)
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


# Test cases
if __name__ == "__main__":
    test_cases = [0, 1, 5, 10, 15]
    
    print("Fibonacci Number using different approaches:\n")
    
    for n in test_cases:
        print(f"F({n}):")
        print(f"  Recursive: {fibonacciRecursive(n)}")
        print(f"  Memoization: {fibonacciMemo(n)}")
        print(f"  Tabulation: {fibonacciTabulation(n)}")
        print(f"  Optimized: {fibonacciOptimized(n)}")
        print()
    
    print("\nComparison:")
    print(f"F(30) - Optimized: {fibonacciOptimized(30)}")  # Much faster than recursive
