#!/usr/bin/env python3
"""
Contains function download()
"""
from snakebite.client import Client


def download(l):
    """
    Downloads a file
    """
    rev_l = sorted(l, reverse=True)
    c = Client('localhost', 9000)
    for x in client.copyToLocal(rev_l, "/tmp"):
        print(x)


if __name__ == "__main__":
    l = ["/holbies/input/lao.txt"]
    download(l)
    lao = open("/tmp/lao.txt", "r")
    lao.close()
