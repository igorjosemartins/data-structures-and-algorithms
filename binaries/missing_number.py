# 268. Missing Number

# Encontrar o número faltante de um array de sequência 0 a N

# Solução com XOR:
  # a ^ a = 0
  # a ^ 0 = a
  # A ordem das operações XOR não importam
  # Portanto se fizermos XOR com todos os items do array e com todos os items do range de 0 a N, teremos:
    # 0 ^ 1 ^ 3 ^ 0 ^ 1 ^ 2 ^ 3
    # Ou : 0 ^ 0 | ^ 1 ^ 1 | ^ 3 ^ 3 | ^ 2
      # => 0 ^ 0 = 0
      # => 1 ^ 1 = 0
      # => 3 ^ 3 = 0
    # Retornando apenas o número que falta
def missingNumber(nums: list[int]) -> int:
  x = 0
  for num in nums:
      x ^= num
  for i in range(len(nums)+1):
      x ^= i

  return x

print(missingNumber([0, 1, 3])) # 2