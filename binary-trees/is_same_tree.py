# 100. Same Tree

# com recursão
def isSameTree(p, q):
  if p is None and q is None:
    return True
  if p is None or q is None or p.val != q.val:
    return False
  
  left = isSameTree(p.left, q.left)
  right = isSameTree(p.right, q.right)
  
  return left and right

# com preorder traversal
def isSameTree2(p, q):
  if p is None and q is None:
    return True
  if p is None or q is None:
    return False
  
  tree1 = []
  tree2 = []
  
  def preorder_traversal(node, tree):
    if node:
      tree.append(node.val)
      preorder_traversal(node.left)
      preorder_traversal(node.right)
    else:
      tree.append(None)
      
  preorder_traversal(tree1)
  preorder_traversal(tree2)
  
  return tree1 == tree2