from Tkinter import*
from random import randint

def random_row():
	return randint(1,6)*100
def random_col():
	return randint(1,6)*100
def grid_Lines(x1,y1,x2,y2,Dim,row):
	i=1
	if row:
		while i<10:
			y1+=Dim
			y2+=Dim
			w.create_line(x1, y1, x2, y2, fill='black')
			i+=1
	elif not row:
		while i<10:
			x1+=Dim
			x2+=Dim
			w.create_line(x1, y1, x2, y2, fill='black')
			i+=1
def game_Coords(game_Coord,row,x0,y0,Dim,horizontal_Midpoint):

	if row:
		board_leftHalf=0
		x_pt=(x0+board_leftHalf)/2
		x_alt=x_pt+horizontal_Midpoint
		y_pt=y0+(Dim/2)

		for x in game_Coord:
			w.create_text(x_pt,y_pt,text=x, fill='white')
			w.create_text(x_alt,y_pt,text=x, fill='white')
			y_pt+=Dim
			
	elif not row:
	
		x_pt=x0+(Dim/2)
		x_alt=x_pt+horizontal_Midpoint
		y_pt=y0-Dim
		
		for x in game_Coord:
			w.create_text(x_pt,y_pt, text=x, fill='white')
			w.create_text(x_alt,y_pt, text=x, fill='white')
			x_pt+=Dim 
			x_alt+=Dim

	
	
#Create enemy x,y coordinates for single cell ship
#---------------------------------------------------------------------------------------------------
enemy_row=random_row()
enemy_col=random_col()


#Create list of text to be displayed for columns and rows respectively
#---------------------------------------------------------------------------------------------------
board_colNumbers=['1','2','3','4','5','6','7','8','9','10']
board_rowLetters=['A','B','C','D','E','F','G','H','I','J']


master=Tk()


#Create 1350x700 window and board space created with top left corner point (50,75) and bottom right corner point(625,650)
#---------------------------------------------------------------------------------------------------
w=Canvas(master, width=1350,height=700)
w.pack()
w.create_rectangle(0,0,1350,700, fill='black')
width=1350
height=700
horizontal_Midpoint=675
row_Minimum=0
w.create_text(horizontal_Midpoint, 75, text='BATTLESHOTS', fill='red')


#Create enemy board
#---------------------------------------------------------------------------------------------------
board_shootAtX_0=100			
board_shootAtY_0=175			
board_shootAtX_1=575		
board_shootAtY_1=650	
w.create_rectangle(board_shootAtX_0, board_shootAtY_0, board_shootAtX_1, board_shootAtY_1, fill= 'white')


#Create own board:Translation of x coordinates to the right (+x direction) by half the length of the board
#---------------------------------------------------------------------------------------------------
board_protectX_0=board_shootAtX_0+horizontal_Midpoint
board_protectY_0=board_shootAtY_0
board_protectX_1=board_shootAtX_1+horizontal_Midpoint
board_protectY_1=board_shootAtY_1
w.create_rectangle(board_protectX_0, board_protectY_0, board_protectX_1, board_protectY_1, fill= 'white')


#Variables for use in functions
#---------------------------------------------------------------------------------------------------

box_Dim=(board_shootAtX_1-board_shootAtX_0)/10	#Dimensions of each cell square (cuz a 'squares length'=='its width' you turkey)
row=True										#Switch for row/column interchangable tasks


#Creates grid lines for rows and columns
#---------------------------------------------------------------------------------------------------

#Enemy board
grid_Lines(board_shootAtX_0, board_shootAtY_0, board_shootAtX_1, board_shootAtY_0, box_Dim, row)
grid_Lines(board_shootAtX_0, board_shootAtY_0, board_shootAtX_0, board_shootAtY_1, box_Dim, not row)

#Own board
grid_Lines(board_protectX_0, board_protectY_0, board_protectX_1, board_protectY_0, box_Dim, row)
grid_Lines(board_protectX_0, board_protectY_0, board_protectX_0, board_protectY_1, box_Dim, not row)


#Creates visual letters and numbers representing the attack coordinates
#---------------------------------------------------------------------------------------------------

#Enemy board
game_Coords(board_rowLetters, row, board_shootAtX_0, board_shootAtY_0, box_Dim, horizontal_Midpoint)
game_Coords(board_colNumbers, not row, board_shootAtX_0, board_shootAtY_0, box_Dim, horizontal_Midpoint)		
		
#Own board
#game_Coords(board_rowLetters, row, board_protectX_0, board_protectY_0, box_Dim, horizontal_Midpoint)
#game_Coords(board_colNumbers, not row, board_protectX_0, board_protectY_0, box_Dim, row_Minimum)


class Button(Frame):
	def __init__(self, parent):
		Frame.__init__(self, parent)
		
		self.parent = parent
		self.initUI()
		
	def initUI(self):
		self.parent.title("Quit button")
		self.style=Style()
		self.style.theme_use('default')
		
		self.pack(fill=BOTH, expand=1)
		
		quitButton=Button(self, text='Quit', command=self.quit)
		quitButton.place(x=50,y=50)















#Fills each individual cell with an 0 at the exact center, this build displays the string 'enemy' in the cell positioned determined by randomly
#ty=100	
#while ty<650:								#Board generaton
#	tx=100
#	while tx<650:
#		if tx != enemy_row or ty != enemy_col:
#			w.create_text(tx,ty,text='0')
#		else:
#			w.create_text(enemy_row, enemy_col, text='Enemy')
#		tx+=100
#	ty+=100


	
	
	
mainloop()