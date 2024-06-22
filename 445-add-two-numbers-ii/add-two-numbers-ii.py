# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        while curr is not None:
            nextN = curr.next
            curr.next = prev
            prev = curr
            curr = nextN
        return prev

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the input lists
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        carry = 0
        dummy_head = ListNode(0)
        current = dummy_head

        # Add the two numbers
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Create a new node with the sum of values
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in the input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # The result is in reverse order, reverse it back
        return self.reverseList(dummy_head.next)

        # Add the two numbers
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the carry
            total = val1 + val2 + carry
            carry = total // 10
            new_val = total % 10
            
            # Create a new node with the sum of values
            current.next = ListNode(new_val)
            current = current.next
            
            # Move to the next nodes in the input lists
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # The result is in reverse order, reverse it back
        return self.reverseList(dummy_head.next)









   

        