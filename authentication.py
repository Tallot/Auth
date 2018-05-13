from keyboard_handling import gather_data
from auth_math import *
import os.path
import pickle
from pprint import pprint

if os.path.isfile('./standard'):
    mode = 'auth'
else: 
    mode = 'add'
    
if mode == 'add':
    eval, pressed_intervals, unpressed_intevals = gather_data()
    while not eval:
        pprint(pressed_intervals)
        pprint(unpressed_intevals)
        print('No no no (TheFatRat)')
        eval, pressed_intervals, unpressed_intevals = gather_data()
    
    pprint(pressed_intervals)
    pprint(unpressed_intevals)
    
    intervals_filter(pressed_intervals)
    intervals_filter(unpressed_intevals)
    
    pprint(pressed_intervals)
    pprint(unpressed_intevals)
    
    with open('standard', 'wb') as fs:
        pickle.dump([pressed_intervals, unpressed_intevals], fs)
        
else:
    with open('standard', 'rb') as fs:
        standard = pickle.load(fs)
        
    pprint(standard)
        
    eval, y_pressed_intervals, y_unpressed_intervals = gather_data()
    while not eval:
        print('No no no (TheFatRat)')
        eval, y_pressed_intervals, y_unpressed_intervals = gather_data()
    
    r = 0   
    for i in range(K_e):
        if hyphothesis_check(y_pressed_intervals, standard[0]):
            r+=1
        else:
            pass
        
    for i in range(K_e):
        if hyphothesis_check(y_unpressed_intervals, standard[1]):
            r+=1
        else:
            pass
            
    P = r/(2*K_e)
    if P > 0.5:
        print('You have passed')
    else:
        print('Fuck off')