import pygame, sys

#Initialize the pygame module
pygame.init()

#Font init
try:
    pygame.ftfont.init()
except:
    pygame.font.init()

#Setting variables
white = (255,255,255)
black = (0,0,0)
i = 0
width = 620
height = 620
play1 = False
play2 = False

#Initialize screen and mouse
screen = pygame.display.set_mode((width,height))
pygame.display.set_caption("Tic Tac Toe")
pygame.mouse.set_visible(1)

#Font variables
font = pygame.font.SysFont("arial", 72)
winningText1 = font.render("Victory player 1!", True, (0,0, 0))
winningText2 = font.render("Victory player 2!", True, (0,0, 0))

# Handling the logic, 0 for empty, 1 for X, 2 for O
board = [[0,0,0],[0,0,0],[0,0,0]]

#Loads image
background = pygame.image.load("background.png")
circle = pygame.image.load("circle.png")
empty = pygame.image.load("empty.png")
cross = pygame.image.load("cross.png")

#"Draws"/blit image on screen
screen.blit(background,(0,0))
tl = screen.blit(empty, (0,0))
tm = screen.blit(empty, (215,0))
tr = screen.blit(empty, (430,0))
ml = screen.blit(empty, (0,215))
mm = screen.blit(empty, (215,215))
mr = screen.blit(empty, (430,215))
bl = screen.blit(empty, (0,430))
bm = screen.blit(empty, (215,430))
br = screen.blit(empty, (430,430))

#Update screen to make changes visible
pygame.display.flip()

#Defining a variable to control the main loop
running = True


#Check for winning move
def win (board,winningText1,winningText2):
	
	#Horizontal player1
	if(board[0][0]==1 and board[0][1]==1 and board[0][2] == 1):
		draw(board)
		screen.blit(winningText1, (0,300))
		pygame.display.flip()
	if(board[1][0]==1 and board[1][1]==1 and board[1][2] == 1):
		draw(board)
		pygame.draw.line(screen, black, (0,300),(600,300),10)
		screen.blit(winningText1, (0,300))
		pygame.display.flip()
	if(board[2][0]==1 and board[2][1]==1 and board[2][2] == 1):
		draw(board)
		screen.blit(winningText1, (0,300))
		pygame.display.flip()

	#Horizontal player2
	if(board[0][0]==2 and board[0][1]==2 and board[0][2] == 2):
		draw(board)
		screen.blit(winningText2, (0,300))
		pygame.display.flip()
	if(board[1][0]==2 and board[1][1]==2 and board[1][2] == 2):
		draw(board)
		screen.blit(winningText2, (0,300))
		pygame.display.flip()
	if(board[2][0]==2 and board[2][1]==2 and board[2][2] == 2):
		draw(board)
		screen.blit(winningText2, (0,300))
		pygame.display.flip()
	
	#Vertical player1
	if(board[0][0]==1 and board[1][0]==1 and board[2][0] == 1):
		draw(board)
		screen.blit(winningText1, (0,300))
		pygame.display.flip()
	if(board[0][1]==1 and board[1][1]==1 and board[2][1] == 1):
		draw(board)
		screen.blit(winningText1, (0,300))
		pygame.display.flip()
	if(board[2][0]==1 and board[2][1]==1 and board[2][2] == 1):
		draw(board)
		screen.blit(winningText1, (0,300))
		pygame.display.flip()

	#Vertical player2
	if(board[0][0]==2 and board[1][0]==2 and board[2][0] == 2):
		draw(board)
		screen.blit(winningText2, (0,300))
		pygame.display.flip()
	if(board[0][1]==2 and board[1][1]==2 and board[2][1] == 2):
		draw(board)
		screen.blit(winningText2, (0,300))
		pygame.display.flip()
	if(board[0][2]==2 and board[1][2]==2 and board[2][2] == 2):
		draw(board)
		screen.blit(winningText2, (0,300))
		pygame.display.flip()

	#Cross player1
	if(board[0][0]==1 and board[1][1]==1 and board[2][2] == 1):
		draw(board)
		screen.blit(winningText1, (0,300))
	if(board[0][2]==1 and board[1][1]==1 and board[2][0] == 1):
		draw(board)
		screen.blit(winningText1, (0,300))

	#Cross player2
	if(board[0][0]==2 and board[1][1]==2 and board[2][2] == 2):
		draw(board)
		screen.blit(winningText2, (0,300))
	if(board[0][2]==2 and board[1][1]==2 and board[2][0] == 1):
		draw(board)
		screen.blit(winningText2, (0,300))



def draw (board):

	#Horizontal player 1
	if(board[0][0]==1 and board[0][1]==1 and board[0][2] == 1):
			pygame.draw.line(screen, black, (0,100),(600,100),10)
	if(board[1][0]==1 and board[1][1]==1 and board[1][2] == 1):
			pygame.draw.line(screen, black, (0,300),(600,300),10)
	if(board[2][0]==1 and board[2][1]==1 and board[2][2] == 1):
			pygame.draw.line(screen, black, (0,500),(600,500),10)
	
	#Horizontal player2
	if(board[0][0]==2 and board[0][1]==2 and board[0][2] == 2):
			pygame.draw.line(screen, black, (0,100),(600,100),10)
	if(board[1][0]==2 and board[1][1]==2 and board[1][2] == 2):
			pygame.draw.line(screen, black, (0,300),(600,300),10)
	if(board[2][0]==2 and board[2][1]==2 and board[2][2] == 2):
			pygame.draw.line(screen, black, (0,500),(600,500),10)
	
	#Vertical player 1
	if(board[0][0]==1 and board[1][0]==1 and board[2][0] == 1):
			pygame.draw.line(screen, black, (100,0),(100,600),10)
	if(board[0][1]==1 and board[1][1]==1 and board[2][1] == 1):
			pygame.draw.line(screen, black, (300,0),(300,600),10)
	if(board[0][2]==1 and board[1][2]==1 and board[2][2] == 1):
			pygame.draw.line(screen, black, (500,0),(500,600),10)

	#Vertical player 2
	if(board[0][0]==2 and board[1][0]==2 and board[1][2] == 2):
			pygame.draw.line(screen, black, (100,0),(100,600),10)
	if(board[0][1]==2 and board[1][1]==2 and board[2][1] == 2):
			pygame.draw.line(screen, black, (300,0),(300,600),10)
	if(board[0][2]==2 and board[1][2]==2 and board[2][2] == 2):
			pygame.draw.line(screen, black, (500,0),(500,600),10)

	#Cross player 1
	if(board[0][0]==1 and board[1][1]==1 and board[2][2] == 1):
			pygame.draw.line(screen, black, (0,0),(600,600),10)
	if(board[0][2]==1 and board[1][1]==1 and board[2][0] == 1):
			pygame.draw.line(screen, black, (600,0),(0,600),10)

	#Cross player 2
	if(board[0][0]==2 and board[1][1]==2 and board[2][2] == 2):
			pygame.draw.line(screen, black, (0,0),(600,600),10)
	if(board[0][2]==2 and board[1][1]==2 and board[2][0] == 2):
			pygame.draw.line(screen, black, (600,0),(0,600),10)

#main loop
while running:
	#handles events, gets all event from the eventqueue
	for event in pygame.event.get():
		#screen.fill(white)
		pygame.display.update()
		if event.type == pygame.QUIT:
			running = False
		#Activates on mouseclick
		if(event.type == pygame.MOUSEBUTTONDOWN and event.button == 1):
					pos = pygame.mouse.get_pos()
					if tl.collidepoint(pos):
						if (i % 2 == 1):
							screen.blit(circle, (10,0))
							board[0][0]=2
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
						else:
							screen.blit(cross, (10,0))
							board[0][0]=1
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()

					if tm.collidepoint(pos):
						if (i % 2 == 1):
							screen.blit(circle, (215,0))
							board[0][1]=2
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
						else:
							screen.blit(cross, (215,0))
							board[0][1]=1
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
					if tr.collidepoint(pos):
						if (i % 2 == 1):
							screen.blit(circle, (430,0))
							board[0][2]=2
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
						else:
							screen.blit(cross, (430,0))
							board[0][2]=1
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()

					if ml.collidepoint(pos):
						if (i % 2 == 1):
							screen.blit(circle, (10,215))
							board[1][0]=2
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
						else:
							screen.blit(cross, (10,215))
							board[1][0]=1
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()

					if mm.collidepoint(pos):
						if (i % 2 == 1):
							screen.blit(circle, (215,215))
							board[1][1]=2
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
						else:
							screen.blit(cross, (215,215))
							board[1][1]=1
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()

					if mr.collidepoint(pos):
						if (i % 2 == 1):
							screen.blit(circle, (430,215))
							board[1][2]=2
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
						else:
							screen.blit(cross, (430,230))
							board[1][2]=1
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()

					if bl.collidepoint(pos):
						if (i % 2 == 1):
							screen.blit(circle, (10,430))
							board[2][0]=2
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
						else:
							screen.blit(cross, (10,430))
							board[2][0]=1
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()

					if bm.collidepoint(pos):
						if (i % 2 == 1):
							screen.blit(circle, (215,430))
							board[2][1]=2
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
						else:
							screen.blit(cross, (215,430))
							board[2][1]=1
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip

					if br.collidepoint(pos):
						if (i % 2 == 1):
							screen.blit(circle, (430,430))
							board[2][2]=2
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
						else:
							screen.blit(cross, (430,430))
							board[2][2]=1
							i += 1
							win(board,winningText1,winningText2)
							pygame.display.flip()
pygame.quit()