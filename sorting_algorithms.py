import time
import sys; sys.dont_write_bytecode = True
import pygame
from OpenGL.GL import *

class SortingAlgorithms:
    def __init__(self, lst, screen, width, height, margin, bar_color, compare_color, bg_color, wait_time, USE_GL=False):
        self.lst = lst
        self.screen = screen
        self.width = width
        self.height = height
        self.margin = margin
        self.bar_color = bar_color
        self.compare_color = compare_color
        self.bg_color = bg_color
        self.wait_time = wait_time
        self.n = len(self.lst)
        self.bar_width = self.width / self.n
        self.height_unit = self.height / max(self.lst)
        self.USE_GL = USE_GL
        self.draw = self.draw_bar_GL if self.USE_GL else self.draw_bar

    def draw_bar(self, index, value, color):
        rect = pygame.Rect(index * self.bar_width, self.height - value * self.height_unit, self.bar_width - self.margin, value * self.height_unit)
        pygame.draw.rect(self.screen, color, rect)
        pygame.display.update(rect)

    def draw_bar_GL(self, index, value, color):
        r, g, b = color
        glColor3f(r, g, b)
        glBegin(GL_QUADS)
        glVertex2f(self.bar_width * index, 0)
        glVertex2f(self.bar_width * (index+1) - self.margin, 0)
        glVertex2f(self.bar_width * (index+1) - self.margin, self.height_unit * value)
        glVertex2f(self.bar_width * index, self.height_unit * value)
        glEnd()

    def swap_bars(self, i, j):
        self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
        self.draw(i, self.lst[i], self.bar_color)
        self.draw(j, self.lst[j], self.bar_color)

    def update_display(self):
        if self.USE_GL:
            glClear(GL_COLOR_BUFFER_BIT)
            for k, value in enumerate(self.lst):
                self.draw(k, value, self.bar_color)
            pygame.display.flip()
            # time.sleep(self.wait_time)
        else:
            pygame.display.update()

    def bubble_sort(self, *args):
        n = len(self.lst)
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                self.draw(j, self.lst[j], self.compare_color)
                self.draw(j + 1, self.lst[j + 1], self.compare_color)
                pygame.display.flip()
                time.sleep(self.wait_time)

                if self.lst[j] > self.lst[j + 1]:
                    self.swap_bars(j, j + 1)
                    swapped = True

                self.draw(j, self.lst[j], self.bar_color)
                self.draw(j + 1, self.lst[j + 1], self.bar_color)
                self.update_display()

            if not swapped:
                break

    def GL_partition(self, low, high):
        i = (low-1)
        pivot = self.lst[high]

        for j in range(low, high):
            if self.lst[j] <= pivot:
                i = i+1
                self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
                glClear(GL_COLOR_BUFFER_BIT)
                for k, value in enumerate(self.lst):
                    color = self.compare_color if k == i or k == j else self.bar_color
                    self.draw(k, value, color)
                pygame.display.flip()
                pygame.time.wait(0)
        self.lst[i+1], self.lst[high] = self.lst[high], self.lst[i+1]
        return (i+1)

    def quick_sort(self, low, high):
        if low < high:
            pi = self.partition(low, high) if not self.USE_GL else self.GL_partition(low, high)
            self.quick_sort(low, pi - 1)
            self.quick_sort(pi + 1, high)
