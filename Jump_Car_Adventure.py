from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import math

# Initializing all variables
vehicle_trans_width = 30

vehicle_trans_height = 0


WIDTH = 800
HEIGHT = 500

particles = []

score_points = 0

vehicle_velocity = 0

jump_mechanism = False

gamestart = True

obstacle_speed = 4  # tree

initial_position_right = 700

initial_position_left = 745

is_visual_effect_enabled = True

cloud_movement = False

cloud_shift_amount = 0

speed_of_power = 2

background_color = [0.0, 0.0, 0.0, 1.0]

ball_x, ball_y = 100, 200  

ball_radius = 10

ball_velocity_x, ball_velocity_y = 3, -2  

powerup_score = 0

# Day /night transition

is_day = False
is_night = True


# Loading bar

loading_bar_height = 0  # Initial height of the loading bar
loading_bar_max_height = 250  # Maximum height for the loading bar
loading_bar_width = 200  # Width of the loading bar
loading_bar_x = 300  # X-coordinate for the bar's left edge
loading_bar_y = 50  # Y-coordinate for the bar's bottom edge
loading_bar_progress = True  # Toggle for loading progress





# Drawing



# Ground
def flower_ground():
    draw_line_mpl(0, 100, 800, 100, (1, 1, 1))
    for i in particles:
        glBegin(GL_POINTS)
        glVertex2f(i[0], i[1])
        glEnd()

for i in range(800):
        particles.append((i, random.randint(92, 99)))




# Car
car_bottom_left_x = 47
car_bottom_left_y = 100
car_bottom_right_x = 108
car_bottom_right_y = 100
car_top_left_x = 47
car_top_left_y = 135
car_top_right_x = 108
car_top_right_y = 135

def vehicle():
    global vehicle_trans_width, vehicle_trans_height

    draw_line_mpl(20 + vehicle_trans_width, 110 + vehicle_trans_height, 75 + vehicle_trans_width, 110 + vehicle_trans_height, (1, 1, 1))  # Lower straight line
    draw_line_mpl(20 + vehicle_trans_width, 110 + vehicle_trans_height, 20 + vehicle_trans_width, 120 + vehicle_trans_height, (1, 1, 1))  # Left attached line
    draw_line_mpl(75 + vehicle_trans_width, 110 + vehicle_trans_height, 75 + vehicle_trans_width, 120 + vehicle_trans_height, (1, 1, 1))  # Right attached line
    draw_line_mpl(20 + vehicle_trans_width, 120 + vehicle_trans_height, 30 + vehicle_trans_width, 120 + vehicle_trans_height, (1, 1, 1))  # Left attached line to the right
    draw_line_mpl(30 + vehicle_trans_width, 120 + vehicle_trans_height, 30 + vehicle_trans_width, 130 + vehicle_trans_height, (1, 1, 1))  # To the right
    draw_line_mpl(75 + vehicle_trans_width, 120 + vehicle_trans_height, 65 + vehicle_trans_width, 120 + vehicle_trans_height, (1, 1, 1))  # Right attached line to the left
    draw_line_mpl(65 + vehicle_trans_width, 120 + vehicle_trans_height, 65 + vehicle_trans_width, 130 + vehicle_trans_height, (1, 1, 1))  # To the left
    draw_line_mpl(30 + vehicle_trans_width, 130 + vehicle_trans_height, 65 + vehicle_trans_width, 130 + vehicle_trans_height, (1, 1, 1))  # Head

    draw_line_mpl(car_bottom_left_x, car_bottom_left_y, car_top_left_x, car_top_left_y, (0, 0, 0))
    draw_line_mpl(car_top_left_x, car_top_left_y, car_top_right_x, car_top_right_y, (0, 0, 0))
    draw_line_mpl(car_bottom_right_x, car_bottom_right_y, car_top_right_x, car_top_right_y, (0, 0, 0))
    draw_line_mpl(car_bottom_right_x, car_bottom_right_y, car_bottom_left_x, car_bottom_left_y, (0, 0, 0))





# Tree
tree_bottom_left_x = 719
tree_bottom_left_y = 100
tree_bottom_right_x = 774
tree_bottom_right_y = 100
tree_top_left_x = 719
tree_top_left_y = 178
tree_top_right_x = 774
tree_top_right_y = 178

item1_x, item1_y = 700, 100
item2_x, item2_y = 730, 130
item3_x, item3_y = 730, 100
item4_x, item4_y = 760, 130
item5_x, item5_y = 760, 100
item6_x, item6_y = 790, 130

is_tree_or_power_up = True

def trees():
    global is_tree_or_power_up
    if is_tree_or_power_up:
        global obstacle_speed
        glEnable(GL_POINT_SMOOTH)
        
        # Tree trunk (drawn as vertical lines)
        for i in range(755 - obstacle_speed, 745 - obstacle_speed, -1):
            draw_line_mpl(i, 100, i, 130, (165 / 255, 42 / 255, 42 / 255))  # Tree trunk
        
        # Tree bounding box (rectangle)
        glColor3f(1, 1, 1)
        draw_line_mpl(tree_bottom_left_x, tree_bottom_left_y, tree_bottom_right_x, tree_bottom_right_y, (1, 1, 1))  # Bottom line
        draw_line_mpl(tree_bottom_left_x, tree_bottom_left_y, tree_top_left_x, tree_top_left_y, (1, 1, 1))  # Left line
        draw_line_mpl(tree_top_left_x, tree_top_left_y, tree_top_right_x, tree_top_right_y, (1, 1, 1))  # Top line
        draw_line_mpl(tree_top_right_x, tree_top_right_y, tree_bottom_right_x, tree_bottom_right_y, (1, 1, 1))  # Right line
        
        # Tree foliage (drawn as points)
        glColor3f(0, 1, 0)
        glPointSize(20)
        glBegin(GL_POINTS)
        glVertex2f(750 - obstacle_speed, 140)
        glVertex2f(735 - obstacle_speed, 145)
        glVertex2f(765 - obstacle_speed, 145)
        glVertex2f(750 - obstacle_speed, 150)
        glVertex2f(750 - obstacle_speed, 166)
        glEnd()
    else:
        # Power-up or other items
        glPointSize(3)
        draw_line_mpl(item1_x, item1_y, item2_x, item2_y, (0, 0, 1))
        draw_line_mpl(item2_x, item2_y, item3_x, item3_y, (0, 1, 0))
        draw_line_mpl(item3_x, item3_y, item4_x, item4_y, (1, 0, 0))
        draw_line_mpl(item4_x, item4_y, item5_x, item5_y, (0, 0, 1))
        draw_line_mpl(item5_x, item5_y, item6_x, item6_y, (1, 0, 0))


# Bouncing Ball
def draw_ball():
    global ball_x, ball_y, ball_radius
    glColor3f(1, 0, 0)  # Red color for the ball
    glBegin(GL_POINTS)
    for i in range(ball_radius):
        midpoint_circle(ball_x, ball_y, i)
    glEnd()

def update_ball():
    global ball_x, ball_y, ball_velocity_x, ball_velocity_y, ball_radius, HEIGHT, WIDTH, car_bottom_left_x, car_bottom_right_x, car_bottom_left_y, car_top_left_y, car_top_right_x, car_bottom_right_y
    global powerup_score
    
    ball_x += ball_velocity_x
    ball_y += ball_velocity_y

    if ball_y - ball_radius <= 0:
        ball_y = ball_radius
        ball_velocity_y *= -1  

    if ball_y + ball_radius >= HEIGHT:
        ball_y = HEIGHT - ball_radius
        ball_velocity_y *= -1

    if ball_x - ball_radius <= 0 or ball_x + ball_radius >= WIDTH:
        ball_velocity_x *= -1

    if (car_bottom_left_x <= ball_x <= car_bottom_right_x) and (car_bottom_left_y <= ball_y <= car_top_left_y):
        ball_velocity_y *= -1  # Reverse vertical velocity
        ball_y = car_top_left_y + ball_radius
        ball_velocity_y *= +1  
        powerup_score += 2 # Increase power-up points 
        
    if (tree_bottom_left_x <= ball_x <= tree_bottom_right_x) and (tree_bottom_left_y <= ball_y <= tree_top_left_y):
        ball_velocity_y *= -1
        ball_y = tree_top_left_y + ball_radius

# Cloud
def clouds():
    global cloud_shift_amount

    glEnable(GL_POINT_SMOOTH)
    glColor3f(0, 0, 1)
    glPointSize(20)
    glBegin(GL_POINTS)

    cloud_positions = [(100, 450), (300, 430), (500, 390), (700, 370)]
    
    for x, y in cloud_positions:
        glVertex2f(x + cloud_shift_amount, y)
        glVertex2f(x + 20 + cloud_shift_amount, y)
        glVertex2f(x + 40 + cloud_shift_amount, y)
        glVertex2f(x + 10 + cloud_shift_amount, y + 10)
        glVertex2f(x + 30 + cloud_shift_amount, y + 10)

    glEnd()

    cloud_shift_amount -= 0.5
    if cloud_shift_amount < -WIDTH:
        cloud_shift_amount = WIDTH 


# Birds
bird1_position = [305, 380]
bird2_position = [335, 400]
bird_wing_angle = 0
bird_wing_direction = 1  # 1 for flapping down, -1 for flapping up

def bird():
    global bird1_position, bird2_position, bird_wing_angle, bird_wing_direction

    glColor3f(0.447, 1.0, 0.973)
    glPointSize(1)

    
    bird_wing_angle += bird_wing_direction * 5
    if bird_wing_angle > 20 or bird_wing_angle < -20:
        bird_wing_direction *= -1

    # Bird 1
    draw_line_mpl(bird1_position[0], bird1_position[1], bird1_position[0] + 15, bird1_position[1], (.447, 1, .973))
    draw_line_mpl(bird1_position[0], bird1_position[1], bird1_position[0] + 13, bird1_position[1] + 8 + bird_wing_angle / 2, (.447, 1, .973))
    draw_line_mpl(bird1_position[0] + 13, bird1_position[1] + 8 + bird_wing_angle / 2, bird1_position[0] + 5, bird1_position[1], (.447, 1, .973))
    draw_line_mpl(bird1_position[0] + 5, bird1_position[1], bird1_position[0] + 5, bird1_position[1] - 10, (.447, 1, .973))
    draw_line_mpl(bird1_position[0] + 5, bird1_position[1] - 10, bird1_position[0], bird1_position[1], (.447, 1, .973))
    draw_line_mpl(bird1_position[0] + 13, bird1_position[1] + 8 + bird_wing_angle / 2, bird1_position[0] + 20, bird1_position[1] + 8 + bird_wing_angle / 2 + 10, (.447, 1, .973))

    # Bird 2
    draw_line_mpl(bird2_position[0], bird2_position[1], bird2_position[0] + 15, bird2_position[1], (.447, 1, .973))
    draw_line_mpl(bird2_position[0], bird2_position[1], bird2_position[0] + 13, bird2_position[1] + 8 + bird_wing_angle / 2, (.447, 1, .973))
    draw_line_mpl(bird2_position[0] + 13, bird2_position[1] + 8 + bird_wing_angle / 2, bird2_position[0] + 5, bird2_position[1], (.447, 1, .973))
    draw_line_mpl(bird2_position[0] + 5, bird2_position[1], bird2_position[0] + 5, bird2_position[1] - 10, (.447, 1, .973))
    draw_line_mpl(bird2_position[0] + 5, bird2_position[1] - 10, bird2_position[0], bird2_position[1], (.447, 1, .973))
    draw_line_mpl(bird2_position[0] + 13, bird2_position[1] + 8 + bird_wing_angle / 2, bird2_position[0] + 20, bird2_position[1] + 8 + bird_wing_angle / 2 + 10, (.447, 1, .973))


def move_birds():
    global bird1_position, bird2_position

    # Move birds horizontally
    bird1_position[0] += 1
    bird2_position[0] += 1

    # Loop the birds back to the left side of the screen
    if bird1_position[0] > WIDTH:
        bird1_position[0] = 0
    if bird2_position[0] > WIDTH:
        bird2_position[0] = 0



# Algorithms



def circle_points(point_x, point_y, center_x, center_y):
    glVertex2f(point_x + center_x, point_y + center_y)
    glVertex2f(point_y + center_x, point_x + center_y)
    glVertex2f(point_y + center_x, -point_x + center_y)
    glVertex2f(point_x + center_x, -point_y + center_y)
    glVertex2f(-point_x + center_x, -point_y + center_y)
    glVertex2f(-point_y + center_x, -point_x + center_y)
    glVertex2f(-point_y + center_x, point_x + center_y)
    glVertex2f(-point_x + center_x, point_y + center_y)


def midpoint_circle(center_x, center_y, radius):
    decision_param = 1 - radius
    current_x = 0
    current_y = radius
    circle_points(current_x, current_y, center_x, center_y)
    while current_x < current_y:
        if decision_param < 0:
            decision_param = decision_param + 2 * current_x + 3
        else:
            decision_param = decision_param + 2 * (current_x - current_y) + 5
            current_y = current_y - 1
        current_x = current_x + 1
        circle_points(current_x, current_y, center_x, center_y)


#Bad Animation

# def draw_line_mpl(x1, y1, x2, y2, color):
#     glColor3f(*color)
    
#     dx = x2 - x1
#     dy = y2 - y1
    
#     d = dy - (dx / 2)
#     x = x1
#     y = y1

#     glBegin(GL_POINTS)
#     glVertex2f(x, y)
    
#     while x < x2:
#         x += 1
#         if d < 0:
#             d = d + dy
#         else:
#             y += 1
#             d = d + (dy - dx)
#         glVertex2f(x, y)
#     glEnd()




def draw_line_mpl(x1, y1, x2, y2, color):
    glColor3f(*color)
    
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    steep = dy > dx
    
    if steep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
        dx, dy = dy, dx
    
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
    
    d = 2 * dy - dx
    y = y1

    for x in range(int(x1), int(x2) + 1):
        if steep:
            glBegin(GL_POINTS)
            glVertex2f(int(y), int(x)) 
            glEnd()
        else:
            glBegin(GL_POINTS)
            glVertex2f(int(x), int(y))
            glEnd()
        
        if d > 0:
            y += 1 if y1 < y2 else -1 
            d -= 2 * dx  
        d += 2 * dy 



# def draw_line_mpl(x1, y1, x2, y2, color):
#     glColor3f(*color)
    
#     dx = x2 - x1
#     dy = y2 - y1
#     d = dy - (dx / 2)
#     x = x1
#     y = y1
    
#     sx = 1 if x1 < x2 else -1
#     sy = 1 if y1 < y2 else -1

#     glBegin(GL_POINTS)
#     glVertex2f(x, y)

#     if abs(dx) > abs(dy):  # If the line is more horizontal than vertical
#         while x != x2:
#             x += sx
#             if d >= 0:
#                 y += sy
#                 d -= dx
#             d += dy
#             glVertex2f(x, y)
#     else:  # If the line is more vertical than horizontal
#         d = dx - (dy / 2)
#         while y != y2:
#             y += sy
#             if d >= 0:
#                 x += sx
#                 d -= dy
#             d += dx
#             glVertex2f(x, y)

#     glEnd()




#Good animation but slow


# def draw_line_mpl(x1, y1, x2, y2, color):
#     glColor3f(*color)
    
#     dx = abs(x2 - x1)
#     dy = abs(y2 - y1)
#     sx = 1 if x1 < x2 else -1
#     sy = 1 if y1 < y2 else -1
#     if dx > dy:
#         d = dy - dx // 2
#         while x1 != x2:
#             if d >= 0:
#                 y1 += sy
#                 d -= dx
#             x1 += sx
#             d += dy
#             glBegin(GL_POINTS)
#             glVertex2f(x1, y1)
#             glEnd()
#     else:
#         d = dx - dy // 2
#         while y1 != y2:
#             if d >= 0:
#                 x1 += sx
#                 d -= dy
#             y1 += sy
#             d += dx
#             glBegin(GL_POINTS)
#             glVertex2f(x1, y1)
#             glEnd()

#     glBegin(GL_POINTS)
#     glVertex2f(x2, y2)
#     glEnd()



# Game Logic


collected_powerups = [False, False, False, False, False, False]

collected_count = 0

game_over = False



def update():
    global obstacle_speed, tree_bottom_left_x, tree_top_left_x, tree_top_right_x, tree_bottom_right_x, tree_top_right_y, car_bottom_left_x, car_bottom_left_y
    global car_bottom_right_x, car_bottom_right_y, car_top_left_x, car_top_left_y, car_top_right_x, car_top_right_y, score_points, gamestart, is_tree_or_power_up, powerup_score, collected_powerups, collected_count, game_over
    global powerup_score 

    if is_tree_or_power_up == True:
        if gamestart == True:
            if obstacle_speed >= 750:
                obstacle_speed = 4
                tree_bottom_left_x, tree_bottom_left_y = 719, 100
                tree_top_left_x, tree_top_left_y = 719, 178
                tree_top_right_x, tree_top_right_y = 774, 178
                tree_bottom_right_x, tree_bottom_right_y = 774, 100
                is_tree_or_power_up = not is_tree_or_power_up

            obstacle_speed += 4
            tree_bottom_left_x -= 4
            tree_top_left_x -= 4
            tree_top_right_x -= 4
            tree_bottom_right_x -= 4

            if ((car_bottom_left_x <= tree_bottom_left_x <= car_bottom_right_x) or (car_bottom_left_x <= tree_bottom_right_x <= car_bottom_right_x)) and (car_bottom_right_y >= tree_top_right_y):
                score_points += 1
                if score_points % 29 == 0:
                    print(int(score_points / 29))

            elif ((car_bottom_left_x <= tree_bottom_left_x <= car_bottom_right_x) or (car_bottom_left_x <= tree_bottom_right_x <= car_bottom_right_x)) and (car_bottom_right_y <= tree_top_right_y):
                print("Game Over")
                game_over = True
                gamestart = False
                
    else:
        global speed_of_power, item1_x, item1_y, item2_x, item2_y, item3_x, item3_y, item4_x, item4_y, item5_x, item5_y, item6_x, item6_y
        if gamestart == True:
            item_positions = [item1_x, item2_x, item3_x, item4_x, item5_x, item6_x]
            for i in range(6):
                item_positions[i] -= speed_of_power
                if ((car_bottom_left_x <= item_positions[i] <= car_bottom_right_x) and not collected_powerups[i] and (car_bottom_left_y <= item_positions[i] <= car_top_left_y)):
                    collected_powerups[i] = True
                    collected_count += 1
            item1_x, item2_x, item3_x, item4_x, item5_x, item6_x = item_positions    
            if collected_count == 6:
                powerup_score += 5
                collected_count = 0  
                print("Power-up score:", powerup_score, "points")
        
        if item6_x < 0 or item1_x < 0:
            item1_x = 700
            item2_x = 730
            item3_x = 730
            item4_x = 760
            item5_x = 769
            item6_x = 790
            is_tree_or_power_up = not is_tree_or_power_up
            collected_powerups = [False, False, False, False, False, False]  
            collected_count = 0  # Reset the count


#Day Night Transition
day_color = [0.53, 0.81, 0.92, 1.0]  # Sky blue (day)
night_color = [0.0, 0.0, 0.0, 1.0]  # Black (night)
transition_speed = 0.01  # Speed of color transition
transitioning_to_day = False
transitioning_to_night = False

def update_background_color(target_color):
    global background_color, transition_speed
    for i in range(3):  
        if background_color[i] < target_color[i]:
            background_color[i] += transition_speed
            if background_color[i] > target_color[i]:
                background_color[i] = target_color[i]
        elif background_color[i] > target_color[i]:
            background_color[i] -= transition_speed
            if background_color[i] < target_color[i]:
                background_color[i] = target_color[i]


# Game Display

game_paused = False


def keyboard(key, x, y):
    global vehicle_trans_height, vehicle_velocity, jump_mechanism, background_color, game_paused
    global transitioning_to_day, transitioning_to_night, day_color, night_color
    global is_day, is_night

    # Implementation of jump mechanism
    if key == b' ' and not jump_mechanism and not game_paused:
        jump_mechanism = True
        vehicle_velocity = 9  
        
    elif key == b'd':
        transitioning_to_day = True  # Start the transition to day color
        transitioning_to_night = False
        is_day = True
        is_night = False
        
    elif key == b'n':
        transitioning_to_night = True  # Start the transition to night color
        transitioning_to_day = False
        is_night = True
        is_day = False
        
    elif key == b'p':
        game_paused = True  # Pause the game
        
    elif key == b's':
        game_paused = False  # Resume the game





def draw_sun():
    glColor3f(1.0, 1.0, 0.0)  # Bright yellow color for the sun
    glBegin(GL_POLYGON)
    
    # Center of the sun
    sun_center_x = 700  # Adjust for your scene's coordinates
    sun_center_y = 400
    sun_radius = 50
    
    # Draw the circle using small line segments
    for angle in range(0, 360, 5):  # Increment in small steps for smoothness
        rad = math.radians(angle)
        x = sun_center_x + sun_radius * math.cos(rad)
        y = sun_center_y + sun_radius * math.sin(rad)
        glVertex2f(x, y)
    
    glEnd()

def draw_moon():
    # Moon center and radius
    moon_center_x = 600
    moon_center_y = 400
    moon_radius = 50
    
    # Colors
    moon_color = (0.9, 0.9, 0.9)  # Light gray for the main moon
    shadow_color = (0, 0, 0)  # Dark shadow for the crescent effect

    # Draw the full moon
    glColor3f(*moon_color)
    glBegin(GL_POLYGON)
    for angle in range(0, 360, 5):
        rad = math.radians(angle)
        x = moon_center_x + moon_radius * math.cos(rad)
        y = moon_center_y + moon_radius * math.sin(rad)
        glVertex2f(x, y)
    glEnd()

    # Draw the shadow (to create the crescent shape)
    glColor3f(*shadow_color)
    glBegin(GL_POLYGON)
    for angle in range(0, 360, 5):
        rad = math.radians(angle)
        x = moon_center_x + moon_radius * 0.8 * math.cos(rad) - 15  # Slight offset for crescent
        y = moon_center_y + moon_radius * 0.8 * math.sin(rad)
        glVertex2f(x, y)
    glEnd()




def animation():
    global transitioning_to_day, transitioning_to_night, day_color, night_color
    if not game_paused:
        if transitioning_to_day:
            update_background_color(day_color)
            if background_color == day_color:
                transitioning_to_day = False
        elif transitioning_to_night:
            update_background_color(night_color)
            if background_color == night_color:
                transitioning_to_night = False
        glutPostRedisplay()




def render_text(string, x, y):
    glColor3f(1.0, 0.0, 0.0)
    glRasterPos2f(x, y)
    for char in string:
        glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24, ord(char))



def render_powerup_score():
    global powerup_score
    glColor3f(1.0, 1.0, 1.0)  
    glRasterPos2f(10, HEIGHT - 20)  
    score_string = f"Power: {powerup_score}"
    for char in score_string:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))


def render_jump_score():
    global score_points
    glColor3f(1.0, 1.0, 1.0)  
    glRasterPos2f(650, HEIGHT - 20)  
    score_string = f"Bounce: {int(score_points / 29)}"
    for char in score_string:
        glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(char))


# Display
def display():
    global vehicle_trans_width, vehicle_trans_height, vehicle_velocity, jump_mechanism, car_bottom_left_y, car_top_left_y, car_top_right_y, car_bottom_right_y, game_over, background_color, health, angle

    glClearColor(*background_color) 
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    glColor3f(0.447, 1.0, 0.973)
    glPointSize(1)

    glBegin(GL_POINTS)
    for i in range(5):
        midpoint_circle(35 + vehicle_trans_width, 106 + vehicle_trans_height, i)
        midpoint_circle(60 + vehicle_trans_width, 106 + vehicle_trans_height, i)
    glEnd()

    if jump_mechanism:
        vehicle_trans_height += vehicle_velocity
        car_bottom_left_y += vehicle_velocity
        car_top_left_y += vehicle_velocity
        car_top_right_y += vehicle_velocity
        car_bottom_right_y += vehicle_velocity
        vehicle_velocity -= 0.2  # Adjust the gravity effect as needed
        if vehicle_trans_height <= 0:
            vehicle_trans_height = 0
            jump_mechanism = False
            vehicle_velocity = 0

    flower_ground()
    vehicle()
    trees()
    bird()
    move_birds()
    clouds()
    update()
    draw_ball()  
    update_ball()  
    render_powerup_score()  
    render_jump_score()
    
    # if transitioning_to_day == True:
    #      draw_loading_bar()  # Draw the loading bar

    if is_day == True:
        draw_sun()

    if is_night == True:
        draw_moon()
    
    if game_over:
        render_text("Game Over", WIDTH / 2 - 50, HEIGHT / 2)
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE)
glutInitWindowSize(WIDTH, HEIGHT)
glutCreateWindow(b"Jumping Car Adventure")
glOrtho(0, WIDTH, 0, HEIGHT, -1, 1)
glClearColor(0, 0, 0, 1)
glutIdleFunc(animation)
glutKeyboardFunc(keyboard)
glutDisplayFunc(display)
glutMainLoop()
