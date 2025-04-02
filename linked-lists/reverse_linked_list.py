# 206. Reverse Linked List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverseList(head):
  # variável que simula um Node vazio para a head apontar
  new_list = None
  
  # enquanto a Head existir, rodamos o loop
  while head:
    # guardamos o próximo Node em uma variável
    next_node = head.next
    # atribuimos o próximo valor da Head à nossa variável vazia
    head.next = new_list
    # andamos o Node criado anteriormente para o primeiro item da lista (Head)
    new_list = head
    # andamos a Head para o próximo Node
    head = next_node
  
  return new_list