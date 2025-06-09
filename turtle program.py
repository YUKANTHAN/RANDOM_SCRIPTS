import turtle

# Create a turtle object
pen = turtle.Turtle()

# Set the turtle's speed
pen.speed(0)  # Set to the fastest speed

# Draw a square
for _ in range(4):
    pen.forward(100)
    pen.left(90)

# Keep the turtle window open until it is manually closed
turtle.done()
