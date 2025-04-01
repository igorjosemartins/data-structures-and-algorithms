# 3090. Maximum Length Substring With Two Occurrences

def sliding_window(s: str) -> int:
  l, r = 0, 0
  _max = 1
  counter = {}

  # atribuindo o valor do primeiro caracter antes do loop, já que sempre haverá pelo menos 1 caractere
  counter[s[0]] = 1

  # enquanto o ponteiro da direita for menor do que o tamanho da string
  # - 1 para evitar erro de 'out of bounds'
  while (r < (len(s) - 1)):
    # avançamos o ponteiro da direita (expansão)
    r += 1

    # checagem se existe a contagem do caracter atual
    if (counter.get(s[r])):
      counter[s[r]] += 1
    else:
      counter[s[r]] = 1

    # caso a contagem de algum elemento chegue em 3 temos que contrair a janela
    while (counter[s[r]] == 3):
      # diminuimos em 1 o caracter atual
      counter[s[l]] -= 1
      # avançamos o ponteiro da esquerda (contração)
      l += 1
    
    # atualizamos o número máximo utilizando a função max() para não sobreescrever o último valor
    # (r - l) para pegarmos o tamanho da string
    # +1 por conta do index 0
    _max = max(_max, (r - l) + 1)
  
  return _max

print(sliding_window('bcbbbb')) # 3