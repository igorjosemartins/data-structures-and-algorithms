class MinHeap:
  def __init__(self):
    self.heap = []
    
  def _parent(self, index):
    return (index - 1) // 2
  
  def _left_child(self, index):
    return (index * 2) + 1
  
  def _right_child(self, index):
    return (index * 2) + 2
  
  # função para reordenar a lista caso seja adicionado um elemento filho menor que o pai
  def _heapify_up(self, index):
    if index == 0:
      return
    
    parent_index = self._parent(index)
    
    if self.heap[index] < self.heap[parent_index]:
      self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
      self._heapify_up(parent_index)
  
  # função para reordenar a lista caso o root seja removido
  def _heapify_down(self, parent_index):
    size = len(self.heap)
    
    left = self._left_child(parent_index)
    right = self._right_child(parent_index)
    
    smallest_index = parent_index
    
    if left < size and self.heap[left] < self.heap[smallest_index]:
      smallest_index = left
    
    if right < size and self.heap[right] < self.heap[smallest_index]:
      smallest_index = right
    
    # caso o menor esteja na esquerda ou na direita, realizamos o swap  
    if smallest_index != parent_index:
      self.heap[parent_index], self.heap[smallest_index] = self.heap[smallest_index], self.heap[parent_index]
      self._heapify_down(smallest_index)
      
  def insert(self, value):
    # insert
    self.heap.append(value)
    # reordenação
    self._heapify_up(len(self.heap) - 1)
    
  def pop_min(self):
    if len(self.heap) == 0:
      raise IndexError("Empty heap")
    if len(self.heap) == 1:
      return self.heap.pop()
      
    root = self.heap[0]
    
    # swap
    self.heap[0] = self.heap.pop()
    # reordenação
    self._heapify_down(0)
    
    return root
  
  def peek(self):
    if len(self.heap) == 0:
      raise IndexError("Empty heap")
    return self.heap[0]
  
  def size(self):
    return len(self.heap)
  
  def is_empty(self):
    return len(self.heap) == 0