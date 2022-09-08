# Recursive
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        return self.inorderTraversal(root.left) + [root.val]+self.inorderTraversal(root.right)


# Iterative
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
            arr = []
            res = []

            while True:
                while root:
                    arr.append(root)
                    root = root.left

                if len(arr) == 0:
                    break

                root = arr.pop()
                res.append(root.val)
                root = root.right
            return res
              