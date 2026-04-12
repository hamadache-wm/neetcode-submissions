# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        listNode_set = set()

        while head:
            if head in listNode_set:
                return True
            listNode_set.add(head)
            head = head.next

        return False