import turtle

# Canvas width
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
#cell size
CELL_SIZE = 40
ERASER_SIZE = 20

# Create screen
screen = turtle.Screen()
screen.setup(CANVAS_WIDTH, CANVAS_HEIGHT)
screen.tracer(0)  # Disable animation for instant drawing
screen.bgcolor("white")

# Create the turtle for drawing
drawer = turtle.Turtle()
drawer.speed(0)
drawer.penup()

# Create the eraser turtle
eraser = turtle.Turtle()
eraser.shape("square")
eraser.color("pink")
eraser.shapesize(ERASER_SIZE / 20)  # Scale it down (default turtle size is 20x20)
eraser.penup()
eraser.hideturtle()  # Hide until click

# Store grid squares in a dictionary
squares = {}

def draw_grid():
    """Draws a grid of blue squares"""
    for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
        for col in range(0, CANVAS_WIDTH, CELL_SIZE):
            drawer.goto(col - CANVAS_WIDTH//2, CANVAS_HEIGHT//2 - row)
            drawer.pendown()
            drawer.fillcolor("blue")
            drawer.begin_fill()
            for _ in range(4):
                drawer.forward(CELL_SIZE)
                drawer.right(90)
            drawer.end_fill()
            drawer.penup()
            squares[(col, row)] = "blue"  # Store square position

def erase_objects(x, y):
    """Erase objects in contact with the eraser"""
    eraser.goto(x, y)
    
    # Convert screen coordinates to grid positions
    for (col, row) in list(squares.keys()):
        if abs(x - (col - CANVAS_WIDTH//2 + CELL_SIZE//2)) < ERASER_SIZE//2 and \
           abs(y - (CANVAS_HEIGHT//2 - row - CELL_SIZE//2)) < ERASER_SIZE//2:
            drawer.goto(col - CANVAS_WIDTH//2, CANVAS_HEIGHT//2 - row)
            drawer.fillcolor("white")  # Erase by coloring white
            drawer.begin_fill()
            for _ in range(4):
                drawer.forward(CELL_SIZE)
                drawer.right(90)
            drawer.end_fill()
            del squares[(col, row)]  # Remove from the dictionary

def start_erasing(x, y):
    """Start eraser at clicked position and follow mouse"""
    eraser.goto(x, y)
    eraser.showturtle()
    screen.ontimer(lambda: follow_mouse(), 10)

def follow_mouse():
    """Move eraser with mouse and erase objects"""
    x, y = screen.cv.winfo_pointerx() - screen.cv.winfo_rootx(), \
           screen.cv.winfo_pointery() - screen.cv.winfo_rooty()
    x -= CANVAS_WIDTH // 2
    y = CANVAS_HEIGHT // 2 - y
    erase_objects(x, y)
    screen.ontimer(follow_mouse, 50)  # Run repeatedly

# Draw the grid and wait for the first click
draw_grid()
screen.update()

screen.onscreenclick(start_erasing)  # Wait for the first click to start erasing
screen.mainloop()
