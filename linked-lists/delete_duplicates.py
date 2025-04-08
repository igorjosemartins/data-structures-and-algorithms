# 83. Remove Duplicates from Sorted List

# 1 Pointer
def deleteDuplicates(head):
  if not head:
    return head
  
  current = head
  
  while current and current.next:
    if current.val == current.next.val:
      current.next = current.next.next
    else:
      current = current.next
  return head

# 2 Pointer
def deleteDuplicates2(head):
  if not head or not head.next:
    return head
  
  temp_node = head
  current = head.next
      
  while current:
    if current.val == temp_node.val:
        temp_node.next = current.next
    else:
        temp_node = current
    current = current.next
  return head