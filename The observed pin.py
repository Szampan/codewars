import numpy as np
import itertools

KEYPAD = np.vstack([np.arange(1, 10).reshape(3, 3), np.array([None, 0, None])])

def get_coord(digit):
    return list(zip(np.where(KEYPAD==digit)[0], np.where(KEYPAD==digit)[1]))[0]
    
def get_adjacents(digit):
    m, n = get_coord(digit)
    adjacents = []
    if not m == 3: adjacents.append(KEYPAD[m+1, n])
    if not m == 0: adjacents.append(KEYPAD[m-1, n])
    if not n == 2: adjacents.append(KEYPAD[m, n+1])
    if not n == 0: adjacents.append(KEYPAD[m, n-1])
    return list(map(str, list(filter(lambda i: i!=None, adjacents))))

def get_pins(observed):
    possible_keys = [[str(n)] + get_adjacents(int(n)) for n in list(observed)]
    pins = itertools.product(*possible_keys)
    return list(map(lambda c: "".join(c), pins))
        

#

print(get_pins('111'))