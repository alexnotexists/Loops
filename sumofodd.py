def sumofodd():
    sum=0
    n=int(input("Upto How Many terms? : "))
    for i in range(1,n+1):
        if i%2==1:
            sum=sum+i
    print(sum)
sumofodd()