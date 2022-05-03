from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def insert(self, head, item):
        temp = ListNode(item)

        if head == None:
            head = temp
        else:
            ptr = head
            while ptr.next != None:
                ptr = ptr.next
            ptr.next = temp

        return head 

    def fromList(self, arr):
        head = None
        for i in range(0, len(arr)):
            head = self.insert(head, arr[i])

        return head

    def toList(self):
        result = []
        head = self
        while head:
            result.append(head.val)
            head = head.next
            
        return result
        



class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        """
        Time: O(n)
        Space: O(1)
        """
        res = result = ListNode(0)
        
        while l1 and l2:
            if l1.val <= l2.val:
                result.next = l1
                l1 = l1.next
            else:
                result.next = l2
                l2 = l2.next
            result = result.next
            print(res.toList())
        
        if l1:
            result.next = l1
        if l2:
            result.next = l2
        
        return res.next
