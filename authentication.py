from auth_math import *
import os.path
import pickle
from pprint import pprint
import os


def read_standard():
    with open('standard.txt', 'r') as fs:
        data = fs.readlines()
        data = [float(datum[:-1]) for datum in data]
        return data[::2], data[1::2]
        
def read_statistics():
    with open('statistics.txt', 'r') as fs:
        data = fs.readlines()
        data = [float(datum[:-1]) for datum in data]
        return data[::2], data[1::2]

def get_intervals(press_times, release_times):
    pressed_intervals = [release_times[i] - press_times[i] for i in range(len(press_times))]
    unpressed_intevals = [press_times[i+1] - release_times[i] for i in range(len(press_times)-1)]
    return pressed_intervals, unpressed_intevals
        
def mix(pressed, unpressed):
    full_vector = []
    full_vector.append(pressed[0])
    for i in range(len(unpressed)):
        full_vector.append(unpressed[i])
        full_vector.append(pressed[i+1])
        
    return full_vector

if os.path.isfile('./standard.txt'):
    mode = 'auth'
else: 
    mode = 'add'
    
if mode == 'add':
    averaged = [0 for i in range(21)]
    for i in range(3):
        print('Enter your password(11 chars):')
        os.system('keyboard_handler.exe 1')
        
        standard1, standard2 = read_standard()
        standard1, standard2 = get_intervals(standard1, standard2)
        
        full_standard = mix(standard1, standard2)
        
        for i in range(len(averaged)):
            averaged[i] += full_standard[i]
    
    averaged = [i/3 for i in averaged]
    
    intervals_filter(averaged)    
    
    with open('etalon', 'wb') as fs:
        pickle.dump(averaged, fs)
        
else:
    with open('etalon', 'rb') as fs:
        full_standard = pickle.load(fs)
        
    #pprint(full_standard)
    
    r = 0   
    for i in range(K_e):
        os.system('keyboard_handler.exe 2')
        y_pressed_intervals, y_unpressed_intervals = read_statistics()
        y_pressed_intervals, y_unpressed_intervals = get_intervals(y_pressed_intervals, y_unpressed_intervals)
        
        
        full_auth = mix(y_pressed_intervals, y_unpressed_intervals)
        #pprint(full_auth)
        
        if hyphothesis_check(full_auth, full_standard):
            r+=1
        else:
            pass
            
    P = r/(K_e)
    print(P)
    if P >= 0.5:
        print('You have passed')
    else:
        print('No no no - TheFatRat')