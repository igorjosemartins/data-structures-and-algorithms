# 112. Path Sum

def hasPathSum(self, root, targetSum):
  if not root:
    return False
  
  if not root.left and not root.right and targetSum == root.val:
    return True
  
  return self.hasPathSum(root.left, targetSum - root.val) or self.hasPathSum(root.right, targetSum - root.val)