#input imports
import msvcrt
import time
#
def timed_input(time_limit = None):
    start = time.time()
    while  time_limit == None or time.time() - start < time_limit:
        start2 = time.time()
        if msvcrt.kbhit():
            key = msvcrt.getch()
            while msvcrt.kbhit():#detect arrow keys while loop to solve decode error?
                key = msvcrt.getch()#k.decode()
            return key.decode()
    return None
class Cin:
    def __init__(self, keymap):
        self.keymap = keymap
        
    def __arrow_map(self, key):#should map to word based controlls
        if key not in list(self.keymap.keys()):
            return None
        return self.keymap[key]
    def key_grab(self, time = None):
        return(self.__arrow_map(timed_input(time)))
#
