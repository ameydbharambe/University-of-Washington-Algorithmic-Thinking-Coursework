import string
url = input()
urlList = [*url]
list1 = []
sum = 0
#define base lists (group into characters used)
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
alphabetLower = list(string.ascii_lowercase)
alphabetUpper = list(string.ascii_uppercase)
for i in urlList: #check each digit in url and find representative decimal value
    if i in numbers:
        list1.append(str(i))
    elif i in alphabetUpper:
        list1.append(str(alphabetUpper.index(i)+10))
    elif i in alphabetLower:
        list1.append(str(alphabetLower.index(i)+36))
list1.reverse()
for i in list1: #sum the values up to convert to base 10
    sum = sum + (62**list1.index(i) * int(i))
print(sum)