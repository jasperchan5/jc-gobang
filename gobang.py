import numpy as np
import random as rd
import math 
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
            whiteWinCount = 0
            for j in range(0,15):
                if self.court[j][i] == 1:
                    blackWinCnt += 1
                    whiteWinCount = 0
                elif self.court[j][i] == 0:
                    whiteWinCount += 1
                    blackWinCnt = 0
                else: 
                    whiteWinCount = 0
                    blackWinCnt = 0
                if blackWinCnt == 5:
                    return "Black wins"
                elif whiteWinCount == 5:
                    return "White wins"
                
        # Case row
        for i in range(0,15):
            blackWinCnt = 0
            whiteWinCount = 0
            for j in range(0,15):
                if self.court[i][j] == 1:
                    blackWinCnt += 1
                    whiteWinCount = 0
                elif self.court[i][j] == 0:
                    whiteWinCount += 1
                    blackWinCnt = 0
                else: 
                    whiteWinCount = 0
                    blackWinCnt = 0
                if blackWinCnt == 5:
                    return "Black wins"
                elif whiteWinCount == 5:
                    return "White wins"
        # Case slant
        for i in range(0,15):
            blackWinCnt = 0
            whiteWinCount = 0
            for j in range(0,15):
                temp = i
                if self.court[i][j] == 1:
                    blackWinCnt += 1
                    whiteWinCount = 0
                    if i < 15:
                        i += 1
                    elif i == 14 and blackWinCnt < 5:
                        return "Nothing"
                elif self.court[i][j] == 0:
                    whiteWinCount += 1
                    blackWinCnt = 0
                    if i < 15:
                        i += 1
                    elif i ==14 and whiteWinCount < 5:
                        return "Nothing"
                else: 
                    blackWinCnt = 0
                    whiteWinCount = 0
                if blackWinCnt == 5:
                    return "Black wins"
                elif whiteWinCount == 5:
                    return "White wins"
                i = temp
                    
        for i in range(0,15):
            blackWinCnt = 0
            whiteWinCount = 0
            for j in range(0,15):
                temp = i
                if self.court[i][j] == 1:
                    blackWinCnt += 1
                    whiteWinCount = 0
                    if i > 0:
                        i -= 1
                    elif i == 0 and blackWinCnt < 5:
                        return "Nothing"
                elif self.court[i][j] == 0:
                    whiteWinCount += 1
                    blackWinCnt = 0
                    if i > 0:
                        i -= 1
                    elif i == 0 and whiteWinCount < 5:
                        return "Nothing"
                else: 
                    blackWinCnt = 0
                    whiteWinCount = 0
                if blackWinCnt == 5:
                    return "Black wins"
                elif whiteWinCount == 5:
                    return "White wins"
                i = temp
                
class Chess:

    def __init__(self,surface,center,color):
        self.surface = surface
        self.center = center
        self.color = color
        self.radius = 10

class RivalBot:

    def __init__(self):
        self.locationScore = 0
        self.maxScore = 0
        self.locationX = -1
        self.locationY = -1
    
    def findLocation(self,nowCourt):
        perfectX = -1
        perfectY = -1
        self.locationScore = 0
        self.maxScore = 0
        for i in range(0,15):
            for j in range(0,15):
                self.locationX = i
                self.locationY = j
                if nowCourt[self.locationX][self.locationY] == 1 or nowCourt[self.locationX][self.locationY] == 0:
                    continue
                else:
                    self.locationScore = self.calculateScore([self.locationX,self.locationY],nowCourt)
                    if self.locationScore > self.maxScore:
                        self.maxScore = self.locationScore
                        perfectX = i
                        perfectY = j

        realPos = (100 + 30*perfectX,100 + 30*perfectY)
        self.locationX = perfectX
        self.locationY = perfectY
        return realPos

    def displayChess(self,pos,gameScreen,color,nowCourt):
        # Display chess

        pygame.draw.rect(gameScreen, Gobang().backgroundColor, pygame.Rect(500,10,180,60))
        posText = pygame.font.SysFont(None, 30)
        tempStr = ""
        tempStr += str(pos[0]) + "," + str(pos[1])
        print(pos[0],pos[1])
        renderedTitle = posText.render(tempStr,True,(0,0,0))
        gameScreen.blit(renderedTitle,(500,10))

        newChess = Chess(gameScreen,pos,color)
        pygame.draw.circle(newChess.surface, newChess.color, newChess.center, newChess.radius)
        if color == (0,0,0):
            nowCourt[self.locationX][self.locationY] = 1
        else:
            nowCourt[self.locationX][self.locationY] = 0
        pygame.display.update()

    def calculateScore(self,pos,nowCourt):
        score = 0
        # Case row
        for i in range(0,15):
            score += 100
            blackCnt = 0
            whiteCnt = 0
            for j in range(0,15):
                if i != pos[0] and j != pos[1]:
                    if nowCourt[i][j] == 0:
                        blackCnt += 1
                        whiteCnt = 0
                        score += (500 - math.sqrt(math.pow(i-pos[0],2) + math.pow(j-pos[1],2))) * (blackCnt + 1)
                    elif nowCourt[i][j] == 1:
                        whiteCnt += 1
                        blackCnt = 0
                        score += (400 - math.sqrt(math.pow(i-pos[0],2) + math.pow(j-pos[1],2))) * (whiteCnt + 1)
        return score
