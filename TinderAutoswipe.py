#!/usr/bin/env python
# Auto-Swipe-Right_TINDER

_author_''' John Melody  Me'''
"""
 Will not run in anywhere then using the shell: 
Require:::
        [+]  Download python-  https://www.python.org/
        [+]  pip install PyAutoGUI  && pip3 install PyAutoGUI   :

            On Windows: 
            >C:\Python34\pip.exe install pyautogui

            On OSX:
            >>>pip3 install pyobjc-core
            >>>pip3 install pyobjc
            >>>pip3 install pyautogui

            On Linux:
            bash$~  pip3 install python3-xlib && sudo apt-get install scrot && sudo apt-get install python3-tk && 
            sudo apt-get install python3-dev && pip3 install pyautogui

"""

import pyautogui #
import time

pyautogui.position() #point your cursor at the button
# {Coordinate} will be appear

i = 0
while 1 <25:
    pyautogui.click(x=1062, y=733) #Insert the {Coordinate} in the bracket.
    time.sleep(0.2)
    i +=1