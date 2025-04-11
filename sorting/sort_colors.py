# 75. Sort Colors

# Ordenar o array de cores vermelho (0), branco (1) e azul (2) in-place

# dutch national flag algorithm
def sortColors(nums: list[int]):
  low = mid = 0
  high = len(nums) - 1
  
  while mid <= high:
    # red
    if nums[mid] == 0:
      nums[low], nums[mid] = nums[mid], nums[low]
      low += 1
      mid += 1
    # white
    elif nums[mid] == 1:
      mid += 1
    # blue
    else:
      nums[mid], nums[high] = nums[high], nums[mid]
      high -= 1

# bubble sort
def sortColors2(nums: list[int]):
  for _ in range(len(nums)):
    is_sorted = True
    for i in range(len(nums) - 1):
      is_sorted = False
      if nums[i] > nums[i + 1]:
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    if is_sorted:
      break
    
arr = [1, 2, 0, 1, 2, 0, 0, 2, 1]
print("unsorted array :", arr)
sortColors(arr)
print("sorted array   :", arr)