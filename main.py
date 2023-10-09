# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def sortedArrayToBST(nums: list[int]) -> TreeNode:
    def helper_point(left, right):
        if left > right:
            return None
        else:
            middle = (left + right) // 2
            root = TreeNode(nums[middle])
            root.left = helper_point(left, middle-1)
            root.right = helper_point(middle+1, right)
            return root

    helper_point(0, len(nums)-1)
