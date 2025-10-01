import py5

mode = 0

def key_pressed():
    global mode
    if py5.key >= '0' and py5.key <= '9':
        mode = int(py5.key) - int('0')
        

def mouse_pressed():
    if py5.is_mouse_pressed:
        return 1

def setup():
    py5.size(500, 500)
    py5.background(0,0,0)

def draw():
    global mode
    print(mode)
    py5.background(0,0,0)
    
    if py5.is_mouse_pressed:
        if mode == 0:
            py5.fill(255, 0, 0)
            py5.circle(py5.mouse_x, py5.mouse_y, 50)
        elif mode == 1:
            py5.fill(0, 255, 0)
            py5.rect(py5.mouse_x, py5.mouse_y, 80, 80)
        elif mode == 2:
            py5.fill(0, 0, 255)
            py5.triangle(
                py5.mouse_x, py5.mouse_y - 40,
                py5.mouse_x - 40, py5.mouse_y + 40,
                py5.mouse_x + 40, py5.mouse_y + 40
            )
        



            
py5.run_sketch()   