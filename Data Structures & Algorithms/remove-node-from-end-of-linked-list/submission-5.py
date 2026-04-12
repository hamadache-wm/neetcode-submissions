# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = prev = head
        counter = n

        # if r.next == None:
        #     return None

        while r.next:
            r = r.next

            if counter > 0:
                counter -= 1
            else:
                prev = prev.next

        # print(prev.val)
        # prev.next = prev.next.next
        if counter > 0:
            return head.next
        else:
            prev.next = prev.next.next

        return head