#Bandar Al Aish

import pygame
import math
from electron import *

class Atom():
    def __init__(self, type, x, y):
        self.atomType = type
        self.x = x
        self.y = y
        self.radius = 15
        self.zoom = 0
        self.electronPositions = [()]
        self.electrons = []
        self.font = pygame.font.Font("freesansbold.ttf", 32)
        self.text = self.font.render(self.atomType, True, (0,0,0))
        self.infoFont = pygame.font.Font("freesansbold.ttf", 17)
        self.infoText = "n Bond type: Ionic n n Defintion: The electrostatic force of attraction between a positive and negative ion n n Explanation: Sodium has 1 electron in its outer shell and chlorine has 7. To get a full outershell, chlorine must receive 1 electron to have 8 and sodium must lose 1 to have 8 in the shell underneath. To do this, sodium gives its 1 electron to become Na+ and chlorine receives the electron, becoming Cl- n n Properties: n Giant ionic lattices have: n .High melting and boiling points: n The many strong electrostatic forces of attraction between the postive and negative ions in the lattice requires a lot of energy to break n .Conduct electricity when molten or in a solution: n The negative ions, when molten or in a solution, are free to move around. Their free movement conduct electricity"
        

        if "-" in self.atomType:
            for i in range(6):
                self.electrons.append(Electron("r"))
            self.electrons.append(Electron("b"))
        
        if self.atomType == "Na":
            self.electrons.append(Electron("b"))
        
        if self.atomType == "Cl":
            for i in range(7):
                self.electrons.append(Electron("r"))



    def update(self, zoomCount, mode):
        self.font = pygame.font.Font('freesansbold.ttf', 10+(5*self.zoom))
        self.text = self.font.render(self.atomType, True, (0,0,0))
        self.zoom = zoomCount+3
        if mode == "ionicBonding":
            self.zoom -= 97
        self.radius = self.zoom*10
        for electron in self.electrons:
            electron.update(mode)

    def draw(self, screen, mode):
        pygame.draw.circle(screen, (100,100,100), (self.x, self.y), self.radius, 1)
        pygame.draw.circle(screen, (100,100,100), (self.x, self.y), self.radius-3*self.zoom)
        screen.blit(self.text, (self.x-(16+(3*self.zoom)), self.y-(16+(5*self.zoom))//2))
        offSet = 2*self.zoom
        offSetfactor = math.sqrt(self.radius**2 - offSet**2)

        #Draw info
        if mode == "ionicBonding":
            textBoxX = 900
            textBoxY = 20
            pygame.draw.rect(screen, (255,255,255), (textBoxX, textBoxY,1280-textBoxX,550))
            #Creates text wrapping
            text = self.infoText.split(" ")

            lenX = 0
            lenY = 0
            for word in text:
                currentWord = self.infoFont.render(word, True, (0,0,0))
                if word == "n":
                    lenY += currentWord.get_height() + 4
                    lenX = 0
                elif currentWord.get_width() + textBoxX + lenX + 5<= 1280:
                    screen.blit(currentWord, (lenX + textBoxX + 5, lenY + textBoxY))
                    lenX += currentWord.get_width() + 4
                else:
                    lenY += currentWord.get_height() + 4
                    lenX = 0
                    screen.blit(currentWord, (lenX + textBoxX + 5, lenY + textBoxY))
                    lenX += currentWord.get_width() + 4
                

        try:  
            self.electrons[0].draw(screen, (self.x+offSet, self.y+offSetfactor), self.zoom)
            self.electrons[1].draw(screen, (self.x-offSet, self.y-offSetfactor), self.zoom)
            self.electrons[2].draw(screen, (self.x+offSet, self.y-offSetfactor), self.zoom)
            self.electrons[3].draw(screen, (self.x-offSet, self.y+offSetfactor), self.zoom)
            self.electrons[4].draw(screen, (self.x-offSetfactor, self.y+offSet), self.zoom)
            self.electrons[5].draw(screen, (self.x-offSetfactor, self.y-offSet), self.zoom)
            self.electrons[6].draw(screen, (self.x+offSetfactor, self.y+offSet), self.zoom)
            self.electrons[7].draw(screen, (self.x+offSetfactor, self.y-offSet), self.zoom)
        except:
            pass


