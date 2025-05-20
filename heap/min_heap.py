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
    
    # caso o node filho seja menor que o pai
    if self.heap[index] < self.heap[parent_index]:
      # realiza o swap
      self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
      # segue a mesma lógica recursivamente
      self._heapify_up(parent_index)
  
  # função para reordenar a lista caso o root seja removido
  def _heapify_down(self, parent_index):
    # pega o tamanho de heap para evitar erro de out of bounds
    size = len(self.heap)
    
    # pega o node esquerdo e direito
    left = self._left_child(parent_index)
    right = self._right_child(parent_index)
    
    # inicializa com o pai
    smallest_index = parent_index
    
    # valida se o node a esquerda é menor que o pai
    if left < size and self.heap[left] < self.heap[smallest_index]:
      smallest_index = left
    
    # valida se o node a direita é menor que o pai
    if right < size and self.heap[right] < self.heap[smallest_index]:
      smallest_index = right
    
    # caso o pai seja o menor, o heap já está correto
    # caso o menor esteja na esquerda ou na direita
    if smallest_index != parent_index:
      # realizamos o swap e segue a mesma lógica recursivamente
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