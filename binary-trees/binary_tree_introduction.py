from collections import deque

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
    
  def dfs(self, val):
    return self._dfs_recursive(self.root, val)
	
  def _dfs_recursive(self, node, val):
    if node:
      print(node.val)
    if node is None:
      return False
    if node.val == val:
      return True
    if self._dfs_recursive(node.left, val):
      return True
    if self._dfs_recursive(node.right, val):
      return True
    
  def bfs(self, val):
    if self.root is None:
      return False
    
    queue = deque()
    queue.append(self.root)
    
    while queue:
      node = queue.popleft()
      print(node.val)
      
      if node.val == val:
        return True
      
      if node.left:
        queue.append(node.left)
      if node.right:
        queue.append(node.right)
    
    return False
    
  def preorder_traversal(self):
    result = []
    self._recursive_preorder_traversal(self.root, result)
    return result
  
  def _recursive_preorder_traversal(self, node, result):
    if node:
      result.append(node.val)
      self._recursive_preorder_traversal(node.left, result)
      self._recursive_preorder_traversal(node.right, result)

  def inorder_traversal(self):
    result = []
    self._recursive_inorder_traversal(self.root, result)
    return result
  
  def _recursive_inorder_traversal(self, node, result):
    if node:
      self._recursive_inorder_traversal(node.left, result)
      result.append(node.val)
      self._recursive_inorder_traversal(node.right, result)
      
  def postorder_traversal(self):
    result = []
    self._recursive_postorder_traversal(self.root, result)
    return result
  
  def _recursive_postorder_traversal(self, node, result):
    if node:
      self._recursive_postorder_traversal(node.left, result)
      self._recursive_postorder_traversal(node.right, result)
      result.append(node.val)
    
tree = BinaryTree()
values = [5, 3, 1, 10, 15, 7, 20]

for val in values:
  tree.insert(val)
  
# print(tree.search(5))  # True
# print(tree.search(9))  # False
# print(tree.search(11)) # False
# print(tree.search(1))  # True

# print(tree.pre_order_traversal()) # [5, 3, 1, 10, 7, 15]
# print(tree.inorder_traversal())   # [1, 3, 5, 7, 10, 15]
# print(tree.postorder_traversal()) # [1, 3, 7, 15, 10, 5]

# print(tree.dfs(2))

print(tree.bfs(10)) # True
print(tree.bfs(12)) # False