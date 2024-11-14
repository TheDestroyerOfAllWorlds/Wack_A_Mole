import pygame, random

pygame.init()

pygame.display.set_caption("Whack-A-Mole!")
screen = pygame.display.set_mode((640, 512))
mole_image = pygame.image.load("mole.png")
mole_rect = mole_image.get_rect(topleft=(3,3))

running = True

def new_board():
    screen.fill((0, 150, 255))
    screen.blit(mole_image, mole_rect)
    for i in range(0, 640, 32):
        pygame.draw.line(screen, (0, 0, 0), (i, 0), (i, 512))
    for j in range(0, 512, 32):
        pygame.draw.line(screen, (0, 0, 0), (0, j), (640, j))

def move_mole():
    mole_rect.topleft = random.randint(0, 19) * 32, random.randint(0, 15) * 32

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if mole_rect.collidepoint(event.pos):
                move_mole()
    new_board()
    pygame.display.flip()

pygame.quit()
