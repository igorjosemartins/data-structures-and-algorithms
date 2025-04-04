# 328. Odd Even Linked List

# Agrupar os nodes com index ímpar seguidos pelos nodes com index par
# Considere o primeiro node como ímpar e o segundo como par, e assim por diante

#          0   1   2   3   4
# input = [10, 20, 30, 40, 50]

#          0   2   4   1   3
# output: [10, 30, 50, 20, 40]

def oddEvenList(head):
  if not head or not head.next:
    return head
  
  # ponteiro ímpar
  odd = head
  
  # ponteiro par (sempre um na frente do ímpar)
  even = head.next
  
  # referência do primeiro par
  even_head = even
  
  # enquanto tiver um par e um na frente dele (ímpar)
  while even and even.next:
    # aponta para o próximo ímpar (na frente do par)
    odd.next = even.next
    # percorre para o próximo ímpar
    odd = odd.next
    
    # aponta para o próximo par (na frente do ímpar)
    even.next = odd.next
    # percorre para o próximo par
    even = even.next
  
  # quando não existir mais pares, atribui ao último ímpar a referência do primeiro par
  odd.next = even_head
  
  return head