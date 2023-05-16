import time

from pynput.keyboard import Key, Controller
from pynput import keyboard

time.sleep(3)

kb = Controller()

kb.press('a')
kb.release('a')

kb.press(Key.space)
kb.release(Key.space)

kb.press('b')
kb.release('b')

kb.press('c')
kb.release('c')

def pressed(e):
    print("Pressed")

def released(e):
    print("Released")

with keyboard.Listener(on_press=pressed,  on_release=released) as listener:
    listener.join()