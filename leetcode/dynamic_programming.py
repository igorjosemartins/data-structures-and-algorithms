def climbStairs(n: int) -> int:
  # tamanho do array será n + 1 já que n é o número de elementos e não o tamanho do array
  size = (n + 1)
  # criamos placeholders para cada degrau
  dp = [0] * size

  # nesta implementação, vamos imaginar que exista o caso de 0 degraus
  # apenas para que possa ser calculado o segundo degrau e que "n" seja de fato a última posição do array
  dp[0] = 1
  dp[1] = 1
  
  for i in range(2, size):
    dp[i] = dp[i - 1] + dp[i - 2]
  
  return dp[n]