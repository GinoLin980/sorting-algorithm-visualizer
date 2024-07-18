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

This will install `pygame`, `pyopengl` and `pyopengl-accelerate`

If you're using other system or this doesn't work, run

```bash
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
python sort_visualizer.py sort_algo
```

