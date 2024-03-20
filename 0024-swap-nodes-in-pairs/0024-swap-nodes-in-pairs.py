# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        # This pointer will be used to traverse the list
        current = dummy
        
        while current.next and current.next.next:
            # Nodes to be swapped
            first = current.next
            second = current.next.next
            
            # Swapping
            current.next = second
            first.next = second.next
            second.next = first
            
            # Move the pointer two nodes ahead
            current = current.next.next
        
        return dummy.next
        