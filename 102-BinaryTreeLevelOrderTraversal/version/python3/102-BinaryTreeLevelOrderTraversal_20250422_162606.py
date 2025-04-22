# Last updated: 4/22/2025, 4:26:06 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # If the tree is empty -> return empty list
        if not root: 
            return []
        # Create an empty queue
        result = []
        # Create an empty list to store visited nodes
        # Add the root to the queue
        queue = deque([root])
        # While queue is not empty
        while queue:
            # Pop the next node off the queue
            # Add the popped node to the list of visited nodes
            level_size = len(queue)
            level_nodes = []
            for i in range (level_size):
                node = queue.popleft()
                level_nodes.append(node.val)
                # Add the popped node's left child to the queue
                if node.left:
                    queue.append(node.left)
                # Add the popped node's right child to the queue
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
        return result


        