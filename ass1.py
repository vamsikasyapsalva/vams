sv=int(input("enter the starting value:"))
ev=int(input("enter the end value:"))
def eve(sv,ev):
    if(sv%2==0):
        for i in range(sv,ev,2):
            if(i%5==0 and i%3==0):
                print(i)
    else:
        for i in range(sv+1,ev,2):
            if(i%5==0 and i%3==0):
                print(i)
eve(sv,ev)
