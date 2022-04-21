from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        Floyd Tortoise algorithm.
        Time - O(n)
        Space - O(1)
        """
        
        if not head:
            return False
        
        
        slow = fast = head
        

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next
            
            if fast == slow:
                return True

        return False

