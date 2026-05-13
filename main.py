import sys
import os
import random

if __name__ == "__main__":
    try:
        if len(sys.argv) == 2:
            sys.path.append(os.path.abspath(f"rush-1-{sys.argv[1]}"))
            from rush import rush
            testcases = ((5,3),
                        (5,1),
                        (1,1),
                        (1,5),
                        (4,4),
                        (random.randint(1,100), random.randint(1,100))
            )
            print(f"Delivery: rush-1-{sys.argv[1]}/*\n")
            case = 0
            for x,y in testcases:
                case+=1
                if case<6:
                    print("When calling rush({},{})".format(x, y))
                else:
                    print("when calling with random numbers: rush({},{})".format(x, y))
                rush(int(x), int(y))
        elif len(sys.argv) == 4:
            sys.path.append(os.path.abspath(f"rush-1-{sys.argv[1]}"))
            from rush import rush
            [x, y] = sys.argv[2:4]
            print("rush({},{})".format(int(x), int(y)))
            rush(int(x), int(y))
        else:
            raise AssertionError("Incorrect number of argv\n  Usage: {} <n> <x> <y>\n        <n> is delivery#(1-5)".format(sys.argv[0]))
    except Exception as e:
        print(e)

