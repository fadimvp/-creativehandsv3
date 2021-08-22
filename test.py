#!/usr/bin/python
# -*- coding: utf-8 -*-
import pyautogui as pt
from time import sleep
import pyperclip
import random

sleep(3)
position3 = pt.locateCenterOnScreen("ww.png", confidence=.6)

x = position3[0]
y = position3[1]

def get_message():
    global x, y
    position1 = pt.locateCenterOnScreen("ww.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x, y, duration=.5)
    pt.moveTo(x + 70, y - 70, duration=.5)
    pt.tripleClick()
    pt.rightClick()
    pt.moveRel(100, -200)
    pt.click()
    whatsapp_message = pyperclip.paste()
    pt.click()

    pyperclip.copy(whatsapp_message)
    print("message recived : " + whatsapp_message)
    return whatsapp_message


def post_response(message):
    global x, y
    position1 = pt.locateCenterOnScreen("whatsappv2/ww.png", confidence=.6)
    x = position1[0]
    y = position1[1]
    pt.moveTo(x + 200, y + 20, duration=.1)
    pt.click()
    pt.typewrite(message, interval=.01)
    pt.typewrite("\n", interval=.01)
    # pt.typewrite("how can I help you  ", interval=.10)
    # pt.typewrite("\n", interval=.10)
    # pt.typewrite("the job from 3:00 am to 6:00 plase wati answer   ", interval=.05)
    # pt.typewrite("\n", interval=.05)


def process_response(message):
    random_no = random.randrange(3)

    if "?" in str(message).lower():
        return " DOn't ask me any question"
    elif "welcome" in str(message).lower():
        return "bedoon essm"
    else:
        if random_no == 0:
            return "that cool"
        elif random_no == 1:
            return "remember to subscribe "
        else:
            return "i want eat something  "


# process_message= process_response(get_message())
# post_response(process_message)

def check_for_new_messages():
    pt.moveTo(x + 70, y - 70, duration=.5)

    while True:
        try:
            position = pt.locateOnScreen("whatsappv2/ff.png", confidence=.7)
            if position is not None:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(.5)
        except(Exception):
            print("no new other users with new messages located ")
        if pt.pixelMatchesColor(int(x + 70), int(y - 70), (255, 255, 255), tolerance=10):
            print("is_white")
            process_message = process_response(get_message())
            post_response(process_message)
        else:
            print("no new message yet")
        sleep(5)


check_for_new_messages()
