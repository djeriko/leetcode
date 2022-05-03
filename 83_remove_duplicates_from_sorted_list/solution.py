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
        for i in range (0, len(arr)):
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
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        """
        Time: O(n)
        Space: O(1)
        """
        if head == None:
            return None
        
        result = head
        while result.next: 
            if result.next.val == result.val:
                result.next = result.next.next
            else:
                result = result.next

        return head

