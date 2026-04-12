# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head

        while p and p.next:
            head = head.next
            p = p.next.next
            if head == p:
                return True

        return False