from Tkinter import *
import sys
 
class application:
 	def click(self, event):
 		print "Clicked ", event.x, event.y
 
 	def __init__(self, master=None):
 		self.master = master
 
 		for r in range(3):
 			for c in range(3):
 				lbl = Label(master, text = 1000 + r + c)
 				lbl.grid(row = r, column = c, sticky = NSEW)
 				
root = Tk()
g = application(root)
root.bind("<Button-1>", g.click)
root.mainloop()
