#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    if len(argv) == 1:
        print("0 arguments.")
        exit()
    elif len(argv) == 2:
        print("1 argument:")
    else:
        print("{} arguments:".format(len(argv)))
    index = 1
    for arg in argv[1:]:
        print("{}: {}".format(index, arg))
        index += 1
