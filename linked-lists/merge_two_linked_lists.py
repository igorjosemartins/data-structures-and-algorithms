# 21. Merge Two Sorted Lists

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def mergeTwoLists(list1, list2):
  # validação das listas
  if not list1:
    return list2
  if not list2:
    return list1
  
  # definição da head
  if list1.val < list2.val:
    head = list1
    list1 = list1.next
  else:
    head = list2
    list2 = list2.next
  
  # criação de uma referência (pointeiro) à head para manipular os elementos seguintes
  head_ref = head
  
  # enquanto tiver elementos em ambas listas
  while list1 and list2:
    # caso o valor da lista 1 seja MENOR
    if list1.val < list2.val:
      # atribui o valor next da head a ele
      head_ref.next = list1.val
      # anda um elemento na lista 1
      list1 = list1.next
    # caso o valor da lista 1 seja MAIOR
    else:
      # atribui o valor next da head ao elemento da lista 2
      head_ref.next = list2.val
      # anda um elemento na lista 2
      list2 = list2.next

    # anda o ponteiro da head para percorrer a lista
    head_ref = head_ref.next
  
  # caso as listas não tenham o mesmo tamanho, nós atribuimos o next ao restante da lista restante
  head_ref.next = list1 if list1 else list2
  
  return head