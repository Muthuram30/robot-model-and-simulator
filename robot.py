# state
history=[]
ptr=-1
width=1000
height=1000
orientation="N"
x,y=0,0
battery_level=100
flag=0
#save till the update is made, so whenever place,move,rotate,and battery check has to be saved
def save_state():
    global history, ptr, x, y, orientation, battery_level

    history[:] = history[:ptr+1]
    history.append((x, y, orientation, battery_level))
    ptr += 1
#access the ptr values
def restore_state():
    global x, y, orientation, battery_level, history, ptr
    x, y, orientation, battery_level = history[ptr]
#ptr-1 and restore
def undo():
    global ptr
    if ptr <= 0:
        print("Nothing to undo")
        return
    ptr -= 1
    restore_state()
    print("Undo done")
#ptr+1 and restore
def redo():
    global ptr
    if ptr >= len(history)-1:
        print("Nothing to redo")
        return
    ptr += 1
    restore_state()
    print("Redo done")


def world():
    global width, height

    w = input("Enter the width in range 0 to 2000 (press Enter for default 1000): ")
    if w == "":
        width = 1000
        print("Width assumed default value 1000")
    else:
        width = int(w)

    h = input("Enter the height in range 0 to 2000 (press Enter for default 1000): ")
    if h == "":
        height = 1000
        print("Height assumed default value 1000")
    else:
        height = int(h)

def battery():
    global battery_level
    c=int(input("Enter charge amount: "))
    if c<=0:
        print("Invalid charge amount")
        return
    battery_level=min(100,battery_level+c)
    save_state()

def battery_check():
    global battery_level
    if(battery_level<=0):
        print("Insufficient battery")
        return 0
    return 1

def place():
    global x,y,orientation,flag
    print("Place the robot!")

    x_dummy=input("Enter x position: ")
    y_dummy=input("Enter y position: ")

    if x_dummy=="":
        x=0
        print("x assumed to be 0")
    else:
        x=int(x_dummy)
    if y_dummy=="":
        y=0
        print("y assumed to be 0")
    else:
        y=int(y_dummy)

    o_input = input("Enter orientation (N/S/E/W) (press Enter for default N): ").upper()
    if o_input == "":
        orientation = "N"
        print("Orientation assumed default value N")
    else:
        orientation = o_input

    if orientation not in ["N","S","E","W"]:
        print("Invalid orientation")
        return

    if(boundary_check()):
        flag=1
        save_state()
    else:
        print("Invalid position")

def boundary_check():
    if x < 0 or y < 0 or x > width or y > height:
        print("Out of boundary!")
        return 0
    return 1

def move():
    global orientation,x,y,battery_level
    if(not battery_check()):
        return
    steps=int(input("Enter number of steps: "))
    oldx,oldy=x,y #store back if boundary check fails

    if(orientation=="N"):
        y+=steps
    elif(orientation=="S"):
        y-=steps
    elif(orientation=="E"):
        x+=steps
    elif(orientation=="W"):
        x-=steps

    if boundary_check():
        battery_level-=abs(steps)
        save_state()
    else:
        print("Move cancelled due to boundary limit")
        x,y=oldx,oldy

def rotate():
    global orientation
    dirs = ['N', 'E', 'S', 'W']
    i = dirs.index(orientation)
    rot = int(input("Enter rotation left(0) or right(1): "))

    if rot not in [0,1]:
        print("Invalid rotation")
        return

    orientation = dirs[(i + 1) % 4] if rot else dirs[(i - 1) % 4]
    save_state()

def report():
    print("Robot position:", x,y)
    print("Robot orientation:", orientation)
    print("Battery level:", battery_level,"%")



world()

print('''
1) Place robot  (Place the robot in grid)
2) Move robot
3) Rotate robot
4) Charge battery
5) Report status
6) Undo last command
7) Redo last command
0) Exit
''')

while True:
    choice = int(input("Enter your choice: "))

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