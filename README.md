# OpenGL Graphics Projects

A collection of Python-based computer graphics projects using **PyOpenGL** to demonstrate everything from fundamental rendering to complex 2D game mechanics.

---

## 📁 Repository Structure

### 🏎️ Jump Car Adventure (`Jump_Car_Adventure.py`)
* **Dynamic Environment**: Features a smooth transition between day and night modes using color interpolation triggered by keyboard inputs.
* **Custom Graphics Algorithms**: Implements a custom Midpoint Line Drawing (MPL) algorithm to handle various line slopes and directions.
* **Circle Rendering**: Uses the Midpoint Circle Algorithm to render the car wheels and the bouncing ball.
* **Game Physics**: Includes a gravity-based jumping mechanism where velocity decreases over time until the car returns to the ground.
* **Collision Detection**: Logic is implemented to detect when the car hits trees (Game Over) or collects power-up items based on coordinate overlaps.



### 🎨 Interactive Drawing Tool (`Lets_draw_sth.py`)
* **Coordinate Mapping**: Converts screen-space mouse coordinates to the OpenGL world-space system centered at (0,0).
* **Dynamic Input**: Supports keyboard listeners to increase or decrease point sizes (`W`/`S`) and adjust animation speeds.
* **Animation**: Demonstrates automated movement and coordinate wrapping to keep objects within the viewport.

### 🏁 Hello OpenGL (`Hello_openGL.py`)
* **Minimalist Boilerplate**: A starter script used to initialize the GLUT window and render basic primitives like points.
* **Viewport Setup**: Configures the projection matrix and orthographic view for a $500 \times 500$ window.

---

## 🎮 Controls (Jump Car Adventure)

* **`Space`**: Perform a jump.
* **`D`**: Transition to **Day** (Sun appears).
* **`N`**: Transition to **Night** (Moon appears).
* **`P`**: Pause the game.
* **`S`**: Resume the game.

---

## 🛠️ Technical Implementation

### Core Algorithms
* **Midpoint Line Algorithm**: Lines are drawn pixel-by-pixel by calculating the decision parameter to determine the next pixel coordinates, handling both steep and shallow slopes.
* **Midpoint Circle Algorithm**: Draws circles using 8-way symmetry, calculating points for one octant and mirroring them to the other seven.
* **Collision Logic**: 
    * **Car vs. Tree**: Checks if the car's bounding box overlaps with a tree's position while the car is below the obstacle's height.
    * **Ball vs. Boundaries**: Reverses velocity vectors when the bouncing ball hits window edges or the car roof.

### Mathematics
* **Gravity Simulation**: The car's height is updated by a velocity variable that is reduced by a constant gravity effect every frame.
* **Trigonometry**: Uses `math.cos` and `math.sin` to calculate vertices for the circular sun and moon polygons.

---

## 🚀 Getting Started

### Prerequisites
Ensure you have Python installed, then install the required OpenGL wrappers:
```bash
pip install PyOpenGL PyOpenGL_accelerate
```
