import pygame, sys
from pygame.locals import *
import random

WHITE=(255,255,255)
BLACK=(0,0,0)

TICK_RATE = 1
SCREEN_HEIGHT = 400
SCREEN_WIDTH = 400
POINT_SIZE = 2

MAX_RAND = 60
VERTEX_LENGTH = 10

def get_random_vertex_list():
    ref_point = (int(SCREEN_WIDTH/2),int(SCREEN_HEIGHT/2))
    shape_verticies = [ref_point]
    for i in range(VERTEX_LENGTH):
        shape_verticies.append(get_random_point(ref_point))
    return shape_verticies
        
def print_points(display,input_vector):
    font_size=15
    font = pygame.font.SysFont('Arial', font_size)
    for i,point in enumerate(input_vector):
        display.blit(font.render(f'({point[0]}),({point[1]})', True, (0,0,0)), (0, font_size*i))

def get_left_most_point(input_vector):
    for point in input_vector:
        if point[0]:
            pass

def get_random_point(ref_point):
    return (ref_point[0]+random.randint(-MAX_RAND,MAX_RAND),ref_point[1]+random.randint(-MAX_RAND,MAX_RAND))

def draw_verticies(display,input_vector):
    for i,point in enumerate(input_vector):
        pygame.draw.circle(display,BLACK,point,POINT_SIZE)
        
def draw_lines(display,input_vector):
    for i,point in enumerate(input_vector):
        pygame.draw.line(display,BLACK,point,input_vector[i-1])
    
def main():
    pygame.init()
    
    clock = pygame.time.Clock()

    DISPLAY=pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT),0,32)
    DISPLAY.fill(WHITE)

    vertex_list = []
    
    do_draw_lines = False
    
    while True:
        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    vertex_list = get_random_vertex_list()
                if event.key == pygame.K_w:
                    if do_draw_lines:
                        do_draw_lines = False
                    else:
                        do_draw_lines = True
                    
        DISPLAY.fill(WHITE)
        
        draw_verticies(DISPLAY,vertex_list)
        if do_draw_lines:
            draw_lines(DISPLAY,vertex_list)
        print_points(DISPLAY,vertex_list)
        pygame.display.update()
        clock.tick(TICK_RATE)

main()