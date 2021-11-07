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
    
def get_m_c(line):
    x0,y0 = line[0]
    x1,y1 = line[1]
    m = (y1-y0)/(x1-x0)
    c = y0 - m*x0
    return m, c
    
def get_intersect(line0,line1):
    # gets the intersection of two lines
    m0,c0 = get_m_c(line0)
    m1,c1 = get_m_c(line1)
    
    x = (c1-c0)/(m0-m1)
    y = m0*x+c0
    return x,y
    
def check_float_between_two_numbers(check,num0,num1):
    a = num0 <= check <= num1
    b = num1 <= check <= num0
    return a or b

def check_intersect(line0,line1):
    # checks if the intersection point lies on one of the lines
    m0,c0 = get_m_c(line0)
    x00,y00 = line0[0]
    x01,y01 = line0[1]
    x10,y10 = line1[0]
    x11,y11 = line1[1]
    xi,yi = get_intersect(line0,line1)
    a = check_float_between_two_numbers(xi,x00,x01)
    b = check_float_between_two_numbers(yi,y00,y01)
    c = check_float_between_two_numbers(xi,x10,x11)
    d = check_float_between_two_numbers(yi,y10,y11)    
    return a and b and c and d
        
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