from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        dummyHead = ListNode()
        curr = dummyHead
        
        last = None
        while head:
            
            if head.val != last:
                newNode = ListNode(head.val)
                curr.next = newNode
                curr = newNode
                last = head.val
            
            head = head.next
        
        return dummyHead.next 
                    
                    
                
"""
1 -> 1 -> 2 -> 3 -> 3
"""
head = ListNode(1,ListNode(1,ListNode(2,ListNode(3,ListNode(3)))))                 
Solution().deleteDuplicates(head)