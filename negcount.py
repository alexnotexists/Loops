def negative():
    numbers=[]
    negcount=0
    while True:
        n=int(input("Enter numbers : "))
        numbers.append(n)
        ans=input("Do you want to continue? (yes/no)")
        if(ans=="no"):
            for number in numbers:
                    if(int(number)<0):
                        negcount+=1
            print(f"There are {negcount} negative numbers.")
            break    
negative()