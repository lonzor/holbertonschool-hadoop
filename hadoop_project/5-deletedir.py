#!/usr/bin/env python3
"""
Contains function deletedir()
"""
from snakebite.client import Client


def deletedir(l):
    """
    Deletes directoery
    """
    rev_l = sorted(l, reverse=True)
    c = Client('localhost', 9000)

    for x in client.delete(rev_l, recurse=True):
        print(x)


if __name__ == "__main__":
    l = ["/Betty", "/Betty/Holberton"]
    deletedir(l)
