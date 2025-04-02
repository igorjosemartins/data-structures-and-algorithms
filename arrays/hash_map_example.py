# 387. First Unique Character in a String

# Dada uma string, precisamos encontrar o primeiro caractere que não repete e retornar o seu index.
# Caso não exista, retornar -1

def firstUniqChar(s: str) -> int:
		# A ideia é criar um hash map contendo a primeira posição que o caractere aparece
		# junto com a quantidade de vezes que ele aparece
		# 'i': [0, 3] 
		# logo, 'i' aparece pela primeira vez no index 0, e repete 3 vezes
		d = {}
		
		# enumerate() cria pares de index e valor para cada elemento de uma string/array
		# enumerate('igor'):
		# [
		#  (0, 'i'),
		#  (1, 'g'),
		#  (2, 'o'),
		#  (3, 'r')
		# ]
		for index, char in enumerate(s):
			if d.get(char):
				d[char][1] += 1
			else:
				d[char] = [index, 1]
				
		# items() retorna as chaves e valores do dictionary (hash map)
		for _, value in d.items():
			# value[1] => quantidade de vezes que o caractere apareceu
			if value[1] == 1:
				return value[0]
				
		return -1

print(firstUniqChar('teste')) # 2 | 's'