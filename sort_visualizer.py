import sys; sys.dont_write_bytecode = True
import pygame
import time
import numpy as np
from OpenGL.GL import *
from pygame.locals import *
from sorting_algorithms import SortingAlgorithms
from GUI import Sort_Visualizer_GUI
from pygame_screen_record import ScreenRecorder

BAR_COLOR: tuple[float] = (1, 0.603, 0.541)  # Peach Pink
COMPARE_COLOR: tuple[float] = (1, 0, 1)  # Purple
settings = {"Start_Visual": False}
APP = Sort_Visualizer_GUI(settings)

while True:
    APP.run()
    settings = APP.get_settings()
    if settings["Start_Visual"]:
        try:
            def reso(resolution: int, direction: str) -> tuple[int, int]:
                """Return 16:9 resolution.

                params: int, str ["p", "l"]

                Example:
                reso(1080, l) -> 1920, 1080
                """
                if direction.lower() == "portrait":
                    return resolution, resolution * 16 / 9
                if direction.lower() == "landscape":
                    return resolution * 16 / 9, resolution


            print(settings)
            # Initialize Pygame
            pygame.init()
            screen = pygame.display.set_mode((reso(settings["reso"], settings["orient"])), DOUBLEBUF | OPENGL)
            pygame.display.set_caption('Sorting Algorithm Visualizer With Pygame and OpenGL')
            if settings["record_this_sort"] == True:
                recorder = ScreenRecorder(fps=30, surf=screen)
                recorder.start_rec()

            # Constants
            WIDTH = screen.get_width()
            HEIGHT = screen.get_height()
            ARR = np.arange(1, settings["elements"] + 1)
            np.random.shuffle(ARR)
            N = len(ARR)
            BAR_WIDTH = WIDTH / N
            HEIGHT_UNIT: float = HEIGHT / max(ARR)
            MARGIN = 100 / N

            # OpenGL settings
            glClearColor(0.0, 0.0, 0.0, 1.0)
            glClear(GL_COLOR_BUFFER_BIT)
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)  # set the start(origin) point from the bottom left of the window
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()


            def draw_bar(index: int, value: float | int, color: tuple[float]) -> None:
                """Use OpenGL to draw rectangles."""
                glColor3f(*color)
                glBegin(GL_QUADS)
                glVertex2f(BAR_WIDTH * index, 0)
                glVertex2f(BAR_WIDTH * (index + 1) - MARGIN, 0)
                glVertex2f(BAR_WIDTH * (index + 1) - MARGIN, HEIGHT_UNIT * value)
                glVertex2f(BAR_WIDTH * index, HEIGHT_UNIT * value)
                glEnd()


            def init_bar(arr) -> None:
                """Draw out all the shuffled array."""
                for i, value in enumerate(arr):
                    draw_bar(i, value, BAR_COLOR)


            # Main loop
            init_bar(ARR)
            pygame.display.flip()
            sorting_algo = SortingAlgorithms(ARR, screen, WIDTH, HEIGHT, MARGIN, BAR_COLOR, COMPARE_COLOR, (0, 0, 0), 0.005)
            running = True

            if settings["algo"].lower().replace(' ', '_') == "quick_sort":
                action = sorting_algo.quick_sort
                algo_name = "Quick Sort"
                params = (0, N - 1)
            elif settings["algo"].lower().replace(' ', '_') == "bubble_sort":
                action = sorting_algo.bubble_sort
                algo_name = "Bubble Sort"
                params = (None, None)
            else:
                print("Invalid sorting algorithm. Choose 'quick_sort' or 'bubble_sort'.")
                running = False

            while running:
                try:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            running = False
                except Exception as e:
                    pygame.quit()
                    break
                action(*params)

                if np.array_equal(ARR, np.sort(ARR)):
                    time.sleep(1)
                    break

            try:
                if settings["record_this_sort"] == True:
                        recorder.stop_rec()
                        recorder.save_recording(f"{algo_name}.avi")
                        print("we've reached end of rec")
                pygame.quit()
            except Exception as e:
                pass
        except:
            print("record error"); sys.exit()

        settings["Start_Visual"] = False
        settings["record_this_sort"] = False
