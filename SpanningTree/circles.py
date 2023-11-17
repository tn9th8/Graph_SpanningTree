import pygame
from graph_data import graph

# constants 
display_width = 800
display_height = 600
radius = 30 # bán kính node

def run():
    pygame.init()

    screen = pygame.display.set_mode((display_width, display_height))
    clock = pygame.time.Clock() # để đồng bộ, thời gian LT và hoạt động LT

    screen.fill((0,0,0)) # background is black

    # loop to draw cicle at each node
    # underscore _ is to ignore the second element
    for xy, _ in graph:
        pygame.draw.circle(screen, (255,255,200), xy, radius) # yellow cicles
        pygame.draw.circle(screen, (0,150,150), xy, radius-4) # green cicles

    pygame.display.update() # copy screen buffer to display

# wait for stop, for repl.it
    while 1:  
        clock.tick(60) 
# DONT DO THIS LOOP NORMALY!
# you usually will check for user events 
# like window close with code like this

# for event in pygame.event.get():
# 	if event.type == pygame.QUIT:
# 		sys.exit()