def IsSubstring(word1,word2):
    length=len(word1)
    temp=[0]*length
    for i in range(length):
        j=i
        k=0
        while(j<len(word1)):
            temp[k]=word1[j]
            k+=1
            j+=1
        j=0
        while(j<i):
            temp[k]=word1[j]
            j+=1
            k+=1
        s=''.join(temp)
        if word2 == s:
           return True
    return False
word1,word2=input().split()
Solution=IsSubstring(word1,word2)
if(Solution):
    print('yes word1 is a substring of word2')
else:
    print('no word1 is not a substring of word2')


