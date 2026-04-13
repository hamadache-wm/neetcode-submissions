class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root

        lifo_queue = [root]

        while lifo_queue:
            node = lifo_queue.pop()

            node.left, node.right = node.right, node.left

            if node.right:
                lifo_queue.append(node.right)
            if node.left:
                lifo_queue.append(node.left)

        return root