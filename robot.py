history=[]
ptr=-1
w=1000
h=1000
o="N"
x,y=0,0
b=100
flag=0

def save_state():
    global history, ptr, x, y, o, b

    history[:] = history[:ptr+1]

    history.append((x, y, o, b)) #loading a tuple inside the list
    ptr += 1

def restore_state():
    global x, y, o, b, history, ptr
    x, y, o, b = history[ptr] #form of equating a tuple

def undo():
    global ptr
    if ptr <= 0:
        print("Nothing to undo")
        return
    ptr -= 1
    restore_state()
    print("Undo done")

def redo():
    global ptr
    if ptr >= len(history)-1:
        print("Nothing to redo")
        return
    ptr += 1
    restore_state()
    print("Redo done")


def world():
    global w,h
    w=int(input("w"))
    h=int(input("h"))

def battery():
    global b
    c=int(input("c"))
    if c<=0:
        print("Invalid charge amount")
        return
    b=min(100,b+c)
    save_state()

def battery_check():
    global b
    if(b<=0):
        print("Insufficient battery")
        return 0
    return 1



def place():
    global x,y,o,flag
    x=int(input("x"))
    y=int(input("y"))
    o=input("orientation").upper()
    if o not in ["N","S","E","W"]:
        print("Invalid orientation")
        return
    if(boundary_check()):
        flag=1
        save_state()
    else:
        print("Invalid position")
    

def boundary_check():
    if x < 0 or y < 0 or x > w or y > h:
        print("out of bound")
        return 0
    return 1

def move():
    global o,x,y,b
    if(not battery_check()):
        return
    steps=int(input("steps"))
    oldx,oldy=x,y
    if(o=="N"):
        y+=steps
    elif(o=="S"):
        y-=steps
    elif(o=="E"):
        x+=steps
    elif(o=="W"):
        x-=steps
    if boundary_check():
        b-=abs(steps)
        save_state()
    else:
        print("move cancel")
        x,y=oldx,oldy

def rotate():
    global o
    dirs = ['N', 'E', 'S', 'W']
    i = dirs.index(o)
    rot = int(input("left(0) or right(1): "))
    if rot not in [0,1]:
        print("Invalid rotation")
        return
    o = dirs[(i + 1) % 4] if rot else dirs[(i - 1) % 4]
    save_state()

def report():
    print("position", x,y)
    print("orientation", o)
    print("battery level", b)




world()

print('''
1) Place robot  ( places the robot in a specific position in the grid)
2) Move (forward/back)
3) Rotate (left/right)
4) Charge battery
5) Report status ( reports the position in grid, orientation, and battery level) 
6) Undo last command
7) Redo last command
0) Exit''')
while True:
    choice = int(input("Enter choice: "))

    if choice == 0:
        break
    elif choice == 1:
        place()
    elif not flag:
        print("Place the robot first!")
    elif choice == 2:
        move()
    elif choice == 3:
        rotate()
    elif choice == 4:
        battery()
    elif choice == 5:
        report()
    elif choice == 6:
        undo()
    elif choice == 7:
        redo()