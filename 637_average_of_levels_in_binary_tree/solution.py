from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    def fromList(values):
        def create(it):
            value = next(it)
            return None if value is None else TreeNode(value)
        
        if not values:
            return None
        
        it = iter(values)
        root = TreeNode(next(it))
        nextlevel = [root]
        try:
            while nextlevel:
                level = nextlevel
                nextlevel = []
                for node in level:
                    if node:
                        node.left = create(it)
                        node.right = create(it)
                        nextlevel += [node.left, node.right]
        except StopIteration:
            return root
        raise ValueError('Invalid list')
                   

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = [root]
        result = []
        while queue:
            level_sum = 0
            node_count = len(queue)
            for _ in range(node_count):
                node = queue.pop()
                if node.left:
                    queue.insert(0, node.left)
                if node.right:
                    queue.insert(0, node.right)
                level_sum += node.val
            
            result.append(level_sum / node_count)
        

        return result
        
        
     
