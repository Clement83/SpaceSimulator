import sys, pygame
from Classes.Space import Espace
from Classes.SpaceShip import SpaceShip
from Classes.InputHelper import InputHelper

pygame.init()
 
size = width, height = 800, 600
speed = [2, 2]
 
screen = pygame.display.set_mode(size)
 
mySpace = Espace(size)
player = SpaceShip(size,pygame)

inputHelper = InputHelper()

while 1:
	inputHelper.GetInput(pygame.event.get())
 	
	if(inputHelper.Quit()):
 		sys.exit()
	# ballrect = ballrect.move(speed) 
	# if ballrect.left < 0 or ballrect.right > width:
		# speed[0] = -speed[0]
	# if ballrect.top < 0 or ballrect.bottom > height:
		# speed[1] = -speed[1]
	
	#update des elements du jeux 
	mySpace.Update(player.NeedChangeSpace())
	player.Update(inputHelper)
	#affichage des elements du jeux
	mySpace.Draw(screen,pygame)
	player.Draw(screen)
   
	pygame.display.flip()