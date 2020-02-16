"""
701.
Given a root of a BST, insert a value to the tree 
and still keep the tree as BST.
Note: 
1. New value doesn't exist in the original BST
2. There could be many valid way of insertion, 
   just return any valid answer
"""
import collections

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def insertIntoBST(self, root, val):
        if not root:
            return None
        if val < root.val:
            if not root.left:
                root.left = TreeNode(val)
            else:
                self.insertIntoBST(root.left, val)
        else:
            if not root.right:
                root.right = TreeNode(val)
            else:
                self.insertIntoBST(root.right, val)
        return self.printTree(root)

    def printTree(self, root):
        if not root:
            return None
        queue = collections.deque([])
        queue.append(root)
        lst = []
        while queue:
            curr = queue.popleft()
            lst.append(curr.val)
            if curr.left:
                queue.append(curr.left)
            if curr.right:
                queue.append(curr.right)
        return lst


t = TreeNode(4)
t.left = TreeNode(2)
t.left.left = TreeNode(1)
t.left.right = TreeNode(3)
t.right = TreeNode(7)

s = Solution()
print(s.printTree(t))
print(s.insertIntoBST(t, 5))