"""
Reverse a Singly Linked List
Given the head of a singly linked list, reverse the list, and return the reversed list.

LeetCode Problem #206
Time Complexity: O(n)
Space Complexity: O(1)
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverseList(head):
    """
    Reverse a singly linked list iteratively.
    
    Args:
        head: The head node of the linked list
    
    Returns:
        The new head of the reversed list
    """
    prev = None
    curr = head
    
    while curr:
        # Store the next node
        next_temp = curr.next
        # Reverse the link
        curr.next = prev
        # Move prev and curr one step forward
        prev = curr
        curr = next_temp
    
    return prev


def reverseListRecursive(head):
    """
    Reverse a singly linked list recursively.
    
    Args:
        head: The head node of the linked list
    
    Returns:
        The new head of the reversed list
    """
    # Base case: empty list or single node
    if not head or not head.next:
        return head
    
    # Reverse the rest of the list
    new_head = reverseListRecursive(head.next)
    
    # Make the next node point to current node
    head.next.next = head
    # Disconnect the current node from the list
    head.next = None
    
    return new_head


def printList(head):
    """Helper function to print the linked list"""
    values = []
    curr = head
    while curr:
        values.append(str(curr.val))
        curr = curr.next
    return " -> ".join(values) if values else "Empty"


# Test cases
if __name__ == "__main__":
    # Test 1: Reverse [1, 2, 3, 4, 5]
    head1 = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    print(f"Original: {printList(head1)}")
    reversed_head1 = reverseList(head1)
    print(f"Reversed: {printList(reversed_head1)}")  # Expected: 5 -> 4 -> 3 -> 2 -> 1
    
    # Test 2: Reverse [1, 2]
    head2 = ListNode(1, ListNode(2))
    print(f"\nOriginal: {printList(head2)}")
    reversed_head2 = reverseList(head2)
    print(f"Reversed: {printList(reversed_head2)}")  # Expected: 2 -> 1
    
    # Test 3: Single node
    head3 = ListNode(1)
    print(f"\nOriginal: {printList(head3)}")
    reversed_head3 = reverseList(head3)
    print(f"Reversed: {printList(reversed_head3)}")  # Expected: 1
