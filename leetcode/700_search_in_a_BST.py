# Tree node definition
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root, target):
        """
        :type root: Node
        :type target: int
        :rtype: Node
        """
        if root == None or root.val == target:
            return root
        elif root.val > target:
            return self.searchBST(root.left, target)
        else:
            return self.searchBST(root.right, target)


