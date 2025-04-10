# 912. Sort an Array

# Ordene os números do array sem utilizar funções nativas de ordenação
# O algoritmo deve ter complexidade temporal O(n(log n)) e mínima complexidade espacial possível

def sortArray(nums: list[int]) -> list[int]:
  def merge_sort(arr):
    if not arr or len(arr) <= 1:
      return arr
    
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    
    return merge(left, right)
  
  def merge(left, right):
      result = []
      i = j = 0
      
      while i < len(left) and j < len(right):
        if left[i] < right[j]:
          result.append(left[i])
          i += 1
        else:
          result.append(right[j])
          j += 1
      
      result.extend(left[i:])
      result.extend(right[j:])
      
      return result
  
  return merge_sort(nums)