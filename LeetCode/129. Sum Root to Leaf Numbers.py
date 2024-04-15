#https://leetcode.com/problems/sum-root-to-leaf-numbers/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root,num):
            if not root:return 0
            num = num*10 +root.val
            if not root.left and not root.right:
                return num
            return dfs(root.left,num) + dfs(root.right,num)
        return dfs(root,0)
