import pandas as pd
import py5
import math

#task 1.1
def load_data():
    global df
    df = pd.read_csv("HabHYG15ly.csv", encoding="latin-1")
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
def draw_grid():
    border = 50

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

def stars():
    global df
    #x line
    x = df['Xg'][1]
    y = df['Yg'][1]
    py5.circle(x,y,20)
    



def draw():
    py5.background(0)
    draw_grid()

    

py5.run_sketch()