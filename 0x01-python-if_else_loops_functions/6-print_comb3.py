#!/usr/bin/python3
for i in range(0, 10):
    for j in range(1 + i, 10):
        if i == 8 and j == 9:
            print(f"{i}{j}", end="\n")
        else:
            print(f"{i}{j}", end=", ")
