# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.maxx = 0 

        def dfs(node, is_left, curr):
            if not node:
                return 
            
            self.maxx = max(self.maxx, curr)

            if is_left:
                dfs(node.right, False, curr+1)
                dfs(node.left, True, 1)
            
            else:
                dfs(node.left, True, curr+1)
                dfs(node.right, False, 1)
        
        dfs(root.left, True, 1)
        dfs(root.right, False, 1)

        return self.maxx

        