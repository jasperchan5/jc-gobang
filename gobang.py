import numpy as np
import random as rd
import pygame
class Gobang:
    # Initialize the court
    def __init__(self):
        pygame.init()
        self.court = np.empty((15,15),dtype=object)
        self.gameScreen = 0
        self.backgroundColor = (114,167,233,0.5)
    def initGame(self,resolution): # Create a blank game interface

        # Create screen
        gameScreen = pygame.display.set_mode(resolution)
        pygame.display.set_caption("Gobang")
        gameScreen.fill(self.backgroundColor)

        # Create title
        title = pygame.font.SysFont(None, 60)
        renderedTitle = title.render("Gobang",True,(0,0,0))
        gameScreen.blit(renderedTitle,(10,10))

        # Create rows and columns
        for i in range(0,15):
            pygame.draw.rect(gameScreen,(0,0,0,0.5),pygame.Rect(100+30*i,100,2,422))
            pygame.draw.rect(gameScreen,(0,0,0,0.5),pygame.Rect(100,100+30*i,422,2))
        pygame.display.update()
        return gameScreen
    
    def displayChess(self,gameScreen,pos,color):

        # Adjust location
        if pos[0] >= 85 and pos [0] < 535 and pos[1] >= 85 and pos[1] < 535:
            posList = [pos[0],pos[1]]
            coord = self.posAdjustment(posList)
            pos = (posList[0],posList[1])

            pygame.draw.rect(gameScreen, self.backgroundColor, pygame.Rect(500,10,180,60))
            posText = pygame.font.SysFont(None, 60)
            tempStr = ""
            tempStr += str(coord[0]) + "," + str(coord[1])
            renderedTitle = posText.render(tempStr,True,(0,0,0))
            gameScreen.blit(renderedTitle,(500,10))

            # Display chess
            newChess = Chess(gameScreen,pos,color)
            pygame.draw.circle(newChess.surface, newChess.color, newChess.center, newChess.radius)
            if color == (0,0,0):
                self.court[coord[0]][coord[1]] = 1
            else:
                self.court[coord[0]][coord[1]] = 0
            pygame.display.update()
    
    # To avoid location mistake
    def posAdjustment(self,pos):
        coord = [-1,-1]
        for i in range(0,15):
            if pos[0] >= 100 + (30*i) - 15 and pos[0] < 100 + (30*i) +15:
                pos[0] = 100 + (30*i)
                coord[0] = i
            if pos[1] >= 100 + (30*i) -15 and pos[1] < 100 + (30*i) +15:
                pos[1] = 100 + (30*i)
                coord[1] = i
        return coord
    
    def endGame(self):
        # Case column
        for i in range(0,15):
            blackWinCnt = 0
            for j in range(0,15):
                try:
                    if self.court[i][j] == 1:
                        blackWinCnt += 1
                    else: 
                        blackWinCnt = 0
                    if blackWinCnt == 5:
                        return "Black wins"
                except:
                    return "Nothing"
        # Case row
        for i in range(0,15):
            blackWinCnt = 0
            for j in range(0,15):
                try:
                    if self.court[j][i] == 1:
                        blackWinCnt += 1
                    else: 
                        blackWinCnt = 0
                    if blackWinCnt == 5:
                        return "Black wins"
                except:
                    return "Nothing"
        # Case slant

class Chess:

    def __init__(self,surface,center,color):
        self.surface = surface
        self.center = center
        self.color = color
        self.radius = 10

class rivalBot:

    def __init__(self) -> None:
        self.locationScore = 0
    
    # def findLocation(self):
        