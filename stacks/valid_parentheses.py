# 20. Valid Parentheses

# s é uma string que só contém os caractéres:
  # '('
  # ')'
  # '['
  # ']'
  # '{'
  # '}'
  
# retornar se o input é valido
# o input é válido quando:
  # 1. a abertura da bracket é do mesmo tipo da que fecha
  # 2. a abertura da bracket tem que ser fechada na ordem correta
  # 3. cada bracket que fecha tem uma bracket de abertura correspondente

def isValid(s):
  # a stack irá receber todas as brackets de abertura (, [ e {
  stack = []
  # o mapping será um hash map contendo as brackets de fechamento como chave e as de abertura como valor
  mapping = {
    ')': '(',
    ']': '[',
    '}': '{'
  }
  
  # para cada caracter na string
  for ch in s:
    # caso encontrou uma bracket de fechamento
    if ch in mapping:
      # verifica se o último item da stack é a bracket correspondente à bracket atual
      if stack and stack[-1] == mapping[ch]:
        # caso seja, remove ela da stack pois está válida
        stack.pop()
      else:
        # caso não seja, é porque não possui a correspondente ou ela está no lugar errado
        return False
    # adiciona à stack as brackets de abertura
    else:
      stack.append(ch)
  
  # caso a stack esteja vazia é porque todas as brackets foram validadas
  # se sobraram brackets, é porque não foram fechadas corretamente
  return len(stack) == 0