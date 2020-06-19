import pygame
from pygame import display, event, image, transform
from animal import Animal
import game_config as gc
from time import sleep
pygame.init()

display.set_caption('Match Game')
screen = display.set_mode((512,512))
matched_image = image.load('other_assets/matched.png')
# image = transform.scale(matched, (gc.IMAGE_SIZE-2*gc.MARGIN, gc.IMAGE_SIZE-2*gc.MARGIN))
# screen.blit(image, (0*gc.IMAGE_SIZE+gc.MARGIN, 1*gc.IMAGE_SIZE+gc.MARGIN))
# display.flip()

running = True
white = (255, 255, 255) 
green = (0, 255, 0) 
blue = (0, 0, 128) 
red = (255,0,0)
  

tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]

# show images at the starting
for i, tile in enumerate(tiles):
	image_i = tile.box
	screen.blit(image_i, (tile.col*gc.IMAGE_SIZE+gc.MARGIN, tile.row*gc.IMAGE_SIZE+gc.MARGIN))
	display.flip()
	sleep(0.2)# 
sleep(0.5)

for tile in tiles:
	screen.blit(tile.image, (tile.col*gc.IMAGE_SIZE+gc.MARGIN, tile.row*gc.IMAGE_SIZE+gc.MARGIN))
display.flip()
sleep(0.5)

def get_score(score):
	loop = True
	while(loop):
		font = pygame.font.Font('freesansbold.ttf', 32)
		screen.fill(white)
		text = font.render(f'Score:{score}', True, green, blue)
		textRect = text.get_rect()
		textRect.center = (256 , 156)
		screen.blit(text, textRect)

		close = font.render('Close', True, red, blue)
		button_quit = close.get_rect()
		button_quit.center = (256, 256)
		screen.blit(close, button_quit)
		mouse = pygame.mouse.get_pos()
		if mouse[0]>=211 and mouse[0]<=300 and mouse[1]>=240 and mouse[1]<=272:
			close = font.render('Close', True, blue, red)
			screen.blit(close, button_quit)
		# display.flip()
		display.flip()
		current_events = event.get()
		for e in current_events:
			# mouse = pygame
			# if mouse[0]>=211 and mouse[0]<=300 and mouse[1]>=240 and mouse[1]<=272:
			# close = font.render('Close', True, red, blue)
			# screen.blit(close, button_quit)
			# display.flip()
			if e.type == pygame.MOUSEBUTTONDOWN:
				mouse_x, mouse_y = pygame.mouse.get_pos()
				if mouse_x>=211 and mouse_x<=300 and mouse_y>=240 and mouse_y<=272:
					loop = False
					break



		




# count = 0
def find_index(mouse_x, mouse_y):
	row = mouse_y // gc.IMAGE_SIZE
	col = mouse_x // gc.IMAGE_SIZE
	# print(f'row: {row}, col: {col}')
	index = row*gc.MARGIN + col
	# print(f'index: {index}')
	return index

current_images = []
current_names = []
score = 0
# match = False
matched = 0
# check = 0
while(running):
    current_events = event.get()
    for e in current_events:
        if e.type == pygame.QUIT:
            running = False
        if e.type == pygame.KEYDOWN:
        	if e.key == pygame.K_ESCAPE:
        		running = False
        		get_score(score)

        if matched == 8:
        	running = False
        	get_score(score)

        if e.type == pygame.MOUSEBUTTONDOWN:
        	mouse_x, mouse_y = pygame.mouse.get_pos()
        	index = find_index(mouse_x, mouse_y)

        	if index not in current_images:
        		current_images.append(index)
        		current_names.append(tiles[index].name)
        		score += 1
        	# print(tiles[index].name)
        	print(current_names)
        	# if len(current_names)>=2:
        	# 	if current_names[-1]==current_names[-2]:
        	# 		for i in range(100):
	        # 			screen.blit(matched, (0, 0))
	        # 			display.flip()
        	# 		match = True
        	# 		current_images = []
        	# 		current_names = []


        	if len(current_images) > 2 :#and not match:
        		current_images = current_images[1:]
        		current_names = current_names[1:]

    screen.fill((255,255,255))

    for i, tile in enumerate(tiles):
    	image_i = tile.image if i in current_images else tile.box
    	if not tile.skip:
    		screen.blit(image_i, (tile.col*gc.IMAGE_SIZE+gc.MARGIN, tile.row*gc.IMAGE_SIZE+gc.MARGIN))
    display.flip()
    if len(current_images)==2:
    	idx1, idx2 = current_images
    	if tiles[idx1].name == tiles[idx2].name:
    		tiles[idx1].skip = True
    		tiles[idx2].skip = True
    		current_images = []
    		current_names = [] 
    		sleep(0.5)
    		matched += 1
    		screen.blit(matched_image, (0, 0))
    		display.flip()
    		sleep(0.5)	



print('Goodbye!')