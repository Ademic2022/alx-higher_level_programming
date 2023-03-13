#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    for x in range(len(my_list)):
        print(my_list[(-x)-1])
print_reversed_list_integer(my_list)
