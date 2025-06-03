from collections import heapq
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
  def __init__(self, val=0, next=None):
    self.val = val
    self.next = next

# o problema nos fornece "k" linked lists
# precisamos retornar uma linked list com todos os nodes das outras ordenados
def mergeKLists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
  heap = []

  # caso enviarmos uma tupla para um heap, ele irá ordenar com base no primeiro elemento da tupla
  # portanto, encaminhamos:
  # - o valor do node para ordenação da lista
  # - função id apenas para possíveis desempates de ordem caso existam dois nodes com o mesmo valor
  # - o node para conseguirmos percorrer cada linked list
  def push_node(heap, node):
    if node:
      heapq.heappush(heap, (node.val, id(node), node))

  # adicionamos todas as heads no nosso heap
  for head in lists:
    push_node(heap, head)

  # criamos a linked list de retorno
  # dummy = head
  # current = ponteiro para inserção de nodes
  dummy = ListNode()
  current = dummy

  # loop para processar cada node
  while heap:
    # o que importa é apenas o node, os valores servem apenas para ordená-los de forma crescente
    _, _, node = heapq.heappop(heap)

    # adiciona o node na lista de retorno e percorre ele para a próxima iteração
    current.next = node
    current = current.next

    # caso exista um próximo node na lista atual, adiciona na fila de processamento
    if node.next:
      push_node(heap, node.next)
  
  # retorna o next já que a head aponta para um node vazio
  return dummy.next