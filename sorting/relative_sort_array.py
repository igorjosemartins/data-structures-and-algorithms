# 1122. Relative Sort Array

# Ordenar os números de arr1 com base na ordem do arr2
# Os números que tiverem em arr1 que não estão no arr2, devem ser ordenados de forma crescente e adicionados no final de arr1

def relativeSortArray(arr1: list[int], arr2: list[int]) -> list[int]:
  result = []
  extras = []
  
  # catching extras
  for num in arr1:
    if num not in arr2:
      extras.append(num)
      
  for i in arr2:
    for j in arr1:
      if j == i:
        result.append(j)
  
  # bubble sort
  extras_size = len(extras)
  for _ in range(extras_size):
    for idx in range(extras_size - 1):
      if extras[idx] > extras[idx + 1]:
        extras[idx], extras[idx + 1] = extras[idx + 1], extras[idx]

  for num in extras: 
    result.append(num)
  
  return result

unsorted_array = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
sort_order = [2,42,38,0,43,21]

sorted_array = relativeSortArray(unsorted_array, sort_order)
print("unsorted :", unsorted_array)
print("sorted   :", sorted_array)
print("\norder  :", sort_order)