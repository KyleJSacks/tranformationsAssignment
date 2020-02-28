from display import *
from matrix import *
from draw import *
"""
Goes through the file named filename and performs all of the actions listed in that file.
The file follows the following format:
     Every command is a single character that takes up a line
     Any command that requires arguments must have those arguments in the second line.
     The commands are as follows:
         line: add a line to the edge matrix -
               takes 6 arguemnts (x0, y0, z0, x1, y1, z1)
         ident: set the transform matrix to the identity matrix -
         scale: create a scale matrix,
                then multiply the transform matrix by the scale matrix -
                takes 3 arguments (sx, sy, sz)
         translate: create a translation matrix,
                    then multiply the transform matrix by the translation matrix -
                    takes 3 arguments (tx, ty, tz)
         rotate: create a rotation matrix,
                 then multiply the transform matrix by the rotation matrix -
                 takes 2 arguments (axis, theta) axis should be x y or z
         apply: apply the current transformation matrix to the edge matrix
         display: clear the screen, then
                  draw the lines of the edge matrix to the screen
                  display the screen
         save: clear the screen, then
               draw the lines of the edge matrix to the screen
               save the screen to a file -
               takes 1 argument (file name)
         quit: end parsing

See the file script for an example of the file format
"""
def parse_file( fname, points, transform, screen, color ):
    with open(fname, 'r') as f:
	cmnds = f.readlines()
	i = 0
	while True:
	    c = cmnds[i]
	    c = c.strip('\n')
	    if c == 'line':
		args = cmnds[i + 1].strip('\n').split()
		i += 1
		add_edge(points, int(args[0]), int(args[1]), int(args[2]), int(args[3]), int(args[4]), int(args[5]))
	    elif c == 'ident':
		ident(transform)
	    elif c == 'scale':
		args = cmnds[i + 1].strip('\n').split()
		i += 1
		matrix_mult(make_scale(int(args[0]), int(args[1]), int(args[2])), transform)
	    elif c == 'move':
		args = cmnds[i + 1].strip('\n').split()
		i += 1
		matrix_mult(make_translate(int(args[0]), int(args[1]), int(args[2])), transform)
	    elif c == 'rotate':
		args = cmnds[i + 1].strip('\n').split()
		i += 1
		if args[0] == 'x':
		    matrix_mult(make_rotX(int(args[1])), transform)
		    print_matrix(make_rotX(int(args[1])))
		elif args[0] == 'y':
		    matrix_mult(make_rotY(int(args[1])), transform)
		    print_matrix(make_rotY(int(args[1])))
		else:
		    matrix_mult(make_rotZ(int(args[1])), transform)
		    print_matrix(make_rotZ(int(args[1])))
	    elif c == 'apply':
		matrix_mult(transform, points)
	    elif c == 'display':
		clear_screen(screen)
		draw_lines(points, screen, color)
		display(screen)
	    elif c == 'save':
		args = cmnds[i + 1].strip('\n').split()
		i += 1
		clear_screen(screen)
		save_ppm(screen, args[0])
	    elif c == 'quit':
		break
	    i += 1
				
		
