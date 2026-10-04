def listcheck():
    item=["red","blue","green","red","yellow","blue"]
    dup=[]
    for i in range(len(item)):
        for j in range(i+1,len(item)):
            if item[i]==item[j]:
                dup.append(item[i])
    return dup
duplicate=listcheck()
print(duplicate)