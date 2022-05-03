from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: ListNode):
        slow = fast = head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow

    def reverseList(self, head: ListNode) -> ListNode:
        current = head
        prev = None
        
        while current:
            temp_next = current.next
            current.next = prev
            prev = current
            current = temp_next
        
        return prev
        
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = fast = head
        
        if not head:
            return None
        
        middle = self.middleNode(head)
        reverse = self.reverseList(middle)
        
        while reverse:
            if reverse.val != head.val:
                return False 
            reverse = reverse.next
            head = head.next
            
        return True

  
