from keyboard_handling import gather_data, get_intervals
from auth_math import *
import os.path
import pickle
from pprint import pprint
import os

def read_standard():
    with open('standard.txt', 'r') as fs:
        data = fs.readlines()
        data = [int(datum[:-1]) for datum in data]
        return data[::2], data[1::2]
        
def read_statistics():
    with open('statiscitc.txt', 'r') as fs:
        data = fs.readlines()
        data = [int(datum[:-1]) for datum in data]
        return data[::2], data[1::2]

if os.path.isfile('./standard.txt'):
    mode = 'auth'
else: 
    mode = 'add'
    
if mode == 'add':
    print('Enter your password(15 chars):')
    eval, pressed_intervals, unpressed_intervals = gather_data()
    
    pprint(pressed_intervals)
    pprint(unpressed_intervals)
    
    intervals_filter(pressed_intervals)
    intervals_filter(unpressed_intervals)
    
    pprint(pressed_intervals)
    pprint(unpressed_intervals)
    
    with open('standard', 'wb') as fs:
        pickle.dump([pressed_intervals, unpressed_intervals], fs)
        
else:
    standard1, standard2 = read_standard()
    #with open('standard', 'rb') as fs:
        #standard = pickle.load(fs)
        
    #pprint(standard)
    
    r = 0   
    for i in range(K_e):
        os.system('keyboard_handler.exe')
        y_pressed_intervals, y_unpressed_intervals = read_statistics()
        
        intervals_filter(y_pressed_intervals)
        intervals_filter(y_unpressed_intervals)
        if hyphothesis_check(y_pressed_intervals, standard1):
            r+=1
        else:
            pass
        
        if hyphothesis_check(y_unpressed_intervals, standard2):
            r+=1
        else:
            pass
            
    P = r/(2*K_e)
    print(P)
    if P >= 0.5:
        print('You have passed')
    else:
        print('Fuck off')