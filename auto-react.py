import mss
import numpy as np
import pyautogui
import keyboard
import time

REGION = {"top": 150, "left": 0, "width": 100, "height": 100}


def is_green(frame):
    r = frame[:, :, 2]
    g = frame[:, :, 1]
    b = frame[:, :, 0]

    mask = (g > 150) & (r < 120) & (b < 120)
    return np.mean(mask) > 0.25 


print("Auto-Clicker Running...")
print("Press ESC to stop.")

time.sleep(2) 

with mss.mss() as sct:
    while True:
        if keyboard.is_pressed("esc"):
            print("Stopped.")
            break

        frame = np.array(sct.grab(REGION))

        if is_green(frame):
            pyautogui.click()
            print("Clicked!")
            time.sleep(0.1)
