# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        if not root:
            return None
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        
        else:
            if not(root.left and root.right):
                root = root.left or root.right
            else:
                next_largest = root.right
                while next_largest.left:
                    next_largest = next_largest.left
                root.val = next_largest.val
                root.right = self.deleteNode(root.right, root.val)
        return root