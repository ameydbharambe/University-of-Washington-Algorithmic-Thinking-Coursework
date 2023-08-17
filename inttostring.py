string1 = ""
n = 0

while n//10 > 0: #if we don't check the loop goes infinite
    digit = n%10 #use mod to find digit and convert to string
    if digit == 0:
        string1 = string1 + "0" #I took not using string function extremely seriously
    elif digit == 1:
        string1 = string1 + "1"
    elif digit == 2:
        string1 = string1 + "2"
    elif digit == 3:
        string1 = string1 + "3"
    elif digit == 4:
        string1 = string1 + "4"
    elif digit == 5:
        string1 = string1 + "5"
    elif digit == 6:
        string1 = string1 + "6"
    elif digit == 7:
        string1 = string1 + "7"
    elif digit == 8:
        string1 = string1 + "8"
    else:
        string1 = string1 + "9"
    n = n//10
if n//10 == 0: #case for leftmost digit
        digit = n%10
        if digit == 0:
            string1 = string1 + "0"
        elif digit == 1:
            string1 = string1 + "1"
        elif digit == 2:
            string1 = string1 + "2"
        elif digit == 3:
            string1 = string1 + "3"
        elif digit == 4:
            string1 = string1 + "4"
        elif digit == 5:
            string1 = string1 + "5"
        elif digit == 6:
            string1 = string1 + "6"
        elif digit == 7:
            string1 = string1 + "7"
        elif digit == 8:
            string1 = string1 + "8"
        else:
            string1 = string1 + "9"
print(string1[::-1]) #got output reverse so reversed string