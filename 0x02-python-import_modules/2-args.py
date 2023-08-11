#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
        exit()
    elif len(sys.argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(sys.argv)))
    index = 1
    for arg in sys.argv[1:]:
        print("{}: {}".format(index, arg))
        index += 1
