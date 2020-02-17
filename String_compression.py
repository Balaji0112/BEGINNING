def String_compression(word):
    compressed_string=[]
    count=0
    word=list(word)
    for i in range(len(word)-1):
        temp=word[i]
        if(word[i]==word[i+1]):
            count+=1
        else:
            compressed_string.append(temp)
            compressed_string.append(count+1)
            count=0
    compressed_string.append(temp)
    compressed_string.append(count+1)
    return compressed_string
word=input()
Compressed_string=String_compression(word)
if(len(word)<len(Compressed_string)):
    print(word)
else:
    print(*Compressed_string,sep='')

