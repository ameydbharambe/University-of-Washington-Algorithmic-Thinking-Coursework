import sys
sys.setrecursionlimit(20)

def stack_overflow():
    stack_overflow() #use recursion to create data keeps stacking and exceeds how much it can store

def heap_overflow():
    a = [0] * 9999999999999999999999999999 #

stack_overflow()
heap_overflow()