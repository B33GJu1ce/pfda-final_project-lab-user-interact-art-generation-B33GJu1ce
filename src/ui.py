import pygame
import random

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Function to change background color to a random color
def change_background_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

# Initialize UI elements
def init(screen):
    pass  # No need to initialize any UI elements in this version
# Function to display instructions
def display_instructions():
    print("Press B to change background color")
    print("Press O to create a circle")
    print("Press T to create a triangle")
    print("Press R to create a square")
    print("Press C to change color of shape")
    print("Press S to change size of shape")
    print("Press Q to quit")