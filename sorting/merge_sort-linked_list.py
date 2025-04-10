class Node:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next

# 1. Dividir até um nodo
def find_middle(head):
	slow = head
	fast = head.next
	
	while fast and fast.next:
		slow = slow.next
		fast = fast.next.next

	return slow

# Função para ordenação recursiva das sub-listas
# l1 = lado esquerdo da divisão
# l2 = lado direito da divisão
def merge(l1, l2):
	# Inicializamos uma lista com um nodo vazio
	head = Node()
	# Criação de um ponteiro para percorrer a lista
	tail = head
	
	# Enquanto existir elementos na l1 ou l2
	while l1 and l2:
		# Validação de qual número é o menor
		# Atribuição dele na nova lista criada
		if l1.val < l2.val:
			tail.next = l1
			l1 = l1.next
		else:
			tail.next = l2
			l2 = l2.next
		tail = tail.next
	# O loop percorre até alguma das listas acabar, portanto atribuimos 
	# o próximo elemento ao último número da lista que sobrar
	tail.next = l1 or l2
	
	# Retornamos o next por conta do primeiro ser o nodo vazio de inicialização
	return head.next
	
def merge_sort(head):
	if not head or not head.next:
		return head
	
	# Encontramos o meio da lista
	middle = find_middle(head)
	# Guardamos a referência do próximo elemento
	after_middle = middle.next
	# Realizamos a divisão da lista
	middle.next = None
	
	# Recursão do lado esquerdo (head até o middle)
	left = merge_sort(head)
	# Recursão do lado direito (after_middle até o fim da lista)
	right = merge_sort(after_middle)
	
	# Por fim, realizamos o merge das sub-listas até chegar na lista original
	sorted_list = merge(left, right)
	
	return sorted_list

def buildLinkedList(values):
  if not values:
    return None
  
  head = Node(values[0])
  current = head
  
  for val in values[1:]:
    current.next = Node(val)
    current = current.next
  
  return head

def printLinkedList(head):
  if not head:
    return head
  
  result = []
  current = head
  
  while current:
    result.append(current.val)
    current = current.next
    
  print(result)

values = [9, 3, 1, 7]
head = buildLinkedList(values)
sorted_list = merge_sort(head)

print("unsorted list : ", values)
print("sorted list   : ", end=" ")
printLinkedList(sorted_list)