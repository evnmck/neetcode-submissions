# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        one = deque()
        two = deque()

        one.append(p)
        two.append(q)

        while one:
            curr_one, curr_two = one.popleft(), two.popleft()

            if not curr_one and not curr_two:
                continue
            if not curr_one or not curr_two:
                return False
            if curr_one.val != curr_two.val:
                return False
            
            one.append(curr_one.left)
            one.append(curr_one.right)
            two.append(curr_two.left)
            two.append(curr_two.right)

        return True