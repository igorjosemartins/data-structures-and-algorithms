# 191. Number of 1 Bits

# Dado um número N, retorne o número de "1"s da sua representação binária
# 3 => 011 => 2 "1"s
# 128 => 10000000 => 1 "1"s

def hammingWeight(n: int)-> int:
  count = 0
  while n > 0:
    # caso o resultado dessa operação seja 1, portanto o último bit deste número também é 1
    if n & 1:
      n -= 1
      count += 1
    else:
      n >>= 1
  return count

print(hammingWeight(11)) # 3
print(hammingWeight(128)) # 1
print(hammingWeight(2147483645)) # 30