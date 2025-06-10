# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        def helper(root, res):

            if not root.left and not root.right:
                res.append(root.val)
                return 

            if root.left:
                helper(root.left, res)
            
            if root.right:
                helper(root.right, res)
        
        l1 = []
        l2 = []

        helper(root1, l1)
        helper(root2, l2)

        return l1 == l2
        