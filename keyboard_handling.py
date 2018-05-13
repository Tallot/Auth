from pynput.keyboard import Key, Listener
import time
from pprint import pprint

pressed_intervals = []
unpressed_intevals = [] 


def on_press(key):
    press = time.time()
    pressed_intervals.append(press)
    print('{0} pressed'.format(
        key))

def on_release(key):
    unpressed = time.time()
    unpressed_intevals.append(unpressed)
    print('{0} release'.format(
        key))
    if key == Key.esc:
        # Stop listener
        return False

# Collect events until released
with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()
    
pprint(pressed_intervals)
pprint(unpressed_intevals)