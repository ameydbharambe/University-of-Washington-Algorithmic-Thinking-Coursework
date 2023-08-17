class Stack: #create stack to use for RPN. If using stack in program always create this
    def __init__(self):
        self.stack = []
        self.sp = 0
    def Push(self, integer):
        self.stack.append(integer)
        self.sp += 1
    def Pop(self):
        sp1 = self.stack[self.sp-1]
        self.stack.pop()
        if len(self.stack) > 0:
            self.sp -= 1
        else:
            self.sp = 0
        return sp1
        
    def Top(self):
        return self.stack[self.sp-1]
class RPN:
    def __init__(self):
        self.stack1 = Stack()
    def process(self, string1):
        try: #check if this is possible
            self.stack1.Push(int(string1))
        except:
            if string1 == "+":
                value1 = self.stack1.Pop()
                value2 = self.stack1.Pop()
                result =  value1 + value2
            elif string1 == "-":
                value1 = self.stack1.Pop()
                value2 = self.stack1.Pop()
                result = value1 - value2
            elif string1 == '*':
                value1 = self.stack1.Pop()
                value2 = self.stack1.Pop()
                result =  value1 * value2
            elif string1 == "/":
                value1 = self.stack1.Pop()
                value2 = self.stack1.Pop()
                result = value1/value2
            else:
                result = "N/A"
            self.stack1.Push(result)
        return self.stack1.Top()
rpn = RPN()
for i in range(3):
    print(rpn.process(input()))
            
                
                
        

        
        
        