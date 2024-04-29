import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def init(screen):
    # Initialize user interface elements
    button_rect = pygame.Rect(50, 50, 100, 50)
    pygame.draw.rect(screen, WHITE, button_rect)

def update():
    # Update user interface based on user input
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()
    if mouse_click[0]:
        print("Left mouse button clicked at", mouse_pos)