# 106. Construct Binary Tree from Inorder and Postorder Traversal

class Node:
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None
		
def buildTree(inorder, postorder):
	if not inorder or not postorder:
		return None
	
	# Pega o root com base na propriedade do postorder
	root = Node(postorder.pop())
	# Checa a posição do root no inorder
	root_index = inorder.index(root.val)
	
	# Tudo que está a direita do root no inorder, está a direita na árvore
	root.right = buildTree(inorder[root_index+1:], postorder)
	# Tudo que está a esquerda do root no inorder, está a esquerda na árvore
	root.left =	buildTree(inorder[:root_index], postorder)
	
	return root