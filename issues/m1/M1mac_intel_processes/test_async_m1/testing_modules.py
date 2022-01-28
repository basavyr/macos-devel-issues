#!/usr/bin/env python

# runs natively ✅
import os

# runs natively ✅
import asyncio

# runs natively ✅
from time import sleep
s
time_of_sleep = 10


def loopedFunction(time_of_sleep):
    for i in range(5):
        print(asyncio.__doc__)
        sleep(time_of_sleep)
        print("Iteration finished...")


async def myFunction(starter, time_of_sleep):
    for i in range(5):
        print(starter)
        sleep(time_of_sleep)
        starter = starter + 10
        print("Iteration finished...")


def main():
    loopedFunction(time_of_sleep)


main()
