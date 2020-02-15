def IsPermutation(word1,word2):
    n1=len(word1)
    n2=len(word2)
    if(n1!=n2):
        return False
    str1=sorted(word1)
    str2=sorted(word2)
    word1=''.join(str1)
    word2=''.join(str2)
    for i in range(0,n1,1):
        if(word1[i]!=word2[i]):
            return False
    return True
word1,word2=input().split()
if(IsPermutation(word1,word2)):
    print(word1+' is the permutation of '+word2)
else:
    print(word1+' is not the permutation of '+word2)