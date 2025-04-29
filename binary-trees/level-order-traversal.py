# 102. Binary Tree Level Order Traversal

from collections import deque

def levelOrder(root):
  if root is None:
    return []
  
  result = []
  q = deque()
  q.append(root.val)
  
  while q:
    level = []
    
    for _ in range(len(q)):
      node = q.popleft()
      level.append(node)
      
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)
    
    if level:
      result.append(level)
  
  return result