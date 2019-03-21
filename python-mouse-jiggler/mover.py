from pyautogui import moveRel
import time


def move_hz(pixels):
    moveRel(pixels, 0)


def move_v(pixels):
    moveRel(0, pixels)


keep_running = True


def no_screensaver():
    move_hz(25)
    move_hz(-25)
    print('Mouse moved.')
    time.sleep(60)


while keep_running:
    no_screensaver()


if __name__ == '__main__':
    no_screensaver()
