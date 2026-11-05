# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        arr = []
        def solve(temp):
            if temp is None:
                return 
            solve(temp.left)
            arr.append(temp.val)
            solve(temp.right)
        solve(root)
        return arr