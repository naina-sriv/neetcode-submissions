class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        res = []
        curr = root
        lastVisited = None

        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left

            peek = stack[-1]

            if peek.right and lastVisited != peek.right:
                curr = peek.right
            else:
                res.append(peek.val)
                lastVisited = stack.pop()

        return res