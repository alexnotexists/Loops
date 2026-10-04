def reverse():
    reve=0
    n=int(input("Enter number = "))
    while n!=0:
        r=n%10
        n=n//10
        reve=reve*10+r
    return(reve)
rev=reverse()
print(rev)