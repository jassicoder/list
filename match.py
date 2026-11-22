def match(words):
    jas=[]
    count=0
    for word in words:
        if len(word)>1 and word[0]==word[-1]:
            count+=1
            jas.append(word)
    print("matching words are:",jas)
    return count
count=match(["aba","jas","mom","roar"])
print("count of the numbers that have same words in the starting and ending is",count)
