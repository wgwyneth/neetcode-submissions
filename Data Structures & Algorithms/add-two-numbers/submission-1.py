# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        hasCarryOver = False
        sumList = None
        currHead = None
        while hasCarryOver or l1 != None or l2 != None:
            total = 0
            #Calculate total
            if l1 != None and l2 != None:
                total = l1.val + l2.val     
            elif l1 != None:
                total = l1.val
            elif l2 != None:
                total = l2.val

            #Add carryover if existing, and calculate if total needs carryover
            if hasCarryOver:
                total += 1
                hasCarryOver = False

            if total >= 10:
                total = total % 10
                hasCarryOver = True

            #construct new node with full total
            if sumList == None:
                sumList = ListNode(val=total)
                currHead = sumList
            else:
                currHead.next = ListNode(val=total)
                currHead = currHead.next

            if l1 != None:
                l1 = l1.next
                print("nexting l1")
            if l2 != None:
                l2 = l2.next
                print("nexting l2")
        


        return sumList
