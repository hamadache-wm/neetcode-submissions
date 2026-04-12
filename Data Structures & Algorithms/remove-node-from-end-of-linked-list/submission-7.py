# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = prev = head

        while r.next:
            r = r.next

            if n > 0:
                n -= 1
            else:
                prev = prev.next

        if n > 0:
            return head.next
        else:
            prev.next = prev.next.next

        return head