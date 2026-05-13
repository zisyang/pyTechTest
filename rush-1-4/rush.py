import sys

def rush(x, y):
    """
    Display a square pattern based on x (width) and y (height)

    Args:
        x (int): Width of the square
        y (int): Height of the square
    """
    if x <= 0 or y <= 0:
        print("Invalid size", file=sys.stderr)
        return
        
    indent = "   "
    if x == 1:
        if y >= 1:
            print(f"{indent}B")
        if y > 1:
            for n in range(y-1):
                print(f"{indent}B")
    else:
        if y == 1:
            line=['B']*x
            print("{}{}".format(indent, ''.join(line)))
        elif y > 1:
            line=['B']*(x-2)
            print("{}A{}C".format(indent, ''.join(line)))
            for n in range(y-2):
                line=[' ']*(x-2)
                print("{}B{}B".format(indent, ''.join(line)))
            line=['B']*(x-2)
            print("{}A{}C".format(indent, ''.join(line)))
    print("\n")
    pass
