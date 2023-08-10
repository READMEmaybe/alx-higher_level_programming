#!/usr/bin/python3
if __name__ == '__main__':
    import calculators_1
    a = 10
    b = 5
    print("{} + {} = {}".format(a, b, calculators_1.add(a, b)))
    print("{} - {} = {}".format(a, b, calculators_1.sub(a, b)))
    print("{} * {} = {}".format(a, b, calculators_1.mul(a, b)))
    print("{} / {} = {}".format(a, b, calculators_1.div(a, b)))