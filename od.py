sv=int(input("enter the starting value:"))
ev=int(input("enter the end value:"))
def od(sv,ev):
    if(sv%2!=0):
        for i in range(sv,ev,2):
            print(i)
    else:
        for i in range(sv+1,ev,2):
            print(i)
od(sv,ev)
