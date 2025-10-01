import py5
import pandas as pd
import math

# Global variables
stars_df = None
selected_star_1 = None
selected_star_2 = None

def load_data():
    """Load star data from CSV"""
    # Your code here
    pass

def print_stars():
    """Print star information"""
    # Your code here
    pass

def parsecs_to_pixels_x(parsecs):
    """Convert parsec X to pixel X"""
    return py5.remap(parsecs, -5, 5, 50, 750)

def parsecs_to_pixels_y(parsecs):
    """Convert parsec Y to pixel Y"""
    return py5.remap(parsecs, -5, 5, 50, 750)

def draw_grid():
    """Draw coordinate grid"""
    # Your code here
    pass

def draw_stars():
    """Draw all stars"""
    # Your code here
    pass

def find_clicked_star(mouse_x, mouse_y):
    """Find which star was clicked"""
    # Your code here
    pass

def calculate_distance(star1, star2):
    """Calculate 3D distance between stars"""
    # Your code here
    pass

def setup():
    py5.size(800, 800)
    global stars_df
    stars_df = load_data()
    print_stars()

def draw():
    py5.background(0)
    draw_grid()
    draw_stars()
    # Add interactive line drawing here

def mouse_pressed():
    """Handle mouse clicks"""
    # Your code here
    pass

py5.run_sketch()