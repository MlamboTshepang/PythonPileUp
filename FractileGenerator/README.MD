Read Me Fractile

Project Descrption: Just a fractile creator using python.



Turtle Fractal Drawer
Usage:
  python turtle_fractal.py                 # Koch snowflake, depth 4
  python turtle_fractal.py koch 5         # Koch snowflake, depth 5
  python turtle_fractal.py sierpinski 6   # Sierpinski triangle, depth 6
  python turtle_fractal.py tree 9         # Fractal tree, depth 9





Archive
OLD CODE I May Need Later
- first edition
    # if fractal == 'koch':
    #     t.penup(); t.goto(-280, 160); t.setheading(0); t.pendown()
    #     koch_snowflake(t, 560, depth)
    # elif fractal == 'sierpinski':
    #     t.penup(); t.goto(-280, -280); t.setheading(0); t.pendown()
    #     sierpinski_triangle(t, 560, depth)
    # elif fractal == 'tree':
    #     t.penup(); t.goto(0, -360); t.setheading(90); t.pendown()
    #     fractal_tree(t, 220, max(1, depth + 1))  # trees look better with slightly higher depth
    # else:
    #     t.penup(); t.goto(0, 0); t.pendown()
    #     t.write("Unknown fractal. Use 'koch', 'sierpinski', or 'tree'.", align='center', font=('Arial', 16, 'normal'))

    # screen.update()
    # screen.mainloop()