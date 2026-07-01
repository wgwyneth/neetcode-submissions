/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

func reverseList(head *ListNode) *ListNode {
    var previousNode *ListNode
	currNode := head
	
	for currNode != nil {
		tempNode := currNode.Next
		currNode.Next = previousNode
		previousNode = currNode
		currNode = tempNode
	}

	return previousNode
}
