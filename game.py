import pygame
pygame.init()
screenWidth = 400
screenHight = 400
screen = pygame.display.set_mode((screenWidth, screenHight))
pygame.display.set_caption("My First Game")
sprite = pygame.image.load("birds.png").convert()
done = False
is_blue = True
x = 30
y = 30

while not done:
	for event in pygame.event.get():
 		if event.type == pygame.QUIT:
 			done = True
 		if event.type == pygame.KEYDOWN and event.type == pygame.K_SPACE:
 			is_blue = not is_blue



 		pressed = pygame.key.get_pressed()
 		if pressed[pygame.K_UP]:
 			y -= 3
 		if pressed[pygame.K_DOWN]:
 			y += 3
 		if pressed[pygame.K_LEFT]:
 			x -= 3
 		if pressed[pygame.K_RIGHT]:
 			x += 3
 		
 		if is_blue:
 			color = (0,128,255)
 		else : color = (255,100,0)
 		



 		screen.fill((255,255,255))
 		#pygame.draw.rect(screen,color,pygame.Rect(x,y,60,60))
 		screen.blit(sprite,(30,30,60,60))
 		pygame.display.flip()
