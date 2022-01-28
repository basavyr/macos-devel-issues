#!/usr/bin/env python

import asyncio
import iterm2


async def myFunction(starter, time_of_sleep):
    for i in range(5):
        print(starter)
        sleep(time_of_sleep)
        starter = starter + 10
        print("Iteration finished...")


async def main(connection):
    x=1
    


iterm2.run_forever(main)