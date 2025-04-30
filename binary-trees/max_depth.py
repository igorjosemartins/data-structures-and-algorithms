from collections import deque

def maxDepth(root):        
  if root is None:
    return 0
    
  depth = 0
  q = deque()
  q.append(root)

  while q:
    depth += 1

    for _ in range(len(q)):
      node = q.popleft()
      if node.left:
        q.append(node.left)
      if node.right:
        q.append(node.right)

  return depth