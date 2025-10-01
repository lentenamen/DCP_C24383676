import pandas as pd
import py5
import math

selected_star_1 = None
selected_star_2 = None

#task 1.1
def load_data():
    global df
    df = pd.read_csv("week3dcp/HabHYG15ly.csv", encoding="latin-1")
    print(f"Loaded {len(df)} stars")

#1.2
def setup():
    global df
    py5.size(750, 750)
    load_data()        
    print_stars()       

#2
def print_stars():
    global df
    print(f"number of stars {len(df)} ")
    name = df['Display Name']
    distance = df['Distance']
    x = df['Xg']
    y = df['Yg']
    z = df['Zg']
    for i in range(5):
        print(name[i], distance[i], x[i], y[i], z[i])

#3
border = 50
def draw_grid():
    global border

    for i in range(-5,6):
        x = py5.remap(i, -5, 5, border, py5.width - border )
        y = py5.remap(i, -5, 5, border, py5.height - border )
        py5.text(i,x,25)
        py5.text(i,25,y)
        
    py5.stroke(128, 0, 128)
    for i in range(50, py5.width, 50):
        py5.line(i, 50, i, py5.height - 50)

    for j in range(50, py5.width, 50):
        py5.line(50, j, py5.width - 50, j)

#4
def draw_stars():
    global df
    global border

    for i, row in df.iterrows():
        xg = row['Xg']
        x = py5.remap(xg, -5, 5, border, py5.width - border)
        yg = row['Yg']
        y = py5.remap(yg, -5, 5, border, py5.height - border)
        py5.stroke(255,255,0)
        py5.line(x-5,y,x+5,y)
        py5.line(x,y-5,x,y+5)

        py5.no_fill()
        py5.stroke(255,0,0)
        py5.circle(x, y, 10)

#5
def find_clicked_star(mouse_x, mouse_y):
    global selected_star_1
    global selected_star_2

    min_dist = float('inf')
    clicked_star = None

    for i, row in df.iterrows():
        x = py5.remap(row['Xg'], -5, 5, border, py5.width - border)
        y = py5.remap(row['Yg'], -5, 5, border, py5.height - border)
        dist = math.hypot(mouse_x - x, mouse_y - y)

        if dist < 10 and dist < min_dist:
            min_dist = dist
            clicked_star = row

    if clicked_star is not None:
        if selected_star_1 is None:
            selected_star_1 = clicked_star
        elif selected_star_2 is None:
            selected_star_2 = clicked_star
        else:
            selected_star_1 = clicked_star
            selected_star_2 = None
        print(f"Selected: {clicked_star['Display Name']}")

    


def mouse_pressed():
    find_clicked_star(py5.mouse_x, py5.mouse_y)


def draw():
    py5.background(0)
    draw_grid()
    draw_stars()

py5.run_sketch()