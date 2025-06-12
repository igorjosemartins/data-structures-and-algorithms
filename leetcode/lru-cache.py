class Node:
  def __init__(self, key, value):
    self.key, self.value = key, value
    self.prev, self.next = None, None
    
class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.cache = {}
    # dummy da head e da tail
    # serve para não precisarmos implementar uma linked list
    self.left, self.right = Node(0,0), Node(0,0)
  
  # removemos o último node (previous do right)
  def remove(self, node):
    prev, _next = node.prev, node.next
    
    # apontando o node anterior para o próximo node do node atual
    prev.next = _next
    # apontando o próximo node para o node anterior do node atual
    _next.prev = prev
  
  # adicionar na head (next do left)
  def insert(self, node):
    prev, _next = self.left, self.left.next
    
    # apontando o próximo de left para o node atual
    prev.next = node
    # apontando o anterior da antiga head para o node atual
    _next.prev = node
    
    # apontando o anterior do node atual para o left
    node.prev = prev
    # apontando o próximo do node atual para a antiga head
    node.next = _next
  
  # o get precisa retornar o elemento na posição de key E adicioná-lo na head
  def get(self, key):
    if self.cache.get(key):
      # precisamos remover da onde ele está
      self.remove(self.cache[key])
      # e adicioná-lo na head
      self.insert(self.cache[key])
      return self.cache[key].val
    
    return -1
  
  # o put precisa colocar o node no hashmap e na linked list
  def put(self, key, value):
    # caso ele já exista, precisamos remover da posição atual
    if self.cache.get(key):
      self.remove(self.cache[key])
    
    # criamos o node no hashmap
    self.cache[key] = Node(key, value)
    # inserimos na lista
    self.insert(self.cache[key])
    
    # caso a lista exceda o limite
    if len(self.cache) > self.capacity:
      # pegamos o lru
      lru = self.right.prev
      # removemos ele da lista e do hashmap
      self.remove(lru)
      del self.cache[lru.key]