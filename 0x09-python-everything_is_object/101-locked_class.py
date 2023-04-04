#!/usr/bin/python3
""" LockedClass
"""

class LockedClass:
    __slots__ = 'first_name'

    def __setattr__(self, key, value):
        if not hasattr(self, 'first_name') and key != 'first_name':
            raise AttributeError("Cannot add new attribute to LockedClass")
        object.__setattr__(self, key, value)
