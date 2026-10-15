import turtle
import math
import colorsys
import time

# Set up the drawing window
screen = turtle.Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("Full Rainbow Spirograph")
screen.tracer(0, 0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(1)

# Pattern settings
LAYERS = 3
CURVES_PER_LAYER = 18
POINTS_PER_CURVE = 600
BASE_RADIUS = 145
LAYER_GAP = 25
WAVE_SIZE = 65
PETALS = 8


def draw_pattern():
    for layer in range(LAYERS):
        for curve in range(CURVES_PER_LAYER):
            phase = (curve / CURVES_PER_LAYER) * math.tau

            for point in range(POINTS_PER_CURVE + 1):
                # math.tau is one complete 360-degree turn
                angle = math.tau * point / POINTS_PER_CURVE

                radius = (
                    BASE_RADIUS
                    + layer * LAYER_GAP
                    + WAVE_SIZE * math.sin(PETALS * angle + phase)
                )

                # Center the complete pattern around the window origin
                x = radius * math.cos(angle)
                y = radius * math.sin(angle)

                hue = (
                    curve / CURVES_PER_LAYER
                    + layer * 0.16
                    + point / POINTS_PER_CURVE * 0.25
                ) % 1

                red, green, blue = colorsys.hsv_to_rgb(hue, 1, 1)
                pen.pencolor(red, green, blue)

                if point == 0:
                    pen.penup()
                    pen.goto(x, y)
                    pen.pendown()
                else:
                    pen.goto(x, y)

                if point % 50 == 0:
                    screen.update()
                    time.sleep(0.001)

            screen.update()


draw_pattern()
screen.mainloop()