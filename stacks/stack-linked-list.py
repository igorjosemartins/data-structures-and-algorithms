class Node:
  def __init__(self, val):
    self.val = val
    self.next = None
    
class Stack:
  def __init__(self):
    self.top = None
    self._size = 0
    
  def push(self, item):
    new_node = Node(item)
    new_node.next = self.top
    self.top = new_node
    self._size += 1
    
  def pop(self):
    if self.top is None:
      return IndexError("Empty stack")
    
    popped_node = self.top
    self.top = popped_node.next
    self._size -= 1
    
    return popped_node.val
  
  def peek(self):
    if self.top is None:
      return IndexError("Empty stack")
    
    return self.top.val
  
  def size(self):
    return self._size

stack = Stack()

print(stack.size()) # 0

stack.push(1)
stack.push(2)
stack.push(3)

print(stack.size()) # 3

print(stack.pop()) # 3
print(stack.pop()) # 2
print(stack.pop()) # 1
print(stack.pop()) # Empty stack