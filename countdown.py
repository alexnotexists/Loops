import time
def countdown():
    n=int(input("Start of countdown : "))
    while n!=-1:
        print(n)
        time.sleep(1)
        n=n-1
countdown()