#https://leetcode.com/problems/smallest-string-starting-from-leaf/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        def X(root,cur):
            if not root:return 
            cur = chr(ord('a')+root.val)+cur
            if root.left and root.right:
                return min(X(root.left,cur),X(root.right,cur))
            if root.left:
                return X(root.left,cur)
            if root.right:
                return X(root.right,cur)
            return cur
        return X(root,"")
