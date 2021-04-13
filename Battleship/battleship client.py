import os
import pygame
import socket
import threading
from GRID import Grid

os.environ['SDL_VIDEO_WINDOW_POS'] = '200,100'

surface = pygame.display.set_mode((1000, 1000))
while True: