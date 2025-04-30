from collections import deque

class Node:
  def __init__(self, val, neighbors):
    self.val = val
    self.neighbors = neighbors if neighbors else []

def clone(node):
  if not node:
    return node

  q = deque([node])
  
  clones = {}
  clones[node.val] = Node(node.val, [])
  
  while q:
    # curr => node original
    curr = q.popleft()
    
    # curr_clone => node clonado
    curr_clone = clones[curr.val]
    
    # percorre os vizinhos do node original
    for n in curr.neighbors:
      # verifica se ele já não foi criado no hashmap
      if n.val not in clones:
        # adiciona no hashmap
        clones[n.val] = Node(n.val, [])
        
        # adiciona os nodes a fila para também serem processados 
        q.append(n)
        
      # adiciona os vizinhos criados ou já criados do node clonado
      curr_clone.neighbors.append(clones[n.val])
  
  # retorna o primeiro node clonado
  return clones[node.val]