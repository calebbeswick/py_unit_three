import math

def triangle_area(a, b, c):
    side = (a + b + c) / 2
    Area = math.sqrt(side * (side-a) * (side-b) * (side-c))
    return Area
def main():
    triangle_area()

if __name__ == '__main__':
    main()

