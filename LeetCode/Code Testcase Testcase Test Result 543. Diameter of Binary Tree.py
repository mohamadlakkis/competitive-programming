#https://leetcode.com/problems/diameter-of-binary-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = [0]

        def X(root): #return the height
            if not root: return -1
            left = X(root.left)
            right = X(root.right)
            res[0] = max(res[0],2+left+right)
            return 1+max(left,right)
        X(root)
        return res[0]
