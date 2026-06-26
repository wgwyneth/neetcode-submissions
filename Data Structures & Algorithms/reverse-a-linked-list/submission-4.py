# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node = head
        previous = None

        while curr_node != None:
            temp = curr_node.next
            curr_node.next = previous
            previous = curr_node
            curr_node = temp

    
        return previous