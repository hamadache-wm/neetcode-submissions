# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        fifo_queue = {root: 1}
        to_visit = [root]
        depth = 0

        while to_visit:
            node = to_visit.pop(0)

            node_right, node_left = node.right, node.left

            if node_left:
                to_visit.append(node_left)
                fifo_queue[node_left] = fifo_queue[node] + 1
            if node_right:
                to_visit.append(node_right)
                fifo_queue[node_right] = fifo_queue[node] + 1
            
            depth = fifo_queue[node]

        return depth