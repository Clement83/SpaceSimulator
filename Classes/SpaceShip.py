from Classes.ObjectBase import ObjectBase
import Classes.InputHelper

class SpaceShip(ObjectBase) :

	def __init__(self, size,pygame):
		#taille de la zone de dessin
		#self.size = size
		ObjectBase.__init__(self, size,(size[0]/2,size[1]/2),pygame )
		self.image = self.pygame.image.load("Ressources/Images/SpaceShip.png").convert()
		self.vitesse = 0
		self.acceleration =0
		self.vitesseMax = 10
		self.accelerationMax=2
		self.__ChangeSpace = False;

	def Update(self, theInput):

		if theInput.Haut():
			self.position =(self.position[0],self.position[1]-1)


		if theInput.Bas():
			self.position =(self.position[0] ,self.position[1]+1)


		if theInput.Gauche() :
			self.position = (self.position[0] - 1,self.position[1]) 


		if theInput.Droite():
			self.position =(self.position[0] +1,self.position[1])

#gestion des bords
		if self.position[0] > self.size[0] : 
			self.position =(0,self.position[1])
			self.__ChangeSpace=True

		if self.position[0] <0 : 
			self.position =(self.size[0],self.position[1])
			self.__ChangeSpace=True

		if self.position[1] > self.size[1] : 
			self.position =(self.position[0],0)
			self.__ChangeSpace=True

		if self.position[1] <0 : 
			self.position =(self.position[0],self.size[1])
			self.__ChangeSpace=True
		
	def Draw(self,screen):
		screen.blit(self.image, self.position) 

	def NeedChangeSpace(self) : 
		temp=self.__ChangeSpace
		self.__ChangeSpace = False;
		return temp;