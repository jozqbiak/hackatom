import pygame,sys
white= (255,255,255)
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
black = (0,0,0)

class Rakieta(pygame.sprite.Sprite):
	def __init__(self,width,height,screen):
		self.width = width
		self.height = height
		self.screen = screen
		pygame.sprite.Sprite.__init__(self)
		self.rakieta = pygame.image.load('rakieta.png').convert_alpha()
		self.left_roation = 0
		self.rakieta_rect = self.rakieta.get_rect(center = (self.width/2, self.height-self.height/3.5))
		print(self.rakieta_rect)
	def _blit_rakieta(self):
		self.screen.blit(self.rakieta,self.rakieta_rect)
	def _rotate_rakieta(self,a):
		pygame.transform.rotate(self.rakieta, a)
		self.rakieta_rect = self.rakieta.get_rect(center = (self.width/2, self.height-self.height/3.5))



	def _turbulences(self):
		if self.left_roation == 0:
			self.left_roation =+1
			pygame.transform.rotate(self.rakieta, -3)
		elif self.left_roation == 1:
			self.left_roation =+1
			pygame.transform.rotate(self.rakieta, 3)
		elif self.left_roation == 2:
			self.left_roation =+1
			pygame.transform.rotate(self.rakieta, 3)
		elif self.left_roation == 3:
			pygame.transform.rotate(self.rakieta, -3)
			self.left_roation = 0

