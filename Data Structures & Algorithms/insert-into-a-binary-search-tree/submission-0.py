# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        currNode = root
        prevNode = None
        while currNode != None:
            value = currNode.val

            if value > val:
                prevNode = currNode
                currNode = currNode.left
            else:
                prevNode = currNode
                currNode = currNode.right

        if prevNode == None:
            return TreeNode(val=val)
        else:
            if value > val:
                prevNode.left = TreeNode(val=val)
            else:
                prevNode.right = TreeNode(val=val)
        return root

