# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.ans=[]
        def traversal(root):
            if not root:
                return
            else:
                traversal(root.left)
                self.ans.append(root.val)
                traversal(root.right)
                return root
        traversal(root)
        return self.ans


        