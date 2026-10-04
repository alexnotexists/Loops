def multiplication():
    n=int(input("Enter a number of whose you wanna see multiplication table of : "))
    for i in range(1,11):
        if(i!=3):
            print(f"{n}*{i}={n*i}")
multiplication()