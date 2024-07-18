import pygame
import sys; sys.dont_write_bytecode = True
import time
import numpy as np
from OpenGL.GL import *
from pygame.locals import *
from sorting_algorithms import SortingAlgorithms

def reso(resolution, direction): # return 16:9
    if direction == "p":
        return resolution, resolution*16/9
    if direction == "l":
        return resolution*16/9, resolution

available_algo = ["bubble_sort", "quick_sort"]

if len(sys.argv) != 2:
    print(f"\nUsage: python3 sort_visualizer_OpenGL.py {' or '.join(available_algo)}\n")
    sys.exit(1)

sort_algorithm = sys.argv[1].lower()

assert sort_algorithm in available_algo, f"\nThis {sort_algorithm} is not available now\nPlease choose from {','.join(available_algo)}\n"

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((reso(1080, "l")), DOUBLEBUF | OPENGL)
pygame.display.set_caption('Pygame OpenGL Rectangle')

# Constants
BAR_COLOR = (1, 0.603, 0.541)
COMPARE_COLOR = (1, 0, 1)
WIDTH = screen.get_width()
HEIGHT = screen.get_height()
ARR = np.arange(1, 512 + 1)
np.random.shuffle(ARR)
N = len(ARR)
BAR_WIDTH = WIDTH / N
HEIGHT_UNIT = HEIGHT / max(ARR)
MARGIN = 100 / N


# OpenGL settings
glClearColor(0.0, 0.0, 0.0, 1.0)
glClear(GL_COLOR_BUFFER_BIT)
glMatrixMode(GL_PROJECTION)
glLoadIdentity()
glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
glMatrixMode(GL_MODELVIEW)
glLoadIdentity()


def draw_bar(index: int, value: float | int, color: tuple[float]) -> None: # 左下 右下 右上 左上

    r, g, b = (i for i in color)
    glColor3f(r, g, b)
    glBegin(GL_QUADS)
    glVertex2f(BAR_WIDTH * index, 0)
    glVertex2f(BAR_WIDTH * (index+1) - MARGIN, 0)
    glVertex2f(BAR_WIDTH * (index+1) - MARGIN, HEIGHT_UNIT * value)
    glVertex2f(BAR_WIDTH * index, HEIGHT_UNIT * value)
    glEnd()

# GO FIX THE BUBBLE SORT DISPLAY ISSUE


def init_bar(arr):
    for i, value in enumerate(arr):
        draw_bar(i, value, BAR_COLOR)

# Main loop
init_bar(ARR)
pygame.display.flip()
sorting_algo = SortingAlgorithms(ARR, screen, WIDTH, HEIGHT, MARGIN, BAR_COLOR, COMPARE_COLOR, (0, 0, 0), 0.005, True)
running = True

if sort_algorithm == "quick_sort":
    action = sorting_algo.quick_sort
    params = (0, N-1)
elif sort_algorithm == "bubble_sort":
    action = sorting_algo.bubble_sort
    params = (None, None)
else:
    print("Invalid sorting algorithm. Choose 'quicksort' or 'bubblesort'.")
    running = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    action(*params)

    if np.array_equal(ARR, np.sort(ARR)):
        time.sleep(3)
        break

pygame.quit()
sys.exit()
