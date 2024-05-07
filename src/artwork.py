import pygame
import random

class Circle:
    def __init__(self):
        self.color = (0, 0, 255)  # Initial color is blue
        self.radius = 50  # Initial radius
        self.center = (400, 300)  # Center of the screen

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.center, self.radius)

    def change_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def change_size(self):
        self.radius = random.randint(10, 100)  # Random radius between 10 and 100

class Square:
    def __init__(self):
        self.color = (255, 0, 0)  # Initial color is red
        self.size = 100  # Initial size (width and height)
        self.rect = pygame.Rect(350, 250, self.size, self.size)  # Initial position

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def change_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def change_size(self):
        self.size = random.randint(50, 150)  # Random size between 50 and 150
        self.rect = pygame.Rect(400 - self.size // 2, 300 - self.size // 2, self.size, self.size)

class Triangle:
    def __init__(self):
        self.color = (0, 255, 0)  # Initial color is green
        self.size = 100  # Initial size (base and height)
        self.points = [(400, 200), (350, 300), (450, 300)]  # Initial points

    def draw(self, screen):
        pygame.draw.polygon(screen, self.color, self.points)

    def change_color(self):
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def change_size(self):
        self.size = random.randint(50, 150)
        # Recalculate the points based on the new size
        self.points = [(400, 200), (400 - self.size // 2, 200 + self.size), (400 + self.size // 2, 200 + self.size)]