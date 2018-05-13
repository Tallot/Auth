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
    with open('standard', 'rb') as fs:
        standard = pickle.load(fs)
        
    #pprint(standard)
    print('Enter password')
    
    r = 0   
    for i in range(K_e):
        eval, y_pressed_intervals, y_unpressed_intervals = gather_data()
        
        intervals_filter(y_pressed_intervals)
        intervals_filter(y_unpressed_intervals)
        if hyphothesis_check(y_pressed_intervals, standard[0]):
            r+=1
        else:
            pass
        
        if hyphothesis_check(y_unpressed_intervals, standard[1]):
            r+=1
        else:
            pass
            
    P = r/(2*K_e)
    print(P)
    if P >= 0.5:
        print('You have passed')
    else:
        print('Fuck off')