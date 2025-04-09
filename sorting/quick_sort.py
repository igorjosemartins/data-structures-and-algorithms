# Os ponteiros left e right servem para localizar onde começa e termina os sub-arrays
# o que evitar a criação de novos arrays, melhorando a complexidade espacial do algoritmo

# left sempre começará no início 0
# right será sempre o último elemento

def quick_sort(arr):
  def partition(arr, left, right):
    # a escolha do pivô será o elemento mais à direita da lista
    pivot = arr[right]
    
    # o ponteiro i serve como a referência na lista de onde devemos alocar o nosso pivô 
    i = left - 1
    
    # percorre a lista até encontrar um elemento menor ou igual ao pivô
    for j in range(left, right):
      # caso encontre: troca o elemento do ponteiro i com ele
      if arr[j] <= pivot:
        i += 1
        arr[i], arr[j] = arr[j], arr[i]

    # coloca o pivô na posição correta (após o ponteiro i)
    arr[i+1], arr[right] = arr[right], arr[i+1]
    
    # retorna o índice do pivô
    return i+1
    
  def quicksort_recursive(left, right):
    # quando left for igual a right, significa que o array está ordenado
    if left < right:
      # pi = posição do pivô (onde houve a partição do array para sub-arrays)
      pi = partition(arr, left, right)
      
      # faz um novo quick sort com a parte da esquerda
      # left até o pivô - 1
      quicksort_recursive(left, pi-1)
      
      # faz um novo quick sort com a parte da direita
      # pivô + 1 até o right
      quicksort_recursive(pi+1, right)
  
  quicksort_recursive(0, len(arr) - 1)
  
  return arr

# Outra implementação com list comprehensions do Python
# É ineficiente
  # Não é in-place, portanto devemos receber o retorno em uma variável
  # Cria arrays e percorre a lista mais vezes do que o necessário
def quick_sort2(arr):
  if len(arr) <= 1:
    return arr
  else:
    pivot = arr[0]
    less_than_pivot = [x for x in arr[1:] if x <= pivot]
    more_than_pivot = [x for x in arr[1:] if x > pivot]
    return quick_sort2(less_than_pivot) + [pivot] + quick_sort2(more_than_pivot)

###########
## TESTS ##
###########

test_array = [10, 7, 8, 9, 1, 5]
print("Unsorted array :", test_array, "\n")

sorted2_array = quick_sort2(test_array)

print("Quick Sort 1   :", quick_sort(test_array))
print("Quick Sort 2   :", sorted2_array)