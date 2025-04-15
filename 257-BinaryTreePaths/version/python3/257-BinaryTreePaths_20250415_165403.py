# Last updated: 4/15/2025, 4:54:03 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        def pre_order(node, path, paths):
            if not node:
                return
            # add node to path
            path.append(str(node.val))
            if not node.left and not node.right:
                # add our path to paths list
                paths.append("->".join(path))
            else:
                pre_order(node.left, path, paths)
                pre_order(node.right, path, paths)
            # we've explored all leaves, remove node from path
            path.pop()
        
        pre_order(root, [], paths)
        return paths
            

        