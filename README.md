# sorting-algorithm-visualizer

This is a sorting algorithm visulizer made with Pygame and OpenGL.

---

## Prerequisites

This program needs `Pygame`, `numpy`, and `PyOpenGL`

```bash
pip install pygame numpy pyopengl pyopengl-accelerate
```

If your `PyOpenGL` or `PyOpenGL-accelerate` installation failed, run

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
python sort_visualizer.py sort_algo
```

