import pygame

pygame.init()

screen = pygame.display.set_mode((800,600))
screen.fill((150,150,150))
pygame.display.set_caption('shooting/place')

imgpl = pygame.image.load('./assets/player.png')
imgbl = pygame.image.load('./assets/bullet.png')
Xpl = 380
Ypl = 500
Xbl = 400
Ybl = 300

running = True
while running:
    screen.blit(imgpl,(Xpl,Ypl))
    screen.blit(imgbl,(Xbl,Ybl))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.update()