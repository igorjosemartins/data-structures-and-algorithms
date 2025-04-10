def merge_sort(arr: list[int]) -> list[int]:
  if len(arr) <= 1:
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

arr = [4, 3, 9, 2, 1, 6, 7, 5]
print("unsorted :", arr)
print("sorted   :", merge_sort(arr))