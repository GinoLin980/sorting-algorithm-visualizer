import time
import sys; sys.dont_write_bytecode = True
import numpy
import pygame
from OpenGL.GL import *


class SortingAlgorithms:
    def __init__(self, arr: numpy.ndarray, screen: pygame.Surface, width: int, height: int, margin: float,
                 bar_color: tuple[float], compare_color: tuple[float], bg_color: tuple[float], wait_time: float):
        self.quit = False
        self.arr = arr
        self.screen = screen
        self.width = width
        self.height = height
        self.margin = margin
        self.bar_color = bar_color
        self.compare_color = compare_color
        self.bg_color = bg_color
        self.wait_time = wait_time
        self.n = len(self.arr)
        self.bar_width = self.width / self.n
        self.height_unit = self.height / max(self.arr)

    def draw_bar(self, index: int, value: int, color: tuple[float]) -> None:
        """Use OpenGL to draw rectangles."""
        glColor3f(*color)
        glBegin(GL_QUADS)
        glVertex2f(self.bar_width * index, 0)
        glVertex2f(self.bar_width * (index + 1) - self.margin, 0)
        glVertex2f(self.bar_width * (index + 1) - self.margin, self.height_unit * value)
        glVertex2f(self.bar_width * index, self.height_unit * value)
        glEnd()

    def swap_bars(self, i: int, j: int) -> None:
        """Draw the value of each other bar."""
        self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
        self.draw_bar(i, self.arr[i], self.bar_color)
        self.draw_bar(j, self.arr[j], self.bar_color)

    def update_display(self) -> None:
        glClear(GL_COLOR_BUFFER_BIT)
        for k, value in enumerate(self.arr):
            self.draw_bar(k, value, self.bar_color)
        pygame.display.flip() if not self.quit else pygame.quit()
        # time.sleep(self.wait_time)

    def check_quit(self) -> None:
        """Check quit state in the for loop"""
        try:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.quit = True
                    pygame.quit()
        except Exception as e:
            pygame.quit()

    def bubble_sort(self, *args):
        if not self.quit:
            n = len(self.arr)
            for i in range(n):
                self.check_quit()
                if self.quit:
                    return
                swapped = False
                for j in range(0, n - i - 1):
                    self.draw_bar(j, self.arr[j], self.compare_color)
                    self.draw_bar(j + 1, self.arr[j + 1], self.compare_color)
                    self.check_quit()
                    if self.quit:
                        return
                    pygame.display.flip() if not self.quit else pygame.quit()
                    time.sleep(self.wait_time)

                    if self.arr[j] > self.arr[j + 1]:
                        self.swap_bars(j, j + 1)
                        swapped = True

                    self.draw_bar(j, self.arr[j], self.bar_color)
                    self.draw_bar(j + 1, self.arr[j + 1], self.bar_color)
                    self.update_display()

                if not swapped:
                    break

    def partition(self, low: int, high: int) -> int:
        i = low - 1
        pivot = self.arr[high]

        for j in range(low, high):
            self.check_quit()
            if self.arr[j] <= pivot:
                i = i + 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                glClear(GL_COLOR_BUFFER_BIT)
                for k, value in enumerate(self.arr):
                    color = self.compare_color if k == i or k == j else self.bar_color
                    self.draw_bar(k, value, color)
                self.check_quit()
                pygame.display.flip() if not self.quit else pygame.quit()
                pygame.time.wait(0)
        self.arr[i + 1], self.arr[high] = self.arr[high], self.arr[i + 1]
        return i + 1

    def quick_sort(self, low: int, high: int):
        self.check_quit()
        if low < high and not self.quit:
            pi = self.partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)
