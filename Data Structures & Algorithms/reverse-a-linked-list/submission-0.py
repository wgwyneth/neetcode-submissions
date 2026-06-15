# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None:
            return None
        currNode = head
        lastNode = None
        while(currNode.next != None):
            currNext = currNode.next
            currNode.next = lastNode
            
            lastNode = currNode
            currNode = currNext
        
        currNode.next = lastNode
        return currNode