class Node:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

def sortList(head):
  def merge_sort(head):
    if not head or not head.next:
      return head
    
    def find_middle(head):
      slow = head
      fast = head.next
      
      while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
      
      return slow
    
    def merge(left, right):
      head = Node()
      current = head
      
      while left and right:
        if left.val < right.val:
          current.next = left
          left = left.next
        else:
          current.next = right
          right = right.next
        current = current.next
      
      current.next = left or right
      
      return head.next
    
    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None
    
    left = merge_sort(head)
    right = merge_sort(after_middle)
    
    return merge(left, right)
  
  return merge_sort(head)

def printLinkedList(head):
  result = []
  
  while head:
    result.append(head.val)
    head = head.next
  
  print(result)

node_3 = Node(3)
node_1 = Node(1, node_3)
node_2 = Node(2, node_1)
node_4 = Node(4, node_2)

printLinkedList(node_4)
printLinkedList(sortList(node_4))