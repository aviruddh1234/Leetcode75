class Solution:
    count = 0
    targetSum = 0
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        self.targetSum = targetSum
        self.countPath(root,targetSum,True)
        return self.count
    
    def countPath(self,root,curr_sum,isRoot: bool):
        if not root: return 
        curr_sum -= root.val
        if curr_sum == 0:
            self.count += 1
        self.countPath(root.right,curr_sum,False)
        self.countPath(root.left,curr_sum,False)
        
        if isRoot:
            self.countPath(root.right,self.targetSum,True)
            self.countPath(root.left,self.targetSum,True)
            