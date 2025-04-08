def bubble_sort(nums):
  size = len(nums)
  
  for _ in range(size):
    print(nums)
    is_sorted = True
    for i in range(size - 1):
      if nums[i] > nums[i + 1]:
        is_sorted = False
        nums[i], nums[i + 1] = nums[i + 1], nums[i]
    if is_sorted:
      return nums
  return nums

bubble_sort([1,2,4,3])