# 743. Network Delay Time

# times => lista que contem os nodes no formato: 
#   - [0] => current_node
#   - [1] => target_node
#   - [2] => delay_time
# n => número de nodes a serem percorridos
# k => start node

# retornar o menor tempo possível para que todos os nodes recebam o sinal
# caso seja impossivel todos os nodes receberem o sinal, retornar -1

import heapq

def networkDelayTime(times, n, k):
  table = {}
  
  # formatação de times para { current_node: { target_node: delay_time } }
  for t in times:
    if not table.get(t[0]):
      table[t[0]] = { t[1]: t[2] }
    else:
      table[t[0]][t[1]] = t[2]

  # lista de processamento
  min_heap = [(0, k)]
  # objeto de retorno
  distances = { k: 0 }
  
  while min_heap:
    curr_distance, curr_node = heapq.heappop(min_heap)
    
    # é preciso fazer esta validação porque nós só adicionamos os nodes de origem no dicionario
    row = table.get(curr_node)
    
    if row:
      for neighbor, weight in row.items():
        # distancia já registrada, caso não exista utiliza infinito como default
        old_distance = distances.get(neighbor, float('inf'))
        new_distance = curr_distance + weight
        
        if new_distance < old_distance:
          distances[neighbor] = new_distance
          heapq.heappush(min_heap, (new_distance, neighbor))
  
  # caso não tenha percorrido todos os nodes
  if len(distances) < n:
    return -1
  
  _max = 0
  
  # pega a menor distancia no objeto de retorno
  for distance in distances.values():
    _max = max(_max, distance)
  
  # caso seja 0 precisamos retornar -1 por conta do leetcode
  if _max == 0:
    return -1
  
  return _max

print(networkDelayTime([[2,1,1],[2,3,1],[3,4,1]], 4, 2)) # 2
print(networkDelayTime([[1,2,1]], 2, 1)) # 1
print(networkDelayTime([[1,2,1]], 2, 2)) # -1