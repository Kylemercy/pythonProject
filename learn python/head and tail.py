# head and tail
import random
choice = input('head or tail! choose. ').lower()
txt =  random.randint(0,2)
if txt == 0 :
    print('its a tail')
else:
    print('its a head')
