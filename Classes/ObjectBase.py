# la base de tous mes objets du jeux
# position x, y , update et draw


class ObjectBase :

	def __init__(self, size,position,pygame):
		self.size = size
		self.position = position
		self.pygame = pygame

	def Update(self):
		raise Exception('Surcharge de "Update" obligatoire') 
		
	def Draw(self):
		raise Exception('Surcharge de "Draw" obligatoire') 