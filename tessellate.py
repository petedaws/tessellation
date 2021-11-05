import pygame, sys
from pygame.locals import *
import random

WHITE=(255,255,255)
BLACK=(0,0,0)

TICK_RATE = 20
SCREEN_HEIGHT = 800
SCREEN_WIDTH = 400
POINT_SIZE = 2

MAX_RAND = 20

shape_verticies = [(int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2))]

def get_random_point(ref_point):
    return (ref_point[0]+random.randint(-MAX_RAND,MAX_RAND),ref_point[1]+random.randint(-MAX_RAND,MAX_RAND))

def draw_verticies(display,input_vector):
    for i,point in enumerate(input_vector):
        pygame.draw.circle(display,BLACK,point,POINT_SIZE)
        pygame.draw.line(display,BLACK,point,input_vector[i-1])
    
def main():
    pygame.init()
    
    clock = pygame.time.Clock()

    DISPLAY=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
    DISPLAY.fill(WHITE)

    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        DISPLAY.fill(WHITE)
        shape_verticies.append(get_random_point(shape_verticies[-1]))
        draw_verticies(DISPLAY,shape_verticies)
        pygame.display.update()
        clock.tick(TICK_RATE)

main()