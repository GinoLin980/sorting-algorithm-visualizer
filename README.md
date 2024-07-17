# sorting-algorithm-visualizer

This is a sorting algorithm visulizer made with Pygame and OpenGL.

---

## Prerequisites

This program needs `Pygame` and `OpenGL`(optional)

run this if you use Pygame version only:

```bash
pip install pygame
```

run this if you use OpenGL included version:

```bash
pip install -r requirements.txt
```

This will install `PyOpenGL-3.1.7-cp312-cp312-win_amd64` which is for PyOpenGL 3.17 for x86 Windows with Python 3.12

If you're using other system or this doesn't work, run

```bash
git clone https://github.com/mcfletch/pyopengl.git
cd pyopengl
pip install -e .
cd accelerate
pip install -e .
```

---

## Run this program

The current available algorithms are:

| bubble_sort | quick_sort |
|-------------|------------|

To run this program, type 

```bash
python sort_visualizer_openGL.py sort_algo
```

