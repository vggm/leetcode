# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        p1, p2, p3 = list1, list2, ListNode()
        curr = p3
        
        while p1 or p2:

            if p1 and p2:
                if p1.val < p2.val:
                    minor = p1.val
                    p1 = p1.next if p1.next else None
                else:
                    minor = p2.val
                    p2 = p2.next if p2.next else None
            elif p1:
                minor = p1.val
                p1 = p1.next if p1.next else None
            else:
                minor = p2.val
                p2 = p2.next if p2.next else None
                
            newNode = ListNode(minor)
            curr.next = newNode
            curr = newNode
        
        return p3.next


sol = Solution()
list1 = ListNode(1,ListNode(2,ListNode(4)))
list2 = ListNode(1,ListNode(3,ListNode(4)))
sol.mergeTwoLists(list1,list2)