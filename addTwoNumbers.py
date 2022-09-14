# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        
        p1, p2, p3, carry = l1, l2, ListNode(), 0
        actualNode = p3
        
        while p1 or p2 or carry:
            p1_val = p1.val if p1 else 0
            p2_val = p2.val if p2 else 0
            
            value = p1_val + p2_val + carry
            
            newNode = ListNode(value % 10)
            carry = value // 10
            
            actualNode.next = newNode
            actualNode = newNode
            
            p1 = p1.next if p1 else None
            p2 = p2.next if p2 else None
            
        
        return p3.next
        

# l1 = [2,4,3]
# l2 = [5,6,4]
l1 = ListNode(2,ListNode(4,ListNode(3)))
l2 = ListNode(5,ListNode(6,ListNode(4)))

# l1 = [9,9,9,9,9,9,9]
# l2 = [9,9,9,9]
l1 = ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9,ListNode(9)))))))
l2 = ListNode(9,ListNode(9,ListNode(9,ListNode(9))))

sol = Solution()
sol.addTwoNumbers(l1,l2)        