# Last updated: 4/8/2025, 5:34:58 PM
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        # Understand - Singly link list

        # Match - Dummy head

        # Plan
        # Create a dummy node
        # Traverse linked list using next ptr
        # For each next value, is it equal to target
        # if target equal, use next ptr to point to next of target
        dummyHead = ListNode(0)
        dummyHead.next = head # actual start 

        prev, curr = dummyHead, head 

        while curr:
            if curr.val == val:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next
        return dummyHead.next
 
        