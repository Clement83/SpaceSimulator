

class PowerSwitch() :

	def __init__(self,numero, endOfGraphe = False,isStartOfGraph = False, etat = False):
		self.Etat = etat
		self.Numero = numero
		self.Adjacent = []
		self.isEndOfGraph = endOfGraphe
		self.isStartOfGraph = isStartOfGraph
		
	def IsEndOfGraphe(self):
		return self.isEndOfGraph
	
	def IsStartOfGraphe(self):
		return self.isStartOfGraph
		
	def IsOpen(self):
		return  self.Etat