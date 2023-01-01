# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    total_steps = 0
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.getExtraCoins(root)
        return self.total_steps

    # steps, coins 
    def getExtraCoins(self, node: TreeNode) -> int:
        if node == None:
            return 0
        left_coins = self.getExtraCoins(node.left)
        right_coins = self.getExtraCoins(node.right)
        coins = left_coins + right_coins + node.val - 1
        self.total_steps += abs(coins)
        return coins

sol = Solution()
# print(sol.distributeCoins(TreeNode(3,TreeNode(0),TreeNode(0))))
print(sol.distributeCoins(TreeNode(0,TreeNode(3),TreeNode(0))))
