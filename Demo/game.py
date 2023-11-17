import pygame
import sys
from graph_data import graph
from constants import *

# graph element parts:
#  [0] : xy 
#  [1] : adjacent node indexes
#  [2] : node edge color 
#  [3] : node fill color

# hàm run
def run(choices):
    global screen, edges, clock, font, font2

    # chuẩn hóa graph: thêm 2 màu sắc cho node
    for element in graph:
        element.extend([grey, black])
    # chuẩn bị line
    build_edges()

    # khởi tạo game
    pygame.init()
    pygame.font.init()
    pygame.font.get_init()
    pygame.display.set_caption('Spanning Tree Finding ALgorithm - BFS')
    
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((display_width, display_height))
    font = pygame.font.SysFont('freesanbold.ttf', 30)
    
    # vẽ graph
    draw_graph()
    
    update()
    pygame.time.delay(3000) 

    # game loop: let's get stated
    while True: 
        # catch event: thoát game
        for event in pygame.event.get(): 
            if event.type == pygame.QUIT: 
                pygame.quit() 
                sys.exit() 
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print('auto run')
                    do_BFS_auto()
                if event.key == pygame.K_o:
                    print('one step')
                    do_BFS_one_step()

def do_BFS_auto():
        # run BFS algorith loop
        while len(queue) > 0:
            n1 = queue.pop(0) # current node
            current = graph[n1] 
            current[2] = white
            current[3] = green_dark
            
            for n2 in current[1]: # adjacents
                if graph[n2][3] == black and n2 not in queue:  # haven't visited => leaf node
                    queue.append(n2)
                    graph[n2][2] = white
                    graph[n2][3] = red
                    edges[edge_id(n1,n2)][1] = yellow 
        
                    update()
        
            current[3] = blue # visited 
            update()

def do_BFS_one_step():
        # run BFS algorith loop
        while len(queue) > 0:
            n1 = queue.pop(0) # current node
            current = graph[n1] 
            current[2] = white
            current[3] = green_dark
            
            for n2 in current[1]: # adjacents
                if graph[n2][3] == black and n2 not in queue:  # haven't visited => leaf node
                    queue.append(n2)
                    graph[n2][2] = white
                    graph[n2][3] = red
                    edges[edge_id(n1,n2)][1] = yellow 
        
                    update()
            
            loop = True
            while loop:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT: 
                        pygame.quit() 
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_SPACE:
                            loop = False

            current[3] = blue # visited 
            update()
            
#
def edge_id(n1, n2): 
    return tuple(sorted((n1, n2)))  

def build_edges():
    global edges
    edges = {} # edgeid: [(n1,n2), color]
    for n1, (_, adjacents, _, _) in enumerate(graph):
        for n2 in adjacents:
            eid = edge_id(n1, n2)
            if eid not in edges:
                edges[eid] = [(n1, n2), grey]

def draw_graph():
    global graph, screen, edges

    screen.fill((0, 0, 0,))

    for e in edges.values(): # draw edges
        (n1, n2), color = e
        pygame.draw.line(screen, color, graph[n1][0], graph[n2][0], 3)

    for i, (xy, _, lcolor, fcolor) in enumerate(graph): # draw nodes
        #print(i, xy)
        circle_fill(i, xy, yellow, lcolor, fcolor, 25, 2)

def update():
    global clock
    draw_graph()
    pygame.display.update()
    clock.tick(speed)

def circle_fill(i, xy, num_color, line_color, fill_color, radius, thickness):
    global screen
    pygame.draw.circle(screen, line_color, xy, radius)
    pygame.draw.circle(screen, fill_color, xy, radius - thickness)

    # Vẽ số nguyên i tại vị trí xy với màu num_color
    text = font.render(str(i), True, num_color)
    text_rect = text.get_rect(center=xy)
    screen.blit(text, text_rect)
