#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list):
        j = 0
        k = 0
        for tuple in my_list:
            i = tuple[0] * tuple[1]
            j += i
            k += tuple[1]
        return j / k
    return 0
