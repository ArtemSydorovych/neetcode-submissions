# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
    
        q = deque([root])
        res = []
        q.append(root)

        while q:
            right = None
            

            for i in range(len(q)):
                cur = q.popleft()
                if cur:
                    right = cur
                    q.append(cur.left)
                    q.append(cur.right)
            if right:
                res.append(right.val)
        return res