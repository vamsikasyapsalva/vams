marks=int(input("enter the marks obtained:"))
def grade(marks):
    if(marks>90):
        print("you got distinction")
    elif(marks>80 and marks<90):
        print("you got A grade")
    elif(marks>70 and marks<80):
        print("you got B grade")
    elif(marks>60 and marks<70):
        print("you got C grade")
    elif(marks>50 and marks<60):
        print("you got D grade")
    elif(marks>40 and marks<50):
        print("you got C grade")
    else:
        print("failed")
grade(marks)
