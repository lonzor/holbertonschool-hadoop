#!/usr/bin/env python3
"""
Contains function createdir()
"""
from snakebit.client import Client


def createdir(l):
    """
    Creates directories
    """
    c = Client('localhost', 9000)
    for x in client.mkdir(l, create_parent=True):
        print(x)


if __name__ == '__main__':
    l = ["/Betty", "/Betty/Holberton"]
    createdir(l)
