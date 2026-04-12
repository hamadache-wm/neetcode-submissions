# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        while head.next != None and head.next.next != None:
            prev = head
            r = head.next

            while r.next != None:
                prev = r
                r = r.next
            
            prev.next = None
            nxt = head.next
            head.next = r
            head = head.next
            head.next = nxt
            head = head.next