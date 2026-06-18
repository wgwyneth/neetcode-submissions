# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        list1Curr = list1
        list2Curr = list2
        currentNodeMember = None
        returns = None
        previousNode = None
        while list1Curr != None and list2Curr != None:
            if list1Curr.val > list2Curr.val:
                currentNodeMember = list2Curr
                list2Curr = list2Curr.next
            else:
                currentNodeMember = list1Curr
                list1Curr = list1Curr.next
            
            if returns == None:
                returns = currentNodeMember
                previousNode =  returns 
            else:
                previousNode.next = currentNodeMember
                previousNode = currentNodeMember
        
        if list1Curr != None:
            if previousNode == None:
                returns = list1Curr
            else:
                previousNode.next = list1Curr
        
        if list2Curr != None:
            if previousNode == None:
                returns = list2Curr
            else:
                previousNode.next = list2Curr

        return returns

            
