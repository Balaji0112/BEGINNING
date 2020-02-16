def One_away(word1,word2):
    word1_length=len(word1)
    word2_length=len(word2)
    if(abs(word1_length-word2_length)>1):
        return False
    count=0
    word1_index=0
    word2_index=0
    while(word1_index<word1_length and word2_index<word2_length):
        if(word1[word1_index]!=word2[word2_index]):
            if(count>1):
                return False
            if word1_length<word2_length:
                word1_index+=1
            elif word2_length<word1_length:
                word2_index+=1
            else:
                word1_index+=1
                word2_index+=1
            count+=1
        else:
            word1_index+=1
            word2_index+=1
    if(word1_index<word1_length or word2_index<word2_length):
        count+=1
    return count==1
word1,word2=input().split()
if(One_away(word1,word2)):
    print('Yes they are one edit away')
else:
    print('No they have more than one edit')