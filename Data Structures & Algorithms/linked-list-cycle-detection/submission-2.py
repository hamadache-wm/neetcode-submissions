# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p = head

        while head and p:
            if head == p.next:
                return True
            head = head.next
            if p.next:
                p = p.next.next

        return False