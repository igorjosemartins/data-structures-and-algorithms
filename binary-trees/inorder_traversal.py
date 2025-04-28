# 94. Binary Tree Inorder Traversal

def inorderTraversal(root):
  result = []
    
  def inorder(node, result):
    if node:
      inorder(node.left, result)
      result.append(node.val)
      inorder(node.right, result)
  
  inorder(root, result)

  return result

def inorderTraversal2(root):
  def inorder(node):
    return inorder(node.left) + [node.val] + inorder(node.right) if node else []
  return inorder(root)