from Tkinter import *
import math

c = Canvas(width = 400, height = 400)

class turtle():
    def __init__(self, can, x, y, angle):
				self.x = x
				self.y = y
				self.angle = angle
				self.can = can
				self.can.pack()
				self.a = can.create_polygon(x+15,y,x,y-5,x,y+5)
				self.hidden=1
				self.draw=1

    def move_forward(self, dist):
				""" Makes the turtle move forward a certain distance """
				x1 = self.x + dist * math.cos((self.angle / 180.00) * 3.14)
				y1 = self.y - dist* math.sin((self.angle / 180.00) * 3.14)
				if self.draw:
					self.can.create_line(self.x, self.y, x1, y1)
				self.x = x1
				self.y = y1
				self.can.move(self.a, dist * math.cos((self.angle / 180.00) * 3.14), -(dist * math.sin((self.angle / 180.00) * 3.14)))

    def rotate(self, angle):
				""" Rotates the turtle at a certain angle"""
				self.angle = self.angle+angle
				self.can.delete(self.a)
				self.x1 = self.x + 15 * math.cos((self.angle / 180.00) * 3.14)
				self.y1 = self.y - 15 * math.sin((self.angle / 180.00) * 3.14)
				self.x2 = self.x + 5 * math.cos(((90 + self.angle) / 180.00) * 3.14)
				self.y2 = self.y - 5 * math.sin(((90 + self.angle) / 180.00) * 3.14)
				self.x3 = self.x + 5 * math.cos(((270 + self.angle) / 180.00) * 3.14)
				self.y3 = self.y - 5 * math.sin(((270 + self.angle) / 180.00) * 3.14)
				x,y=self.x1,self.y1
				if self.hidden:
					self.a = self.can.create_polygon(self.x1, self.y1, self.x2, self.y2, self.x3, self.y3)	    	
	 	
    def hide(self):
			"""Hides the turtle"""
			self.hidden=0
    def view(self):
			"""Exposes the turtle"""
			self.hidden=1
    def pendown(self):
			"""Prevents drawing on the screen"""
			self.draw=0
    def penup(self):
			"""Allows drawing on the screen"""
			self.draw=1

