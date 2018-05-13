from pynput.keyboard import Key, Listener
import time
from pprint import pprint

press_times = []
release_times = [] 


def on_press(key):
    press = time.time()
    press_times.append(press)
    #print('{0} pressed'.format(
        #key))

def on_release(key):
    release = time.time()
    release_times.append(release)
    #print('{0} release'.format(
        #key))
    if key == Key.esc:
        # Stop listener
        return False

def get_intervals(press_times, release_times):
    #sometimes press and release timestamps are written in incorrect order 
    press_times = sorted(press_times[:-1])
    release_times = sorted(release_times[:-1])
    pressed_intervals = [release_times[i] - press_times[i] for i in range(len(press_times))]
    unpressed_intevals = [press_times[i+1] - release_times[i] for i in range(len(press_times)-1)]
    return pressed_intervals, unpressed_intevals

def gather_data():
    # Collect events until released
    with Listener(
        on_press=on_press,
        on_release=on_release) as listener:
        listener.join()
    
    pressed_intervals, unpressed_intevals = get_intervals(press_times, release_times)
    
    #pprint(pressed_intervals)
    #pprint(unpressed_intevals)
    
    for i in unpressed_intevals:
        if i < 0.0:
            return False
    
    return True
    
if __name__=='__main__':
    eval = gather_data()
    if eval:
        print('OK!')
    else: 
        print('No no no (TheFatRat)')

