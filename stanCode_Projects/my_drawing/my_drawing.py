"""
File: my_drawing.py
Name: 賴珈汶
----------------------
TODO: This file uses campy module to draw on a GWindow object.
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GLabel, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    TODO: Use campy to draw a figure on GWindow.
    喜歡多拉A夢，所以就畫出來了!
    """
    window = GWindow(width=800, height=500, title="Doraemon")
    background = GRect(800, 500)
    background.filled = True
    background.fill_color = "White"
    window.add(background)
    doraemon(window)
    door(window)
    stancode(window)


def doraemon(window):
    """
    Draw a figure of Doraemon.
    """
    left_arm = GOval(100, 35, x=125, y=265)
    left_arm.filled = True
    left_arm.fill_color = "dodgerblue"
    window.add(left_arm)
    left_hand = GOval(45, 45, x=100, y=260)
    left_hand.filled = True
    left_hand.fill_color = "White"
    window.add(left_hand)
    # right_arm = GOval(100, 35, x=290, y=265)
    # right_arm.filled = True
    # right_arm.fill_color = "Blue"
    # window.add(right_arm)
    right_arm_1 = GArc(120, 100, 60, 100, x=300, y=250)
    right_arm_1.filled = True
    right_arm_1.fill_color = "dodgerblue"
    window.add(right_arm_1)
    right_arm_2 = GArc(60, 60, 160, 230, x=312, y=242)
    right_arm_2.filled = True
    right_arm_2.fill_color = "dodgerblue"
    window.add(right_arm_2)
    right_arm_3 = GArc(60, 60, 160, 230, x=310, y=240)
    right_arm_3.filled = True
    right_arm_3.fill_color = "dodgerblue"
    right_arm_3.color = "dodgerblue"
    window.add(right_arm_3)
    right_hand = GOval(45, 45, x=355, y=240)
    right_hand.filled = True
    right_hand.fill_color = "White"
    window.add(right_hand)
    finger_1 = GOval(10, 30, x=368, y=230)
    finger_1.filled = True
    finger_1.fill_color = "White"
    window.add(finger_1)
    finger_2 = GOval(10, 30, x=378, y=230)
    finger_2.filled = True
    finger_2.fill_color = "White"
    window.add(finger_2)
    finger_3 = GOval(30, 30, x=362, y=240)
    finger_3.filled = True
    finger_3.fill_color = "White"
    finger_3.color = "White"
    window.add(finger_3)
    body = GOval(170, 200, x=165, y=215)
    body.filled = True
    body.fill_color = "dodgerblue"
    window.add(body)
    belly = GOval(150, 140, x=176, y=230)
    belly.filled = True
    belly.fill_color = "White"
    window.add(belly)
    pocket = GArc(125, 220, 180, 180, x=188, y=240)
    pocket.filled = True
    pocket.fill_color = "White"
    window.add(pocket)
    left_foot = GOval(90, 40, x=160, y=395)
    left_foot.filled = True
    left_foot.fill_color = "White"
    window.add(left_foot)
    right_foot = GOval(90, 40, x=250, y=395)
    right_foot.filled = True
    right_foot.fill_color = "White"
    window.add(right_foot)
    foot_line_1 = GLine(245, 390, 255, 390)
    window.add(foot_line_1)
    foot_line_2 = GLine(250, 390, 250, 410)
    window.add(foot_line_2)
    face = GOval(200, 200, x=150, y=50)
    face.filled = True
    face.fill_color = "dodgerblue"
    window.add(face)
    inner_face = GOval(175, 175, x=162, y=75)
    inner_face.filled = True
    inner_face.fill_color = "White"
    window.add(inner_face)
    necklace = GRect(140, 12, x=178, y=236)
    necklace.filled = True
    necklace.fill_color = "Red"
    window.add(necklace)
    bell_1 = GOval(30, 30, x=236, y=235)
    bell_1.filled = True
    bell_1.fill_color = "gold"
    window.add(bell_1)
    bell_2 = GRect(30, 2.5, x=236, y=243)
    bell_2.filled = True
    bell_2.fill_color = "gold"
    window.add(bell_2)
    bell_3 = GOval(6, 6, x=248, y=250)
    bell_3.filled = True
    bell_3.fill_color = "gray"
    window.add(bell_3)
    bell_3 = GLine(251, 256, 251, 265)
    window.add(bell_3)
    left_eye = GOval(50, 70, x=200, y=55)
    left_eye.filled = True
    left_eye.fill_color = "White"
    window.add(left_eye)
    right_eye = GOval(50, 70, x=250, y=55)
    right_eye.filled = True
    right_eye.fill_color = "White"
    window.add(right_eye)
    left_eyeball = GOval(15, 20, x=230, y=80)
    left_eyeball.filled = True
    left_eyeball.fill_color = "Black"
    window.add(left_eyeball)
    right_eyeball = GOval(15, 20, x=255, y=80)
    right_eyeball.filled = True
    right_eyeball.fill_color = "Black"
    window.add(right_eyeball)
    left_eye_white = GOval(10, 10, x=233, y=88)
    left_eye_white.filled = True
    left_eye_white.fill_color = "White"
    left_eye_white.color = "White"
    window.add(left_eye_white)
    right_eye_white = GOval(10, 10, x=257, y=88)
    right_eye_white.filled = True
    right_eye_white.fill_color = "White"
    right_eye_white.color = "White"
    window.add(right_eye_white)
    nose = GOval(27, 25, x=237, y=110)
    nose.filled = True
    nose.fill_color = "red"
    window.add(nose)
    nose_light = GOval(10, 10, x=242, y=112)
    nose_light.filled = True
    nose_light.fill_color = "White"
    nose_light.color = "White"
    window.add(nose_light)
    mouth_1 = GArc(150, 225, 180, 180, x=175, y=115)
    mouth_1.filled = True
    mouth_1.fill_color = "darkred"
    window.add(mouth_1)
    tongue_1 = GArc(100, 180, 15, 150, x=200, y=180)
    tongue_1.filled = True
    tongue_1.fill_color = "orangered"
    window.add(tongue_1)
    tongue_2 = GArc(178, 178, 224, 92, x=185, y=138)
    tongue_2.filled = True
    tongue_2.fill_color = "orangered"
    tongue_2.color = "orangered"
    window.add(tongue_2)
    beard = GLine(250, 135, 250, 170)
    window.add(beard)
    beard_1 = GLine(230, 135, 180, 120)
    window.add(beard_1)
    beard_2 = GLine(230, 145, 175, 145)
    window.add(beard_2)
    beard_3 = GLine(230, 155, 180, 170)
    window.add(beard_3)
    beard_4 = GLine(270, 135, 320, 120)
    window.add(beard_4)
    beard_5 = GLine(270, 145, 325, 145)
    window.add(beard_5)
    beard_6 = GLine(270, 155, 320, 170)
    window.add(beard_6)


def door(window):
    """
    Draw a Dokodemo Door.
    """
    door_1 = GRect(250, 20, x=460, y=50)
    door_1.filled = True
    door_1.fill_color = "hotpink"
    window.add(door_1)
    door_2 = GRect(230, 330, x=470, y=70)
    door_2.filled = True
    door_2.fill_color = "hotpink"
    window.add(door_2)
    door_3 = GRect(250, 30, x=460, y=400)
    door_3.filled = True
    door_3.fill_color = "hotpink"
    window.add(door_3)
    door_4 = GRect(200, 15, x=485, y=415)
    door_4.filled = True
    door_4.fill_color = "white"
    window.add(door_4)
    door_5 = GRect(200, 300, x=485, y=80)
    door_5.filled = True
    door_5.fill_color = "white"
    window.add(door_5)
    door_6 = GRect(196, 296, x=487, y=82)
    door_6.filled = True
    door_6.fill_color = "hotpink"
    window.add(door_6)
    door_7 = GRect(198, 5, x=485, y=430)
    door_7.filled = True
    door_7.fill_color = "white"
    door_7.color = "white"
    window.add(door_7)
    horn_lock_1 = GOval(25, 25, x=488, y=220)
    horn_lock_1.filled = True
    horn_lock_1.fill_color = "lightgrey"
    window.add(horn_lock_1)
    horn_lock_2 = GOval(15, 15, x=493, y=225)
    horn_lock_2.filled = True
    horn_lock_2.fill_color = "lightgray"
    window.add(horn_lock_2)


def stancode(window):
    """
    The logo of stanCode SC101.
    """
    label = GRect(180, 80, x=495, y=100)
    label.filled = True
    label.fill_color = "White"
    window.add(label)
    label_1 = GLabel("Welcome to", x=505, y=140)
    label_1.font = "-20-bold"
    window.add(label_1)
    label_2 = GLabel("stanCode 101", x=497, y=175)
    label_2.font = "-20-bold"
    window.add(label_2)


if __name__ == '__main__':
    main()
