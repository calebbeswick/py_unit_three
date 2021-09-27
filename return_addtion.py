# Write your addition function in the space below...

def add_two(x, y):
    """
    Adds the two numbers. Adding 5 and 10 would return 15
    :param x: integer value
    :param y: integer value
    :return: integer of x times y
    """
    num1 = x + y
    return num1


# Do not change anything below these lines
def main():

    answer = add_two(x, y)
    print(answer)

if __name__ == '__main__':
    main()