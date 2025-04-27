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
      self.recursive_insert(self.root, val)
  
  def recursive_insert(self, node, val):
    if val < node.val:
      if node.left is None:
        node.left = Node(val)
      else:
        self.recursive_insert(node.left, val)
    else:
      if node.right is None:
        node.right = Node(val)
      else:
        self.recursive_insert(node.right, val)
        
  def search(self, val):
    return self.recursive_search(self.root, val)
  
  def recursive_search(self, node, val):
    if not node:
      return False
    if val == node.val:
      return True
    elif val < node.val:
      return self.recursive_search(node.left, val)
    else:
      return self.recursive_search(node.right, val)
    
tree = BinaryTree()
values = [2, 5, 8, 12, 9, 4, 3]

for val in values:
  tree.insert(val)
  
print(tree.search(5)) # True
print(tree.search(9)) # True
print(tree.search(11)) # False
print(tree.search(1)) # False