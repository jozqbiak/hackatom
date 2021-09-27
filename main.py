import numpy
import pygame
class Engine():
	def __init__(self,m,ft,fg,x,v,dt):			#Mass, Force of Thrust, Force of Gravity, Starting position, starting velocity, delta time,
		self.m = m
		self.ft = ft
		self.fg = fg
		self.x = x
		self.v = v
		self.fin = False
		self.dt = dt
		self.timepassed = 0
		self.maxa = ft/m

	def start(self):
		while self.fin == False:
			self.v = self.v + self.fg*self.dt
			self.x = self.x + self.v*self.dt
			self.timepassed = self.timepassed + self.dt
			print("x -",self.x,"v - (",self.v,")t -",self.timepassed)
			if self.x < 0:
				self.fin = True
	def launch(self):
		while self.fin == False:
			self.v = self.v + self.fg * self.dt + self.maxa * self.dt
			self.x = self.x + self.v * self.dt 
			self.timepassed = self.timepassed + self.dt
			print("x -",self.x,"v - (",self.v,")t -",self.timepassed)
			if self.x > 2000 or self.timepassed > 10:
				self.fin = True

m = 3000000 #Vessel mass in kg
ft = 35000000 #Force thrust in N
fg = -9.8 #Force of gravity
x = 0 #starting postion
v = 0 #Starting velocity
dt = 0.1 #Delta time in s 
program = Engine(m,ft,fg,x,v,dt)
program.launch()
