# Caleb Beswick 9/30/21
#This program draws a flower shape with inmputable side lengths and colors for petals and the center.
#


import turtle


def get_side_length():
    """

    :return: Returns side length of hexagon in pixels
    """
    side_length = float(input("Please enter the side length "))
    return side_length

def get_center_color():
    """

    :return: Returns the color of the center of the flower
    """
    center_color = input("Please enter the center color ")
    return center_color

def get_petal_color():
    """

    :return: Returns the petal color of the petals of the flower
    """
    petal_color = input("Please enter the petal color ")
    return petal_color

def draw_hexagon(pc, sl, cc):
    """

    :param pc: pc is the color of the petal of the flower
    :param sl: The length of the side of the hexagon in pixels
    :param cc: The center color of the flower
    :return:
    """
    turtle.color(pc)
    turtle.begin_fill()
    for x in range(6): #Draws the petals of the flower
        turtle.right(120)
        turtle.fd(sl)
        turtle.left(60)
        for x in range(6):
            turtle.fd(sl)
            turtle.right(60)
    turtle.left(120)
    turtle.end_fill()
    turtle.color(cc)
    turtle.begin_fill()
    for x in range(6): #Draws the center of the flower
        turtle.fd(sl)
        turtle.left(60)
    turtle.end_fill()



    turtle.exitonclick()


def main():
    pc = get_petal_color() #gets lengths of side, and colors of petal and color.
    sl = get_side_length()
    cc = get_center_color()
    turtle.hideturtle()
    draw_hexagon(pc, sl, cc)

if __name__ == '__main__':
    main()