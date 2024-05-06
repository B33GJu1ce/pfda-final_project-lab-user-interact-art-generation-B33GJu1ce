import pygame

def draw(screen, circle_color, circle_radius, circle_shape):
    screen.fill((0, 0, 0))  # Clear the screen

    # Draw the circle
    if circle_shape == "circle":
        pygame.draw.circle(screen, circle_color, (400, 300), circle_radius)
    elif circle_shape == "square":
        square_size = circle_radius * 2
        square_rect = pygame.Rect(400 - circle_radius, 300 - circle_radius, square_size, square_size)
        pygame.draw.rect(screen, circle_color, square_rect)
    elif circle_shape == "rectangle":
        rect_width = circle_radius * 2
        rect_height = circle_radius * 0.75  # Adjust the aspect ratio as needed
        rect_rect = pygame.Rect(400 - circle_radius, 300 - circle_radius, rect_width, rect_height)
        pygame.draw.rect(screen, circle_color, rect_rect)
    elif circle_shape == "triangle":
        # Define triangle vertices
        top_point = (400, 300 - circle_radius)
        left_point = (400 - int(circle_radius * 0.87), 300 + int(circle_radius * 0.5))
        right_point = (400 + int(circle_radius * 0.87), 300 + int(circle_radius * 0.5))
        # Draw the triangle
        pygame.draw.polygon(screen, circle_color, [top_point, left_point, right_point])

    pygame.display.flip()