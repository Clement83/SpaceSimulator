import sys, pygame

class InputHelper :

	def __init__(self) :
		self.KeyEvent=dict([('quit', False), ('haut', False), ('bas', False), ('gauche', False), ('droite', False)])

	def GetInput(self,pyEvent):

		for event in pyEvent:
			if event.type == pygame.QUIT: self.KeyEvent['quit'] = True 
			
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					self.KeyEvent['gauche'] = True
				if event.key == pygame.K_UP:
					self.KeyEvent['haut'] = True
				if event.key == pygame.K_RIGHT:
					self.KeyEvent['droite'] = True
				if event.key == pygame.K_DOWN:
					self.KeyEvent['bas'] = True

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					self.KeyEvent['gauche'] = False
				if event.key == pygame.K_UP:
					self.KeyEvent['haut'] = False
				if event.key == pygame.K_RIGHT:
					self.KeyEvent['droite'] = False
				if event.key == pygame.K_DOWN:
					self.KeyEvent['bas'] = False


	def Quit(self): 
		return self.KeyEvent['quit']

	def Haut(self):
		return self.KeyEvent['haut']

	def Bas(self):
		return self.KeyEvent['bas']

	def Gauche(self):
		return self.KeyEvent['gauche']

	def Droite(self):
		return self.KeyEvent['droite']


# Lettres:
# K_a ... K_z

# Nombres:
# K_0 ... K_9

# Controles:
# K_TAB
# K_RETURN
# K_ESCAPE
# K_SCROLLOCK
# K_SYSREQ
# K_BREAK
# K_DELETE
# K_BACKSPACE
# K_CAPSLOCK
# K_CLEAR
# K_NUMLOCK

# Ponctuation:
# K_SPACE
# K_PERIOD
# K_COMMA
# K_QUESTION
# K_AMPERSAND
# K_ASTERISK
# K_AT
# K_CARET
# K_BACKQUOTE
# K_DOLLAR
# K_EQUALS
# K_EURO
# K_EXCLAIM
# K_SLASH, K_BACKSLASH
# K_COLON, K_SEMICOLON
# K_QUOTE, K_QUOTEDBL
# K_MINUS, K_PLUS
# K_GREATER, K_LESS

# Parenthèses:
# K_RIGHTBRACKET, K_LEFTBRACKET
# K_RIGHTPAREN, K_LEFTPAREN

# Touches F:
# K_F1 ... K_F15

# Touches d'édition:
# K_HELP
# K_HOME
# K_END
# K_INSERT
# K_PRINT
# K_PAGEUP, K_PAGEDOWN
# K_FIRST, K_LAST

# Clavier numérique:
# K_KP0 ... K_KP9
# K_KP_DIVIDE
# K_KP_ENTER
# K_KP_EQUALS
# K_KP_MINUS
# K_KP_MULTIPLY
# K_KP_PERIOD
# K_KP_PLUS

# SHF,CTL,ALT etc:
# K_LALT, K_RALT
# K_LCTRL, K_RCTRL
# K_LSUPER, K_RSUPER
# K_LSHIFT, K_RSHIFT
# K_RMETA, K_LMETA

# Flèches:
# K_LEFT
# K_UP
# K_RIGHT
# K_DOWN

# Autres:
# K_MENU
# K_MODE
# K_PAUSE
# K_POWER
# K_UNDERSCORE
# K_HASH