No_of_chars=256
def CanFormPalindrome(word):
    Count=[0]*No_of_chars
    for i in range(len(word)):
        Count[ord(word[i])]=Count[ord(word[i])]+1
    odd=0
    for j in range(0,No_of_chars):
        if(Count[j]&1):
            odd=odd+1
        if(odd>1):
            return False
    return True
word=input()
if(CanFormPalindrome(word)):
    print('Yes we can form palindrome with a given word')
else:
    print('No we cannot form a palindrome with a given word')
    