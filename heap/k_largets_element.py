# 703. Kth Largest Element in a Stream

from collections import heapq
from typing import List

# nums = lista de notas
# k = número de alunos

# precisamos encontrar a nota de corte baseada nesta lista de notas e o número de alunos

# exemplo:
# nums = [2, 9, 3, 6, 8]
# k = 3
# output = 6*

# * já que o número de alunos é 3, devemos pegar a menor nota dentre as 3 maiores notas (6, 8, 9), logo a resposta é 6

# iremos utilizar min_heap para resolver o problema, já que ele por si só faz a ordenação e possui a lógica de push/pop com base no menor elemento
# se juntarmos com o limite do número de alunos k, nós teriamos sempre a menor nota na posição 0 da lista

class KthLargest:
  def __init__(self, k: int, nums: List[int]):
    self.nums = nums
    self.k = k

    heapq.heapify(self.nums)
    while len(self.nums) > k:
      heapq.heappop(self.nums)

  def add(self, val: int) -> int:
    heapq.heappush(self.nums, val)
    
    if len(self.nums) > self.k:
      heapq.heappop(self.nums)
    
    return self.nums[0]
    
    
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)