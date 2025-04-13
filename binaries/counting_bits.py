# 338. Counting Bits

# Dado um número N, retorne um array de tamanho N + 1 onde cada posição i é o número de 1's da representação binária de i

# O(n log n)
def countBits(n: int) -> list[int]:
  arr = []
  for i in range(n + 1):
    count = 0
    while i > 0:
      count += i & 1
      i >>= 1
    arr.append(count)
  return arr

print(countBits(5)) # [0, 1, 1, 2, 1, 2]