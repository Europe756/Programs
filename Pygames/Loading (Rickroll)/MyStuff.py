import pygame
from pygame.locals import *
import colorama
from colorama import Fore, Style
from time import sleep
for i in range(100):
    i = i+1
    print("Loading,",i ,"%")
    sleep(0.2)
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
for i in range (100):
    print(Fore.RED + "Lol get rickrolled")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
