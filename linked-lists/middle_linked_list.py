# 876 Middle of the Linked List

def middleNode(head):
  ahead = head
  
  while ahead and ahead.next:
    ahead = ahead.next.next
    head = head.next
    
  return head