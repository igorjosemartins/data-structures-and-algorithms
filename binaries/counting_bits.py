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

# O(n)
def countBits2(n: int) -> list[int]:
  # inicializa um array de 0's com o tamanho correto
  arr = [0] * (n + 1)
  for i in range(1, n + 1):
    # utiliza (i >> 1) para reusar um resultado anterior e soma com o bit de paridade (i & 1)
    arr[i] = arr[i >> 1] + (i & 1)
  return arr

print(countBits(5)) # [0, 1, 1, 2, 1, 2]
print(countBits2(5)) # [0, 1, 1, 2, 1, 2]