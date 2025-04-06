# 203. Remove Linked List Elements

def removeElements1(head, val):
  if not head:
    return head

  while head and head.val == val:
    head = head.next

  current = head

  while current and current.next:
    next_node = current.next
    if next_node.val == val:
      current.next = next_node.next

    while current.next and current.next.val == val:
      current.next = current.next.next

    current = current.next

  return head

def removeElements2(head, val):
  if not head:
    return head

  current = head

  while current and current.next:
    next_node = current.next
    if next_node.val == val:
      current.next = next_node.next
    else:
      current = current.next
  
  if head.val == val:
    head = head.next
  
  return head