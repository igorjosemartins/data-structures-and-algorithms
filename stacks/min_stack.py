# 155. Min Stack

# A min stack é uma segunda stack que serve como cache do menor elemento da stack
# Para cada elemento da stack, nós iremos adicionar o seu menor elemento na min stack até que surja um elemento menor
# Desta forma, sempre teremos o menor elemento na última posição da min stack

# Exemplo:
# stack = [1, 4, 9, 5, 2, 3, -2, 0]
# min   = [1, 1, 1, 1, 1, 1, -2, -2]

class MinStack:
  def __init__(self):
    self.stack = []
    self.min_stack = []

  def push(self, val: int) -> None:
    self.stack.append(val)
    
    if self.min_stack:
      val = min(self.min_stack[-1], val)
    
    self.min_stack.append(val)

  def pop(self) -> None:
    self.stack.pop()
    self.min_stack.pop()

  def top(self) -> int:
    return self.stack[-1]

  def getMin(self) -> int:
    return self.min_stack[-1]