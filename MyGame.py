import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('My2D_Game')#To change the title name 
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf',50)# it take (type , size)

#elements surfaces
sky_surface = pygame.image.load('graphiks/Sky.png').convert()
ground_surface = pygame.image.load('graphiks/ground.png').convert()
text_surface = test_font.render('My First game',False,'Black')# it take (text informtion,anti-aliase,color)

snail_surface = pygame.image.load('graphiks/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(bottomright = (600,300))


player_surf = pygame.image.load('graphiks/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            #adding mouse events
        #if event.type == pygame.MOUSEMOTION:
            #if player_rect.collidepoint(event.pos): print('collision')

    #draw all our elements
    screen.blit(sky_surface,(0,0)) #it taik (name,postion)
    screen.blit(ground_surface,(0,300))
    screen.blit(text_surface,(300,50))

    snail_rect.x -= 5
    if snail_rect.right <= 0: snail_rect.left = 800
    screen.blit(snail_surface,snail_rect)
    screen.blit(player_surf,player_rect)

    #if event.type == pygame.MOUSEMOTION:
    #  if player_rect.collidepoint(event.pos): print('collision')

    mouse_pos = pygame.mouse.get_pos()
    if player_rect.collidepoint(mouse_pos):
        print(pygame.mouse.get_pressed())

    #update everything 
    pygame.display.update() 
    clock.tick(60)#it talls the while loop shoud not run faster than 60