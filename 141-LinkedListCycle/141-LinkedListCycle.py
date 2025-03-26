# Last updated: 3/26/2025, 12:13:57 AM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Slow-fast pointer technique
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            # If it is a cycle then return true
            if slow == fast:
                return True
        return False

        