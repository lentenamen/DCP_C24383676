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
    global mode
    py5.background(0)
    py5.fill(0,255,255)

    half_w = py5.width / 2
    half_h = py5.height / 2

    if mode == 0:
        if py5.mouse_x > half_w:
            
            py5.rect(half_w,0,half_w,py5.height)
        else:
            
            py5.rect(0,0,half_w,py5.height)

    elif mode == 1:
        if py5.mouse_x > half_w and py5.mouse_y < half_h:
            
            py5.rect(half_w,0,half_w,half_h)

        elif py5.mouse_x < half_w and py5.mouse_y < half_h:
            
            py5.rect(0,0,half_w,half_h)

        elif py5.mouse_x < half_w and py5.mouse_y > half_h:

            py5.rect(0,half_h,half_w,half_h)

        else:
            py5.rect(half_w,half_h,half_w,half_h)

    elif mode == 2:
        

        if 350 > py5.mouse_x > 150 and 300 > py5.mouse_y >200:
            py5.fill(255, 0, 0) 
        else:
            py5.fill(0, 255, 255)

        py5.rect(150,200,200,100)

py5.run_sketch()