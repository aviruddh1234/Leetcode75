# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        res = []

        q = collections.deque()
        q.append(root)

        while q:
            n = len(q)
            level = []

            for i in range(n):
                node = q.popleft()

                if node:
                    level.append(node.val)

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)
            
            res.append(level)
        
        ressum = float('-inf')
        resind = 0
        
        for i, level in enumerate(res):
            currs = sum(level)

            if currs > ressum:
                ressum = currs
                resind = i+1
        
        return resind
            
            

        

        