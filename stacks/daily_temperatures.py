# 739. Daily Temperatures

def dailyTemperatures(temperatures):
  answer = [0] * len(temperatures)
  
  # stack irá guardar os índices dos dias ainda não resolvidos
  stack = []
  
  for i, temp in enumerate(temperatures):
    # caso o dia do index guardado na stack for menor que o dia atual
    while stack and temperatures[stack[-1]] < temp:
      # resolve ele atribuindo a distância entre ele e o dia atual
      index = stack.pop()
      answer[index] = i - index
    
    # armazena o dia atual
    stack.append(i)
    
  return answer