from collections import deque
stack = deque() #create stack
def Push(N):
    stack.append(N)
Push(5)
Push(3)
Push(2)
Push(9)
print("Was last pushed " + str(stack[len(stack)-1]))
N = len(stack)
for i in range(N):
    print("Popped" + str(stack[N-i-1]))
    stack.pop()
