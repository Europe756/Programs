from time import sleep
import random
times=0.01,0.02,0.03,0.04,0.05,0.06,0.07,0.08,0.09,0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9,1
times2=1,2,3
for i in range (100):
    delay = random.choice(times)
    sleep (delay)
    i=i+1
    print(i,"%")
print("Finished!")
sleep (5)
for l in range (10):
    print("")
print("Lol that was it!")
for m in range (10):
    print("")
    sleep (1)
print("Nothing else is coming!")
for g in range (15):
    print("")
    sleep (1)
print("Ok fine, you win")
for g in range (10):
    print("Debug starting")
    sleep(0.2)
for g in range (100):
    delay = random.choice(times2)
    sleep (delay)
    i=i+1
    print("FastDebug",g,"%") 
print("Debug complete, no bugs found")
flag = True
while flag:
    value = input("Would you like to play a game?(Please use ONLY uppercase letters):")
    if value == "NO":
        flag = False
        print("This is not a game!")
    elif value == "YES":
        print("The game will start shortly!")
        flag = False
    else:
        print("Please enter a valid answer")
import pygame
from pygame.locals import *
import colorama
from colorama import Fore, Style
pygame.init()
width = pygame.display.Info().current_w
height = pygame.display.Info().current_h
screen = pygame.display.set_mode((width, height))
difference = pygame.image.load("Picture.png")
difference = pygame.transform.scale(difference, (width, height))
screen.blit(difference, (0, 0))
pygame.mixer.music.load('Sound.mp3')
pygame.mixer.music.play()
screen.blit(difference, (0, 0))
pygame.display.update()
sleep(9.9366990091081)
pygame.mixer.music.stop()
pygame.quit()
for i in range (30):
    print(Fore.RED + "Lol get rickrolled")

































