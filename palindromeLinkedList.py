# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        string = ""
        
        while head:
            string += str(head.val)
            head = head.next
        
        return string == string[::-1]
    
head = ListNode(1,ListNode(2,ListNode(2,ListNode(1))))
print(Solution.isPalindrome(Solution,head))
            
head = ListNode(1,ListNode(2))
print(Solution.isPalindrome(Solution,head))

head = ListNode(1,ListNode(2,ListNode(3,ListNode(2,ListNode(1)))))
print(Solution.isPalindrome(Solution,head))