import py5

mode = 0

def setup():
    py5.size(500,500)
    

def key_pressed():
    global mode
    if py5.key >= '0' and py5.key <= '9':
        mode = int(py5.key) - int('0')
        print(mode)

def draw():
    py5.background(0,0,0)
    global mode
    print(mode)

    halfw = py5.width/2
    halfh = py5.height/2
    x = py5.mouse_x
    y = py5.mouse_y

    if mode == 0:
        py5.fill(0,255,0)
        py5.circle(py5.mouse_x, py5.mouse_y, 50)
    if mode == 1:
        py5.fill(255,0,0)
        py5.circle(halfw,halfh,x)
    if mode == 2:
        py5.fill(0,0,255)
        py5.rect(halfw,halfh, x,-y)
        py5.rect_mode(py5.CENTER)

        
py5.run_sketch()