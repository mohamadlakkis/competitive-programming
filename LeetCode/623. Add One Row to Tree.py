#https://leetcode.com/problems/add-one-row-to-tree/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth==1:
            tree = TreeNode(val,left=root,right=None)
            return tree
        def X(d, cur):
            if cur:
                if d==depth-1:
                    temo = cur.left
                    temo2 = cur.right
                    cur.left = TreeNode(val,left=temo,right=None)
                    cur.right = TreeNode(val,left=None,right=temo2)
                    return

                X(d+1,cur.left)
                X(d+1,cur.right)
        X(1,root)
        return root
