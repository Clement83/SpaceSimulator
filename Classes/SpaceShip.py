from Classes.ObjectBase import ObjectBase
import Classes.InputHelper
from Classes.PowerSwitch import PowerSwitch

import math
class SpaceShip(ObjectBase) :

	def __init__(self, size,pygame):
		#taille de la zone de dessin
		#self.size = size
		ObjectBase.__init__(self, size,(size[0]/2,size[1]/2),pygame )
		
		tempImage = self.pygame.image.load("Ressources/Images/SpaceShip.png").convert()
		recImage = tempImage.get_rect()
		self.imageBase = self.pygame.transform.scale(tempImage,(recImage.width//2,recImage.height//2))
		self.ReacDroitBase = self.pygame.transform.scale(self.pygame.image.load("Ressources/Images/ReacteurDroit.png").convert(),(recImage.width//2,recImage.height//2))
		self.ReacGaucheBase = self.pygame.transform.scale(self.pygame.image.load("Ressources/Images/ReacteurGauche.png").convert(),(recImage.width//2,recImage.height//2))
		self.ReacCentralBase = self.pygame.transform.scale(self.pygame.image.load("Ressources/Images/ReacteurAux.png").convert(),(recImage.width//2,recImage.height//2))
		self.ReacDroit = self.ReacDroitBase
		self.ReacGauche =self.ReacGaucheBase
		self.ReacCentral = self.ReacCentralBase
		
		self.image = self.imageBase
		self.angle = 0
		self.vitesse = 0
		self.acceleration =0
		self.vitesseMax = 30
		self.desceleration=0.5
		self.accelerationMin=0.2
		
		self.__ChangeSpace = False;
		self.AjoutAngleDroit = 7
		self.AjoutAngleGauche = 7
		
		self.ReacDFire = False
		self.ReacGFire = False
		self.ReacMFire = False
		# pour savoir a quoi serve les switch ce referer au dessin dans le dossier ressource work
		self.powerSwitch = {}
		self.__initPowerSwitch()

	def __initPowerSwitch(self):
		#creation des switchs
		self.powerSwitch[1] = PowerSwitch(1,False,True)
		self.powerSwitch[2] = PowerSwitch(2,False,True)
		self.powerSwitch[3] = PowerSwitch(3,False,True)
		self.powerSwitch[4] = PowerSwitch(4,False,True)
		self.powerSwitch[5] = PowerSwitch(5,False,True)
		self.powerSwitch[6] = PowerSwitch(6,False,True)
		self.powerSwitch[7] = PowerSwitch(7)
		self.powerSwitch[8] = PowerSwitch(8)
		self.powerSwitch[9] = PowerSwitch(9)
		self.powerSwitch[10] = PowerSwitch(10)
		self.powerSwitch[11] = PowerSwitch(11)
		self.powerSwitch[12] = PowerSwitch(12,True,False)
		self.powerSwitch[13] = PowerSwitch(13,True,False)
		self.powerSwitch[14] = PowerSwitch(14,True,False)
		self.powerSwitch[15] = PowerSwitch(15,True,False)
		self.powerSwitch[16] = PowerSwitch(16,True,False)
		
		#creation du graphe
		self.powerSwitch[1].Adjacent = [self.powerSwitch[11],self.powerSwitch[13]]
		self.powerSwitch[2].Adjacent = [self.powerSwitch[10],self.powerSwitch[12]]
		self.powerSwitch[3].Adjacent = [self.powerSwitch[9],self.powerSwitch[10],self.powerSwitch[11]]
		self.powerSwitch[4].Adjacent = [self.powerSwitch[14],self.powerSwitch[7]]
		self.powerSwitch[5].Adjacent = [self.powerSwitch[8],self.powerSwitch[16]]
		self.powerSwitch[6].Adjacent = [self.powerSwitch[7],self.powerSwitch[8],self.powerSwitch[15]]
		self.powerSwitch[7].Adjacent = [self.powerSwitch[4],self.powerSwitch[6],self.powerSwitch[8],self.powerSwitch[14],self.powerSwitch[15]]
		self.powerSwitch[8].Adjacent = [self.powerSwitch[5],self.powerSwitch[6],self.powerSwitch[7],self.powerSwitch[15],self.powerSwitch[16]]
		self.powerSwitch[9].Adjacent = [self.powerSwitch[3],self.powerSwitch[10],self.powerSwitch[11]]
		self.powerSwitch[10].Adjacent = [self.powerSwitch[2],self.powerSwitch[3],self.powerSwitch[9],self.powerSwitch[12]]
		self.powerSwitch[11].Adjacent = [self.powerSwitch[1],self.powerSwitch[3],self.powerSwitch[9],self.powerSwitch[13]]
		self.powerSwitch[12].Adjacent = [self.powerSwitch[10],self.powerSwitch[2]]
		self.powerSwitch[13].Adjacent = [self.powerSwitch[11],self.powerSwitch[1]]
		self.powerSwitch[14].Adjacent = [self.powerSwitch[4],self.powerSwitch[7]]
		self.powerSwitch[15].Adjacent = [self.powerSwitch[7],self.powerSwitch[8],self.powerSwitch[6]]
		self.powerSwitch[16].Adjacent = [self.powerSwitch[8],self.powerSwitch[5]]
		
		
		#TODO pour test 
		self.powerSwitch[9].Etat = True
		self.powerSwitch[10].Etat = True
		
	def Update(self, theInput):
		
		#init react fire
		self.ReacDFire = False
		self.ReacGFire = False
		self.ReacMFire = False


		if theInput.Bas():
			if self.vitesse >0 :
				self.vitesse -= self.desceleration
			if self.vitesse <0 :
				self.vitesse = 0
		
		self.powerSwitch[3].Etat = theInput.Haut()
		self.powerSwitch[1].Etat =  theInput.Gauche()
		self.powerSwitch[2].Etat = theInput.Droite()
		

		
		self.__ReacGauche()
		self.__ReacDroit()
		self.__ReacMillieu()
		
		self.__majPosition()
			
		
	def Draw(self,screen):
		if self.ReacDFire : 
			screen.blit(self.ReacDroit, self.position) 
		if self.ReacGFire :
			screen.blit(self.ReacGauche, self.position)
		if self.ReacMFire :
			screen.blit(self.ReacCentral, self.position) 
		
		screen.blit(self.image, self.position) 
	
	def __incraseSpeed(self,acc) :
		if self.vitesse <self.vitesseMax :
			self.vitesse += acc
	
	def __ChangeAngle(self ,addAngle):
		self.angle += addAngle
		
		if self.angle>360 : 
			self.angle = self.angle - 360
		if self.angle<0 : 
			self.angle = 360 - self.angle
		
	def __isConnecter(self,startNoeud, noeudDejaPasser = []) :
		
		print(str(startNoeud) + ' | -> ' + str(noeudDejaPasser))
		input()
		if self.powerSwitch[startNoeud].IsOpen() :
			noeudDejaPasser.append(startNoeud)
			for noeud in self.powerSwitch[startNoeud].Adjacent:
				if noeud.IsStartOfGraphe() and noeud.IsOpen() : 
					return True
				if noeud.IsOpen() and noeud.Numero not in noeudDejaPasser:
					if self.__isConnecter(noeud.Numero) : 
						return True
		
		return False
		
	def __ReacGauche(self):
		if self.__isConnecter(12) :
			self.__ChangeAngle(self.AjoutAngleGauche)
			self.ReacDFire = True
			self.__incraseSpeed(self.accelerationMin/2)
		
	def __ReacDroit(self):
		if self.__isConnecter(13) :
			self.__ChangeAngle(-self.AjoutAngleDroit)
			self.ReacGFire = True
			self.__incraseSpeed(self.accelerationMin/2)
		
	def __ReacMillieu(self):
		if self.__isConnecter(9) :
			self.__incraseSpeed(self.accelerationMin)
			self.ReacMFire = True
		
	def __majPosition(self) :
	
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
	
	
		#gestion des deplacement
		if self.vitesse > 0 :
			angleRad  = self.deg2rad(self.angle)
			self.position = (self.position[0] - (math.sin(angleRad) * self.vitesse) , self.position[1] - (math.cos(angleRad) * self.vitesse))
			
			centre = self.image.get_rect().center
		
		#gestion de la rotation 
		if self.ReacDFire  or self.ReacGFire :
			self.image = self.pygame.transform.rotate(self.imageBase,self.angle )
			rect = self.image.get_rect()
			rect.center = centre

			self.ReacDroit = self.pygame.transform.rotate(self.ReacDroitBase,self.angle )
			self.ReacGauche = self.pygame.transform.rotate(self.ReacGaucheBase,self.angle )
			self.ReacCentral =self.pygame.transform.rotate(self.ReacCentralBase,self.angle )
	
	def NeedChangeSpace(self) : 
		temp=self.__ChangeSpace
		self.__ChangeSpace = False;
		return temp;
		
	def deg2rad(self,degrees):
		pi = math.pi
		radians = pi * degrees / 180
		return radians