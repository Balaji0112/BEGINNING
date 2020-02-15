Max=1000
def URLify(sentence):
    sentence=sentence.strip()
    word_length=len(sentence)
    space_length=sentence.count(' ')
    new_length=word_length+space_length*2
    if new_length>Max:
        return -1
    index=new_length-1
    sentence=list(sentence)
    for i in range(word_length-2,new_length-2):
        sentence.append('0')
    for j in range(word_length-1,0,-1):
        if(sentence[j]==' '):
            sentence[index]='0'
            sentence[index-1]='2'
            sentence[index-2]='%'
            index-=3
        else:
            sentence[index]=sentence[j]
            index-=1
    return ''.join(sentence)
sentence=input()
URLified_sentence=URLify(sentence)
print(URLified_sentence)