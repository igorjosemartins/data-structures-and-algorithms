def binary_search(arr, element):
  lower = 0
  higher = len(arr)
  
  # para provar a complexidade temporal O(log N)
  # conforme o tamanho do input cresce exponencialmente, o tempo cresce linearmente
  steps = 0
  
  while lower < higher:
    steps += 1
    mid = int((lower + higher) / 2)
    
    if (element == arr[mid]):
      print("steps : ", steps)
      return mid
    elif (element > arr[mid]):
      lower = mid + 1
    else:
      higher = mid
  return -1

n = 3

binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], n)
# input = 10
# steps = x

binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], n)
# input = 20
# steps = x + 1

binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40], n)
# input = 30
# steps = x + 2