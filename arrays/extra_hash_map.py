# 1. Two Sum

# Retornar os índices dos dois números que somados dão o valor de target

# Hash Map
# time: O(N)
# space: O(N)
def twoSum(nums: list[int], target: int) -> list[int]:
  d = {}
  
  for i in range (len(nums)):
    pair = target - nums[i]
    if pair in d:
      return [d[pair], i]
    else:
      d[nums[i]] = i
  return []

# Brute Force
# time: O(N²)
# space: O(1)
def twoSum2(nums: list[int], target: int) -> list[int]:
  for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
      if i + j == target:
        return [i, j]
  return []

print(twoSum([2,7,1,3], 9)) # [0, 1]
print(twoSum([3,2,3,6], 6)) # [0, 2]
print(twoSum([3,2,4,9], 6)) # [1, 2]