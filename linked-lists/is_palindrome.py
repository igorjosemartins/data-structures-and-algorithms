# 234. Palindrome Linked List

# Lógica utilizada:
  # fast irá percorrer a lista de dois em dois
  # slow irá percorrer a lista de um em um
  # quando fast chegar ao final da lista, slow estará no meio
  # até chegar no meio da lista, atribuimos todos os valores em uma pilha
  # ao terminar o loop, inicializamos outro percorrendo o resto dos elementos da lista com base no slow
  # para cada elemento da pilha, o comparamos com o elemento atual de slow
    # se for diferente, é porque não é um palíndromo

def isPalindrome(head):
  fast = head
  slow = head

  stack = []
    
  while fast and fast.next:
    stack.append(slow.val)
    slow = slow.next
    fast = fast.next.next

  # caso a lista seja ímpar, o elemento revertido é ele mesmo, portanto pulamos ele
  if fast:
    slow = slow.next

  while slow:
    top = stack.pop()
    if slow.val != top:
        return False
    slow = slow.next

  return True