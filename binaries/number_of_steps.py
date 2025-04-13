# 1342. Number of Steps to Reduce a Number to Zero

# Calcular em quantos passos demoramos para reduzir um número a 0
# Caso seja ímpar, devemos diminuir em 1
# Caso seja par, devemos dividir por 2

# Solução utilizando Right Shift (>>) e AND (&)
  # Ao utilizarmos a operação '& 1', conseguimos determinar se o número é ímpar ou par pelo bit de paridade
    # 1 = ímpar
    # 0 = par
  # Ao utilizarmos a operação '>> 1' em números pares, sempre será retornado a metade

def numberOfSteps(num: int) -> int:
  steps = 0
  while num > 0:
    if num & 1:
      num -= 1
    else:
      num >>= 1
    steps += 1
  return steps

print(numberOfSteps(7)) # 5
print(numberOfSteps(14)) # 6
print(numberOfSteps(123)) # 12