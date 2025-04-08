# 92. Reverse Linked List II

def reverseBetween(head, left: int, right: int):
  if not head or right == left:
    return head

  current = head
  index = 1
  left_node = None
  pre_left_node = None
  temp_node = None

  while current and index <= right:
    if index + 1 == left:
      pre_left_node = current
      current = current.next
    elif index == left:
      left_node = current
      temp_node = left_node
      current = current.next
    elif left < index < right:
      next_node = current.next
      current.next = temp_node
      temp_node = current
      current = next_node
    elif index == right:
      if head == left_node:
        head = current
      else:
        pre_left_node.next = current
      next_right = current.next
      current.next = temp_node
      left_node.next = next_right
    else:
      current = current.next

    index += 1 

  return head