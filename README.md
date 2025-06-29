# Dynamic Urban Scene Visualization using OpenGL in Python

## Description

This project is a time-based urban scene simulation developed using Python and PyOpenGL. It visualizes a city skyline with dynamic background colors and animated sun movement depending on the hour of the day (military time input from 0–24). The simulation includes:

- Buildings with detailed shapes
- A sun that moves and changes size/color throughout the day
- Sky that gradually changes shades
- Implementation of custom midpoint line and circle drawing algorithms with zone conversion logic

It showcases fundamental concepts of computer graphics such as 2D transformations, symmetry, pixel plotting, and OpenGL-based rendering.

## Features

- **Time-based animation**: Scene changes dynamically based on user-input time (0–24 in military format).
- **Gradient sky rendering**: Background color smoothly transitions to simulate different times of day.
- **Custom-rendered buildings**: Five uniquely styled buildings with separate entry points.
- **Animated sun**: The sun changes position, scale, and color to simulate its movement across the sky.
- **Zone-based line drawing**: Uses 8-way zone detection and transformation to draw lines in all octants.
- **Midpoint circle algorithm**: Efficient algorithm to render circular sun using pixel-based plotting.
- **Matrix-based scaling**: Circle radius is dynamically scaled using matrix multiplication.
- **Real-time OpenGL rendering**: Built using PyOpenGL for GPU-accelerated drawing.


https://www.desmos.com/calculator/y2qvhodvtz

