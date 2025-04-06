def getIntersectionNode(headA, headB):
  listA = headA
  listB = headB
  count = {}
  
  while listA:
    count[listA] = 1
    listA = listA.next
  
  while listB:
    if count.get(listB):
      return listB
    listB = listB.next
  
  return None