def binary_search(arr, target, lower, higher):  
  while lower < higher:
    mid = int((lower + higher) / 2)
    
    if (target == arr[mid]):
      return mid
    elif (target > arr[mid]):
      lower = mid + 1
    else:
      higher = mid
  return -1

def exponential_search(arr, target):
  if (arr[0] == target):
    return 0

  # não precisamos necessariamente utilizar o ponteiro esquerdo
    # devido à busca exponencial, o ponteiro esquerdo sempre será a metade do ponteiro direito
    # l = r // 2
  l = 0
  r = 1
  arr_len = len(arr)

  while (r < arr_len and arr[r] < target):
    # o ponteiro esquerdo recebe o valor anterior do ponteiro direito
    l = r
    # aumento exponencial no ponteiro direito
    r *= 2

  if (arr[r] == target):
    return r
  
  # utilizamos a função min() porque o ponteiro direito pode ter pulado o tamanho máximo do array
  return binary_search(arr, target, l, min(r, arr_len - 1))

arr1 = [
  1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
  11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
  21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 
  31, 32, 33, 34, 35, 36, 37, 38, 39, 40
]

arr2 = [3, 7, 15, 20, 32, 45, 60, 80, 100];

target = 32

print(exponential_search(arr1, target)) # 31
print(exponential_search(arr2, target)) # 4