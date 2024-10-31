import turtle as tur
import colorsys as cs

def prog_1():
    tur.setup(800,800)        # WINDOW SIZE
    tur.speed(0)              # SPEED OF THE POINTER (FIXED SPEED)
    tur.tracer(7)             # DESCRIBE THE SPEED OF POINTER
    tur.width(2)              # WIDTH OF EACH LINE
    tur.bgcolor("black")      # BACKGROUND COLOR
    for j in range(25):
        for i in range(15):
            tur.color(cs.hsv_to_rgb(i/10,j/25,1))
            tur.right(90)     # move pointer to right side at 90deg
            tur.circle(200-j*4, 90)
            tur.left(90)      # move pointer to right side at 90deg
            tur.circle(200-j*4, 90)
            tur.right(100)
            tur.circle(50,24)
    tur.hideturtle()
#prog_1()
def prog_2():
    tur.circle(45)
    tur.circle(55)
    tur.circle(65)
    tur.circle(75)
    tur.circle(85)
    tur.circle(95)
#prog_2()
def desgin_():
    h = 0.001
    tur.speed(0)
    tur.colormode(255)
    tur.Screen().bgcolor("black")
    for i in range(90):
        tur.pencolor(255-2*i,255-2*i,i+3)
        tur.forward(100)
        tur.left(60)
        tur.forward(100)
        tur.right(120)
        tur.circle(50)
        tur.left(240)
        tur.forward(100)
        tur.left(60)
        tur.forward(100)
        h += 0.02
        tur.pencolor(i*2,i+100,255-2*i)
        tur.forward(100)
        tur.right(60)
        tur.forward(100)
        tur.left(120)
        tur.circle(-50)
        tur.right(240)
        tur.forward(100)
        tur.right(60)
        tur.forward(100)
        tur.left(2)
        h += 0.02
    tur.done()
desgin_()
def menu(): 
    print("MENU")
    print("1. Forward")
    print("2. Left")
    print("3. Right")
    print("4. Color")
    print("5. Circle")
tur.color("yellow")
tur.Screen().bgcolor("black")
tur.setup(800,800)
while True:
    menu()
    a = int(input("Move cursor to : "))
    if a==1:
        n = int(input("Length: "))
        tur.forward(n)
        menu()
    elif a==2:
        n = int(input("Degree: "))
        tur.left(n)
        menu()
    elif a==3:
        n = int(input("Degree: "))
        tur.right(n)
        menu()
    elif a==4:
        try:
            n = input("Color: ")
            tur.color(n.lower())
        except:
            print("Invalid color")
        finally:
            menu()
    elif a==5:
        n = int(input("Diameter: "))
        tur.circle(n)
        menu()
    ans = input("If you want to exit press 'n' : ")
    if ans=='n':
        break
    
    
        











    
