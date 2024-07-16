import pygame
import sys; sys.dont_write_bytecode = True
import random
from sorting_algorithms import SortingAlgorithms

def reso(resolution, direction): # return 16:9
    if direction == "p":
        return resolution, resolution*16/9
    if direction == "l":
        return resolution*16/9, resolution

# Initialize Pygame
pygame.init()

# Create a shuffled list of integers
lst = list(range(1, 401))  # Increased to 400 elements
assert len(lst) <= 400, "Without OpenGL, 400 element is bottleneck."
random.shuffle(lst)

# Constants
WIDTH, HEIGHT = reso(1080, "l")
print(WIDTH, HEIGHT)
BG_COLOR = (0, 0, 0)
BAR_COLOR = (255, 154, 138)
COMPARE_COLOR = (255, 0, 255)
MARGIN = 1
WAIT_TIME = 0.001



# Create Pygame window
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Sorting Algorithm Visualization")

def draw_initial_list(lst):
    screen.fill(BG_COLOR)
    n = len(lst)
    width = WIDTH / n
    height_unit = HEIGHT / max(lst)
    for i, value in enumerate(lst):
        pygame.draw.rect(screen, BAR_COLOR, (i * width, HEIGHT - value * height_unit, width - MARGIN, value * height_unit))
        # print(f"INIT {i/len(lst)*100:.2f}%")
        
        # Handle events to prevent the window from becoming unresponsive
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
        pygame.display.update()  # Ensure this is called once after all drawing is done

# Main loop
running = True
sorted = False

draw_initial_list(lst)
pygame.display.update()

sorting_algo = SortingAlgorithms(lst, screen, WIDTH, HEIGHT, MARGIN, BAR_COLOR, COMPARE_COLOR, BG_COLOR, WAIT_TIME)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if not sorted:
    #     sorting_algo.quick_sort(0, len(lst) - 1)  # Change to sorting_algo.bubble_sort() to use Bubble Sort
    #     sorted = True
    sorting_algo.bubble_sort()
    pygame.display.update()

pygame.quit()