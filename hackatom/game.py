import pygame,sys
from main import Engine
from random import randint
from rakieta import Rakieta

white= (255,255,255)
red = (255,0,0)
green = (0,200,0)
blue = (0,0,200)
black = (50,50,50)
yellow = (255,255,0)
m = 3000000 #Vessel mass in kg
ft = 35000000 #Force thrust in N
fg = -9.8 #Force of gravity
x = 0 #starting postion
v = 0 #Starting velocity
dt = 0.1 #Delta time in s 
FU = 1000 #Fuel usage in kg/s
class game():
	def __init__(self, width, height):
		self.engine = Engine(m,ft,fg,x,v,dt,FU)

		self.width = width
		self.height = height
		self.size = self.width, self.height
		self.scale = int(round(self.width*self.height/30000,0))
		print(self.scale)
		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption("Jebnie?")
		self.BigKutafont = pygame.font.Font('penistypography.ttf',self.scale*3)
		self.MediumKutafont = pygame.font.Font('penistypography.ttf',self.scale*2)
		self.SmallKutafont = pygame.font.Font('penistypography.ttf',self.scale*1)
		self.BigNumberFont = pygame.font.SysFont('Comic Sans MS',self.scale*3)
		self.MediumNumberFont = pygame.font.SysFont('Comic Sans MS',self.scale*2)
		self.SmallNumberFont = pygame.font.SysFont('Comic Sans MS',self.scale*1)
		self.clock = pygame.time.Clock()
		self.stopped = False
		self.startsim = False
		self.rakieta = Rakieta(self.width, self.height,self.screen)
		self.screen.fill(blue)

	def _menu(self):
		self.title = self.BigKutafont.render('Lecimy jak rakieta',True,white)
		self.screen.blit(self.title,(self.width/2,50))
	def _drawCloud(self): 
		for i in range(1,16):  
			self.size=randint(20,70)
			self.xOffset=randint(-40,40)
			self.yOffset=randint(-30,30)
			pygame.draw.ellipse(self.screen,white,[100+self.xOffset,100+self.yOffset,50,50])		#100+xOffset,100+yOffset,size,size
	def _height_index(self,value):
		self.index = self.SmallNumberFont.render(str(round(value,0)),True,white)
		self.screen.blit(self.index,(0,0))
	def _rungame(self):
		self.running = True
		self._drawCloud()
		while self.running:
			self.clock.tick(30)
			self.rakieta._rotate_rakieta(40)
			self.rakieta._blit_rakieta()
			self._height_index(self.engine.x)
			self.keys = pygame.key.get_pressed()
			self.engine._update_position_and_speed()

			if self.startsim == False:
				self._menu()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					self.running = False
				if event.type == pygame.KEYUP:
					if self.keys[pygame.K_UP]:
						self.engine._change_ft(1000000)
						print(1)
				if self.keys[pygame.K_DOWN]:
					self.engine._change_ft(-10000)


			pygame.display.flip()
		pygame.quit()
g = game(1000,600)
g._rungame()
#engine._launch()




