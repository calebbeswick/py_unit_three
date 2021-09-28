import turtle

def get_side_length():
    side_length = float(input("Please enter the side length "))
    return side_length

def get_center_color():
    center_color = input("Please enter the center color ")
    return center_color

def get_petal_color():
    petal_color = input("Please enter the petal color ")
    return petal_color

def draw_hexagon(pc, sl, cc):
    for x in range(6):
        turtle.fd(sl)
        turtle.right(60)
    turtle.right(120)
    for x in range(6):
        turtle.fd(sl)
        turtle.right(60)
    turtle.left(300)
    turtle.fd(sl)
    for x in range(6):
        turtle.fd(sl)
        turtle.right(60)



def main():
    pc = get_petal_color()
    sl = get_side_length()
    cc = get_center_color()
    draw_hexagon(pc, sl, cc)

if __name__ == '__main__':
    main()