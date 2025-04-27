class Node:
  def __init__(self, val: int):
    self.val = val
    self.left = None
    self.right = None

class BinaryTree:
  def __init__(self):
    self.root = None
  
  def insert(self, val):
    if self.root is None:
      self.root = Node(val)
    else:
      self._recursive_insert(self.root, val)
  
  def _recursive_insert(self, node, val):
    if val < node.val:
      if node.left is None:
        node.left = Node(val)
      else:
        self._recursive_insert(node.left, val)
    else:
      if node.right is None:
        node.right = Node(val)
      else:
        self._recursive_insert(node.right, val)
        
  def search(self, val):
    return self._recursive_search(self.root, val)
  
  def _recursive_search(self, node, val):
    if not node:
      return False
    if val == node.val:
      return True
    elif val < node.val:
      return self._recursive_search(node.left, val)
    else:
      return self._recursive_search(node.right, val)
    
  def pre_order_traversal(self):
    result = []
    self._recursive_pre_order_traversal(self.root, result)
    return result
  
  def _recursive_pre_order_traversal(self, node, result):
    if node:
      result.append(node.val)
      self._recursive_pre_order_traversal(node.left, result)
      self._recursive_pre_order_traversal(node.right, result)

  def inorder_traversal(self):
    result = []
    self._recursive_inorder_traversal(self.root, result)
    return result
  
  def _recursive_inorder_traversal(self, node, result):
    if node:
      self._recursive_inorder_traversal(node.left, result)
      result.append(node.val)
      self._recursive_inorder_traversal(node.right, result)
    
tree = BinaryTree()
values = [5, 3, 1, 10, 15, 7]

for val in values:
  tree.insert(val)
  
# print(tree.search(5))  # True
# print(tree.search(9))  # False
# print(tree.search(11)) # False
# print(tree.search(1))  # True

print(tree.pre_order_traversal()) # [5, 3, 1, 10, 7, 15]
print(tree.inorder_traversal())   # [1, 3, 5, 7, 10, 15]