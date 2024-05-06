import pygame
import random

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define global variables for UI elements
color_button_rect = pygame.Rect(50, 50, 100, 50)
size_slider_rect = pygame.Rect(50, 150, 200, 20)

# Initialize mouse_pressed variable
mouse_pressed = False

# Initialize UI elements
def init(screen):
    # Draw color button
    pygame.draw.rect(screen, WHITE, color_button_rect)

    # Draw size slider
    pygame.draw.rect(screen, WHITE, size_slider_rect)

# Update UI based on user input
def update():
    global mouse_pressed, color_button_rect, size_slider_rect

    # Check for mouse clicks
    mouse_pos = pygame.mouse.get_pos()
    mouse_click = pygame.mouse.get_pressed()

    # Check for mouse button state transitions
    if not mouse_pressed and mouse_click[0]:
        mouse_pressed = True
        # Check if mouse click is on the color button
        if color_button_rect.collidepoint(mouse_pos):
            # Change the color of the circle to a random color
            new_color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            print("Color button clicked!")
            return new_color
        if size_slider_rect.collidepoint(mouse_pos):
            print("Size slider clicked!")

    elif mouse_pressed and not mouse_click[0]:
        mouse_pressed = False