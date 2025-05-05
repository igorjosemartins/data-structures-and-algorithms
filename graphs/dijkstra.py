import heapq

# utilizaremos a heapq como fila de processamento por conta da sua propriedade de sempre adicionar o menor elemento no começo da fila
# o que otimiza a execução do algoritmo

def dijkstra(graph, start):
  # fila de processamento no formato (distancia, node)
  # ex: (0, "A")
  min_heap = [(0, start)]
  
  # atribuindo infinito como valor default para cada node
  distances = { node: float('inf') for node in graph }
  
  # por ser o início, a distância sempre será 0
  distances[start] = 0
  
  # loop de processamento
  while min_heap:
    current_distance, current_node = heapq.heappop(min_heap)
    
    # validação para não sobrescrever a distância que já temos registrada ser menor do que a distância atual
    if current_distance > distances[current_node]:
      continue
    
    # loop dos vizinhos do node atual
    for neighbor, weight in graph[current_node].items():
      # calculo da distancia até o início
      distance = current_distance + weight
      
      # se a distância for menor do que já existe no dict de retorno
      if distance < distances[neighbor]:
        # atualizamos a distância
        distances[neighbor] = distance
        
        # adicionamos o vizinho na fila de processamento
        heapq.heappush(min_heap, (distance, neighbor))
  
  return distances
  
graph = {
  "A": { "B": 1, "C": 4 },
  "B": { "A": 1, "C": 2, "D": 5 },
  "C": { "A": 4, "B": 2, "D": 1 },
  "D": { "B": 5, "C": 1 },
}

start_node = "A"

# o resultado virá no formato { node: distância }
# ex: { "A": 0, "B": 1, "C": 3, "D": 4 }

distances = dijkstra(graph, start_node)
print(f"Distances from {start_node}: {distances}")