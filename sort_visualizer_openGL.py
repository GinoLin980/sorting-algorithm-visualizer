import pygame
import sys; sys.dont_write_bytecode = True
import time
import numpy as np
from OpenGL.GL import *
from pygame.locals import *
from sorting_algorithms import SortingAlgorithms

available_algo = ["bubble_sort", "quick_sort"]

if len(sys.argv) != 2:
    print(f"\nUsage: python3 sort_visualizer_OpenGL.py {' or '.join(available_algo)}\n")
    sys.exit(1)

sort_algorithm = sys.argv[1].lower()

assert sort_algorithm in available_algo, f"\nThis {sort_algorithm} is not available now\nPlease choose from {','.join(available_algo)}\n"

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((1920, 1080), DOUBLEBUF | OPENGL)
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


def swap_bars(i, j, lst=ARR):
    draw_bar(i, HEIGHT, (0, 0, 0))
    draw_bar(j, HEIGHT, (0, 0, 0))
    lst[i], lst[j] = lst[j], lst[i]
    draw_bar(i, lst[i], BAR_COLOR)
    draw_bar(j, lst[j], BAR_COLOR)

def bubble_sort(lst):
        for i in range(N):
            swapped = False
            for j in range(0, N - i - 1):
                draw_bar(j, lst[j], COMPARE_COLOR)
                draw_bar(j + 1, lst[j + 1], COMPARE_COLOR)
                pygame.display.flip()

                time.sleep(0.01)
                if lst[j] > lst[j + 1]:
                    swap_bars(j, j + 1)
                    swapped = True
                draw_bar(j, HEIGHT, (0, 0 ,0))
                draw_bar(j + 1, HEIGHT, (0, 0, 0))
                pygame.display.flip()
                draw_bar(j, lst[j], BAR_COLOR)
                draw_bar(j + 1, lst[j + 1], BAR_COLOR)
                pygame.display.flip()
            if not swapped:
                break


def partition(arr, low, high):
    i = (low-1)
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i+1
            arr[i], arr[j] = arr[j], arr[i]
            glClear(GL_COLOR_BUFFER_BIT)
            for k, value in enumerate(arr):
                color = COMPARE_COLOR if k == i or k == j else BAR_COLOR
                draw_bar(k, value, color)
            pygame.display.flip()
            pygame.time.wait(0)
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1


def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi-1)
        quick_sort(arr, pi+1, high)


# Main loop
init_bar(ARR)
pygame.display.flip()
sortAlgo = SortingAlgorithms(ARR, screen, WIDTH, HEIGHT, MARGIN, BAR_COLOR, COMPARE_COLOR, (0, 0, 0), 0, True)
running = True

if sort_algorithm == "quick_sort":
        action = sortAlgo.quick_sort
        params = (0, N-1)
elif sort_algorithm == "bubble_sort":
    sortAlgo.bubble_sort
    params = None
else:
    print("Invalid sorting algorithm. Choose 'quicksort' or 'bubblesort'.")
    running = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # quick_sort(ARR, 0, N-1)
    # bubble_sort(ARR)
    # quick_sort(ARR, 0, N-1)
    action(param for param in params)

    if np.array_equal(ARR, np.sort(ARR)):
        time.sleep(3)
        break

pygame.quit()
sys.exit()
