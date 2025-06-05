import pygame

pygame.init()  # Inicia o jogo
window = pygame.display.set_mode((1280, 720))  # Define resolução
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    window.fill("blue")
    pygame.display.flip()  # Mostra os frames desenhados
    clock.tick(120)  # Define taxa de quadros
pygame.quit()
