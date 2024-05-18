#https://leetcode.com/problems/distribute-coins-in-binary-tree
class Solution:
    def __init__(self):
        self.ans = 0

    def distributeCoins(self, root: TreeNode) -> int:
        self.ans = 0
        self.countSteps(root)
        return self.ans

    def countSteps(self, root: TreeNode) -> int:
        if root is None:
            return 0
        leftCoins = self.countSteps(root.left)
        rightCoins = self.countSteps(root.right)
        self.ans += abs(leftCoins) + abs(rightCoins)
        return (root.val - 1) + leftCoins + rightCoins
