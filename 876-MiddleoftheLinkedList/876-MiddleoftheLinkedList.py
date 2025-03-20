# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialized to the head -> used to traverse the list
        slow_pointer = head
        fast_pointer = head
        
        if not head:
            return None
        # Move slow one step
        # Move fast two step
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
        return slow_pointer

        # Time complexity: O(n) - Go through linked list
        # Space complexity: O(1) 
            