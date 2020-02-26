from display import *
from draw import *
from parser import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
edges = []
transform = new_matrix()

transform = make_rotX(180)
print_matrix(transform)
#parse_file( 'script', edges, transform, screen, color )
