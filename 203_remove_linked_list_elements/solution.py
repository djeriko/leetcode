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

    def arrayToList(self, arr):
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
    """
    Time = O(n)
    Space = O(1)
    """
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        result = ListNode()
        result.next = head
        
        current = result
        
        while current.next: 
            if current.next.val == val:
                current.next = current.next.next
            else:
                current = current.next

        return result.next
                
