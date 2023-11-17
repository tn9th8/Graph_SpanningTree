# constants
display_width = 800
display_height = 600
radius = 30 # bán kính của node
speed = 2 # frames per sec

queue = [0] # root of BFS

grey = (100, 100, 100)  # undiscovered node or edge
white = (255, 255, 255)  # discovered edge or node outline
yellow = (200, 200, 0)  # current node fill
red = (200,0,0) # discovered node fill
black = (0, 0, 0)  # undiscovered node fill
blue = (50,50,160) # completed node fill and completed edge
green_dark = (0, 128, 0) # number ndoe
purple = (128, 0, 128) # visited line


        # Lấy vị trí chuột # Nhận trạng thái nút chuột
        #mouse_position = pygame.mouse.get_pos() 
        #mouse_pressed = pygame.mouse.get_pressed() 
