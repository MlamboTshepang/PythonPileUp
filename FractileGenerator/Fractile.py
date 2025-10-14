
import sys
from turtle import Screen, Turtle
import tkinter 

def koch_segment(t: Turtle, length: float, depth: int) -> None:
    if depth == 0:
        t.forward(length)
        return
    l = length / 3.0
    koch_segment(t, l, depth - 1)
    t.left(60)
    koch_segment(t, l, depth - 1)
    t.right(120)
    koch_segment(t, l, depth - 1)
    t.left(60)
    koch_segment(t, l, depth - 1)

def koch_snowflake(t: Turtle, length: float, depth: int) -> None:
    for _ in range(3):
        koch_segment(t, length, depth)
        t.right(120)

def newfractal(t: Turtle, length: float, depth: int) -> None:
    newfractal_side(t, length, depth)
    if depth == 0:
        for _ in range(4):
            t.right(90)
            t.forward(length)
            l = length / 3.0
            newfractal(t, l, depth + 1)
            t.left(90)
        newfractal(t, l, depth + 1)
    return

def sierpinski_triangle(t: Turtle, length: float, depth: int) -> None:
    def tri(size: float, lev: int) -> None:
        if lev == 0:
            t.begin_fill()
            for _ in range(3):
                t.forward(size)
                t.left(120)
            t.end_fill()
            return
        tri(size / 2, lev - 1)
        t.forward(size / 2)
        tri(size / 2, lev - 1)
        t.back(size / 2); t.left(60); t.forward(size / 2); t.right(60)
        tri(size / 2, lev - 1)
        t.left(60); t.back(size / 2); t.right(60)
    tri(length, depth)

def fractal_tree(t: Turtle, length: float, depth: int, angle: float = 25.0, shrink: float = 0.67) -> None:
    if depth == 0 or length < 2:
        return
    t.forward(length)
    t.left(angle)
    fractal_tree(t, length * shrink, depth - 1, angle, shrink)
    t.right(angle * 2)
    fractal_tree(t, length * shrink, depth - 1, angle, shrink)
    t.left(angle)
    t.back(length)



# Main program - Enter Here
def main() -> None:
    fractal = 'sierpinski'
    depth = 4
    if len(sys.argv) > 1:
        fractal = sys.argv[1].lower()
    if len(sys.argv) > 2:
        try:
            depth = int(sys.argv[2])
        except ValueError:
            pass

    screen = Screen()
    screen.setup(width=900, height=900)
    screen.title(f"Turtle Fractal: {fractal} (depth={depth})")
    screen.bgcolor('white')
    screen.tracer(5) 

    t = Turtle(visible=False)
    t.speed(0)
    t.pensize(2)
    t.color('black', 'gray')

    canvas = screen.getcanvas()
    root = canvas.winfo_toplevel()
    toolbar = tkinter.Frame(root, bg='#6A5ACD')
    toolbar.place(relx=0, rely=0, relwidth=1, height=30)

    tkinter.Label(toolbar, text="Fractal Drawer", bg='lightgray').pack(side='left', padx=10)
    entry = tkinter.Entry(toolbar, width=10)
    entry.insert(0, "koch 4")
    entry.pack(side='left', padx=5, expand=True)
    tkinter.Label(toolbar, text="(e.g., 'koch 5', 'sierpinski 6', 'tree 9')", bg='lightgray').pack(side='left', padx=10) 

    def parse(text: str):
        text = text.strip().lower()
        if not text:
            return 'koch', 4
        parts = text.split()
        fractal, depth = None, None

        for p in parts:
            if p in ('koch', 'sierpinski', 'tree'):
                fractal = p
            elif p.isdigit():
                depth = int(p)
            elif p.startswith('depth='):
                try:
                    depth = int(p.split('=')[1])
                except ValueError:
                    pass
        return fractal or 'koch', depth if depth is not None else 4

    def drawText(event=None):
        frac, dep = parse(entry.get())
        dep = max(0, min(8 if frac == 'koch' else 9, dep))
        t.clear()
        if frac == 'koch':
            t.penup()
            t.goto(-280, 160)
            t.setheading(0)
            t.pendown()
            koch_snowflake(t, 500, dep)
        elif frac == 'sierpinski':
            t.penup()
            t.goto(-280, -280)
            t.setheading(0)
            t.pendown()
            sierpinski_triangle(t, 560, dep)
        elif frac == 'tree':
            t.penup()
            t.goto(0, -360)
            t.setheading(90)
            t.pendown()
            fractal_tree(t, 220, max(1, dep + 1))
        elif frac == 'newfractal':
            t.penup()
            t.goto(-200, 100)
            t.setheading(0)
            t.pendown()
            newfractal(t, 400, dep)
        else:
            t.penup()
            t.goto(0, 0)
            t.pendown()
            t.write("Unknown fractal. Use 'koch', 'sierpinski', or 'tree'.", align='center', font=('Arial', 16, 'normal'))
        screen.update()

    tkinter.Button(toolbar, text="Draw", command=drawText).pack(side='left', padx=5)
    entry.bind('<Return>', drawText)
    drawText()
    screen.mainloop()

if __name__ == '__main__':
    main()
