def compare(string1, string2):
    list1 = list(string1)
    list2 = list(string2)
    if len(list1) != len(list2):
        return False
    else:
        for i in range(len(list1)):
            if list1[i] != list2[i]:
                return False
                break
    return True
print(compare('Hello', "hello"))