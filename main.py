#Bandar Al Aish

import pygame
from atom import *

pygame.init()  
screen = pygame.display.set_mode((1280,720))  
run = True

fpsClock = pygame.time.Clock()

salt = pygame.image.load("salt.png")

mode = "chemistryMacro"

zoomCount = 0

atoms = []
for i in range(100):
    if((i%13)%2 == 1):
        atoms.append(Atom("Cl-", (i%13)*120, (i//13)*120))
    else:
        atoms.append(Atom("Na+", (i%13)*120, (i//13)*120))



while run:
    if zoomCount > 2 and zoomCount != 100: #100 = ionic bonding mode
        mode = "chemistryMicro"
    elif zoomCount <= 2 and zoomCount != 100: 
        mode = "chemistryMacro"

    if zoomCount > 3 and zoomCount != 100:
        zoomCount = 3


    screen.fill((255,255,175))

    if mode == "chemistryMacro":
        screen.blit(salt,(640-salt.get_width()/2,360-salt.get_height()/2)) 
    
    if mode == "chemistryMicro" or mode == "ionicBonding":
        for atom in atoms:
            atom.update(zoomCount, mode)
            atom.draw(screen, mode)

    if mode == "ionicBonding":
        pygame.draw.rect(screen, (255,0,0), (10, 10, 70, 70)) #Back button

    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_presses = pygame.mouse.get_pressed()
            if mouse_presses[0]:
                if mode == "chemistryMicro":
                    mode = "ionicBonding"
                    zoomCount = 100
                    atoms = [Atom("Cl", 750, 360), Atom("Na", 500, 370)]
                if mode == "ionicBonding":
                    x, y = pygame.mouse.get_pos()
                    if x > 10 and x < 80 and y > 10 and y < 80:
                        mode = "chemistryMicro"
                        zoomCount = 3
                        atoms = []
                        for i in range(100):
                            if((i%13)%2 == 1):
                                atoms.append(Atom("Cl-", (i%13)*120, (i//13)*120))
                            else:
                                atoms.append(Atom("Na+", (i%13)*120, (i//13)*120))


            if mode != "ionicBonding":
                if event.button == 5: #Scroll down
                    zoomCount -= 1
                    if mode == "chemistryMacro":
                        salt = pygame.transform.scale(salt, (int(salt.get_width()*0.5), int(salt.get_height()*0.5)))
                elif event.button == 4: #Scroll up
                    zoomCount += 1
                    if mode == "chemistryMacro":
                        salt = pygame.transform.scale(salt, (int(salt.get_width()/0.5), int(salt.get_height()/0.5)))


        if event.type == pygame.QUIT:  
            run = False

    fpsClock.tick(60)
    pygame.display.update()


pygame.quit()
