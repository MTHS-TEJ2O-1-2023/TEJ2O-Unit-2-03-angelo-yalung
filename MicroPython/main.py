"""
Created by: Angelo Yalung
Created on: Sep 2023
This module is a Micro:bit MicroPython program
"""

from microbit import *


display.scroll("The Area for a Rectangle that is 3x5 is" + str(3 * 5))
display.show(Image.HAPPY)
sleep(0.5)
display.clear()

display.scroll("The perimeter of a Rectangle that is 3x5 is" + str(2 * (8 + 5)))
display.show(Image.HAPPY)
sleep(0.5)
display.clear()
