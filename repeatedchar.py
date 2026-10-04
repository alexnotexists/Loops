def repchar():
    char=input("Enter characters : ")
    for i in range(len(char)):
        for j in range(i+1,len(str)):
            if char[i]==char[j]:
                print(char[i])
repchar