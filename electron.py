#Bandar Al Aish

import pygame

class Electron():
    def __init__(self, type):
        self.type = type
        self.xOffset = 0
        self.yOffset = 0

    def update(self, mode):
        if self.type == "b":
            if mode == "ionicBonding":
                self.xOffset += 5.92
                self.yOffset -= 1.4
                if self.xOffset > 296:
                    self.xOffset, self.yOffset = 0, 0


    def draw(self, screen, position, zoom):
        if self.type == "r":
            pygame.draw.circle(screen, (255,0,0), (position), 2*zoom*0.25)
        elif self.type == "b":
            pygame.draw.circle(screen, (0,0,255), (position[0]+self.xOffset, position[1]+self.yOffset), 2*zoom*0.25)
