def IsUnique(word):
    Checker=0
    for i in range(len(word)):
        Index=ord(word[i])-ord('a')
        if (Checker & (1<<Index)) >0:
            return False
        Checker=Checker|(1<<Index)
    return True
word=input()
if(IsUnique(word)):
    print(word+' has all the characters as unique')
else:
    print(word+' has some repeated letters')