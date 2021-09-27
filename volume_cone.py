# Write your cone volume function in the space below...
import math

def cone(radius, h):
    vol1 = math.pi * radius ** 2
    vol2 = h / 3
    vol_final = vol1 * vol2
    final = round(vol_final, 2)
    print("The volume of the cone is", final)

# Do not change anything below these lines
def main():
    cone(radius, h)

if __name__ == '__main__':
    main()