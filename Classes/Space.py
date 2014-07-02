import random 

class Espace :

	def __init__(self, size):
		self.position = dict([('x',0),('y',0)])
		self.time = 0
		self.nombreEtoile = 100
		self.TailleEtoile = min,max = 1,6
		self.size = size
		self.refresh = True
		self.black = 0, 0, 0
		self.white = 255, 255, 255
		self.TabEtoile = []
		
	def Update(self,changeSpace):
		
		# si on change d'ecran on rafraichie
		#if shipPosition >


		i=0;
		if self.refresh :
			self.TabEtoile.clear()
			while i < self.nombreEtoile :
				positionEtoileX = random.randint(0, self.size[0])
				positionEtoileY = random.randint(0 , self.size[1])
				tailleEtoile = random.randint(self.TailleEtoile[0],self.TailleEtoile[1])
				self.TabEtoile.append((positionEtoileX,positionEtoileY,tailleEtoile,tailleEtoile))
				# Ellipse example:
				# When border=0 ellipse is filled
				#                  (screen, (rgb colour) (Xpos,Ypos,width,height),border width)
				i += 1


		self.refresh = changeSpace
		
	def Draw(self,screen, pygame):
		# dessine l'espace selon la position courante
		
		
		screen.fill(self.black)	
		for x in self.TabEtoile:
			pygame.draw.ellipse(screen, self.white, x, 0)
		
		