# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Recursive Version
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root == None:
            return TreeNode(val=val)
        
        self.insertIntoBSTHelper(root, val)

        return root

    def insertIntoBSTHelper(self, currNode: TreeNode, val: int) -> TreeNode:
        

        if currNode.val > val:
            if currNode.left != None:
                self.insertIntoBSTHelper(currNode.left, val)
            else:
                currNode.left = TreeNode(val=val)
                return TreeNode
        else:
            if currNode.right != None:
                self.insertIntoBSTHelper(currNode.right, val)
            else:
                currNode.right = TreeNode(val=val)
                return TreeNode