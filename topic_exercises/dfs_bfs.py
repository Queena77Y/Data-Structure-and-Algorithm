from collections import deque

class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def dfs(self, root, target):
        # *** Stack ***
        # LIFO
        if not root:
            return False
        stack = [root]
        visited = set([])
        while stack:
            curr = stack.pop()
            if curr.val == target:
                return True
            else:
                visited.add(curr)
                for child in curr.children:
                    if child not in visited:
                        stack.append(child)
        return False


        # *** Recrusive solution*** 
        # if not root:
        #     return False
        # if root.val == target:
        #     return True
        
        # while root:
        #     for child in root.children:
        #         result = self.dfs(child, target)
        #         if result:
        #            return True
        #     return False

    def bfs(self, root, target):
        # use queue, FIFO
        if not root:
            return False
        queue = deque([root])
        visited = set([])
        while queue:
            curr = queue.popleft()
            if curr.val == target:
                return True
            else:
                visited.add(curr)
                for child in curr.children:
                    if child not in visited:
                        queue.append(child)
        return False
                

        

    
node3 = Node(3, [])
node2 = Node(2, [])
node1 = Node(1, [node2, node3])

test = Solution()
print(test.dfs(node1, 2))