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

## Tech Stack

- **Python 3.10+**
- **PyOpenGL** – for OpenGL bindings
- **GLUT (OpenGL Utility Toolkit)** – windowing and input
- **NumPy** – for matrix operations and scaling

## Requirements

Before running the project, make sure you have the following dependencies installed:

- Python 3.10 or later
- PyOpenGL
- PyOpenGL_accelerate (optional, for performance)
- FreeGLUT (OpenGL Utility Toolkit)
- NumPy

### Installation (Windows/Linux/macOS)

You can install the required Python libraries using pip:

```bash
pip install PyOpenGL PyOpenGL_accelerate numpy
```

Make sure freeglut or an equivalent OpenGL runtime is installed on your system. On Linux, you can install it via:

```bash
sudo apt-get install freeglut3-dev
```

On Windows, you may need to install freeglut via an installer or ensure it comes bundled with your graphics driver.


## How to Run

1. Clone or download this repository to your local machine.
2. Open a terminal or command prompt in the project directory.
3. Run the Python script using:

```bash
python project.py
```

4. When prompted in the terminal, enter the time in military format (0–24).

- For example: 7 for 7:00 AM or 15 for 3:00 PM

5. The OpenGL window will display:

   - A gradient background representing the sky

   - Buildings with entry points

   - A sun that changes position, size, and color based on the entered time

## Project Structure
```
ComputerGraphics_Project/
│
├── project.py        # Main script containing the entire simulation logic
├── README.md      # Project documentation
```
## Key Functional Components:

- `findZone()`, `ZoneZeroConversion()`  
  → Implements zone detection and coordinate transformations for line drawing.

- `MidPointLine()`, `eight_way_symmetry()`  
  → Midpoint line drawing algorithm using 8-way symmetry.

- `midPoint()`, `draw_circle()`  
  → Midpoint circle drawing for rendering the sun.

- `BackGroundColour()`  
  → Updates sky color based on time.

- `buildingX()`  
  → Draws individual buildings.

- `coordinating_circle()`  
  → Updates sun position and color dynamically.

- `showScreen()`  
  → Main display function combining background, buildings, and the sun.

## Concepts Used

This project incorporates several core concepts from computer graphics:

- **Midpoint Line Drawing Algorithm**  
  Used to plot lines between two points using efficient integer calculations. Works with zone-based transformations to support all directions.

- **Zone Detection (8-way symmetry)**  
  The 2D space is divided into 8 zones to generalize line plotting in all octants using only Zone 0 logic.

- **Midpoint Circle Drawing Algorithm**  
  Efficient way to draw a circle by calculating symmetric pixel points around the center.

- **2D Scaling with Matrices**  
  The sun's size is adjusted using scaling transformations implemented with NumPy matrix multiplication.

- **Real-Time Rendering with OpenGL**  
  Visual elements are rendered in real time using PyOpenGL and GLUT windowing.

- **Time-based Animation**  
  Scene elements (sky and sun) change dynamically based on user-inputted time to simulate real-world lighting.


https://www.desmos.com/calculator/y2qvhodvtz

