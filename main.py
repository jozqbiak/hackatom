import numpy
import pygame
class Engine():
	def __init__(self,m,ft,fg,x,v,dt,FU):			#Mass, Force of Thrust, Force of Gravity, Starting position, starting velocity, delta time, Fuel Usage
		self.m = m
		self.ft = ft
		self.fg = fg
		self.x = x
		self.v = v
		self.fin = False
		self.dt = dt
		self.timepassed = 0
		self.FU = FU
	def _update_mass(self):							#Function updating mass by subtracting it's fuel usage multipied by delta time						
		self.mass = self.mass - self.FU*self.dt
		self.empty = 0
	def _update_position_and_speed(self):
		self.v = self.v + self.fg * self.dt + (ft/m)* self.dt
		self.x = self.x + self.v * self.dt 		    		  #Function updating position and speed form the formulas
	def _launch(self):
		while self.fin == False:
			self._update_position_and_speed()
			self.timepassed = self.timepassed + self.dt
			print("x -",self.x,"v - (",self.v,")t -",self.timepassed)
			if self.x > 2000:
				self.fin = True														  #Testing function simulating rocket launch with maximal thrust until the rocket reaches 2000 m 

m = 3000000 #Vessel mass in kg
ft = 35000000 #Force thrust in N
fg = -9.8 #Force of gravity
x = 0 #starting postion
v = 0 #Starting velocity
dt = 0.1 #Delta time in s 
FU = 1000 #Fuel usage in kg/s
program = Engine(m,ft,fg,x,v,dt,FU)
program._launch()
