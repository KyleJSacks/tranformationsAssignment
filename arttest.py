from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [255, 255, 255]
edges = []
transform = new_matrix()
ident(transform)

for i in range(100):
    add_edge(edges, i, 0, 0, i, 100, 0)
    add_edge(edges, i, 0, 100, i, 100, 100)
    add_edge(edges, i, 0, 0, i, 0, 100)
    add_edge(edges, 0, i, 0, 0, i, 100)
    add_edge(edges, i, 100, 0, i, 100, 100)
    add_edge(edges, 100, i, 0, 100, i, 100)


matrix_mult(make_translate(100, 100, 0), transform)
matrix_mult(make_rotX(20), transform)
matrix_mult(make_rotY(20), transform)
matrix_mult(make_rotZ(20), transform)
matrix_mult(transform, edges)
draw_lines(edges, screen, color)
display(screen)
