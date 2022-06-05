from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, rigth=None):
        self.val = val
        self.left = left
        self.rigth = rigth


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        
        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                
                if not node.left and not node.right:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
            depth +=1
                    
         
        return depth
    
