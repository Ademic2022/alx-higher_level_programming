#!/usr/bin/python3
""" LockedClass
"""

class LockedClass:
    __slots__ = ['first_name']

    def __init__(self):
        pass

    def __setattr__(self, name, value):
        if name != 'first_name':
            raise AttributeError("'LockedClass' object has no attribute '{}'".format(name))
        super().__setattr__(name, value)
