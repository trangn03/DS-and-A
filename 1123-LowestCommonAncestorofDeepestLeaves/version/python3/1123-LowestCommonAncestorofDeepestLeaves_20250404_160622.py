# Last updated: 4/4/2025, 4:06:22 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        q = deque([(root, None)])
        par = {}
        val = {}
        left = - 1
        right = -1 
        d = 0
        while q:
            n = len(q)
            for i in range(n):
                node, parent = q.popleft()
                x = node.val
                y = parent.val if parent else - 1

                par[x] = y
                val[x] = node

                if i == 0:
                    left = x
                if i == n - 1:
                    right = x
                
                if node.left:
                    q.append((node.left, node))
                if node.right:
                    q.append((node.right, node))
            d += 1
        if left == right:
            return val[left]

        s = left
        t = right

        while s != t:
            s = par[s]
            t = par[t]
        return val[s]

        