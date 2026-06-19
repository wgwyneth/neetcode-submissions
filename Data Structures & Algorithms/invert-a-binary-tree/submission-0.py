# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None
        
        leftNode = root.left
        rightNode = root.right

        self.invertTree(leftNode)
        root.right = leftNode

        self.invertTree(rightNode)
        root.left = rightNode

        return root