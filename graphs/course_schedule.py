# 207. Course Schedule

# numCourses => total de cursos
# prerequisites => pre requisitos para cursar todos os cursos, vem no formato:
  # [[a1, b1], [a2, b2], ...]
  # a => curso a ser feito
  # b => pre-requisito do curso 'a'
  
# verificar se é possível realizar todos os cursos, se sim retornar True, senão, False

def canFinish(numCourses, prerequisites):
  # vamos utilizar o formato:
  # curso: array dos cursos pre-requisitos
  graph = { i: [] for i in range(numCourses) }
  for a, b in prerequisites:
    graph[b].append(a)
  
  # criar um estado para cada curso:  
  # 0 => não visitado | 1 => visitando | 2 => já visitado
  state = [0] * numCourses
  
  # a logica será verificar se os cursos possuem uma dependência cíclica, que faz com que seja impossível de realizar todos os cursos
  def has_cycle(course):
    # caso o curso atual está sendo visitado, é porque existe um ciclo
    if state[course] == 1:
      return True
    # caso o curso atual já foi visitado, é porque já foi percorrido todos os cursos
    if state[course] == 2:
      return False
    
    # atualiza para visitando
    state[course] = 1
    
    # verifica para cada pre-requisito, se existe uma dependência cíclica
    for prereq in graph[course]:
      if has_cycle(prereq):
        return True
    
    # atualiza para já visitado
    state[course] = 2
    return False
  
  # faz a validação para todos os cursos
  for i in range(numCourses):
    if has_cycle(i):
      return False
    
  return True