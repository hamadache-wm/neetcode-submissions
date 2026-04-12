class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = None

        while head != None:
            res = ListNode(head.val, res)
            head = head.next

        return res