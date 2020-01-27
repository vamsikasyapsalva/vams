num1=int(input("enter num1 value:"))
num2=int(input("enter num2 value:"))
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def fdiv(a,b):
    return a//b
def po(a,b):
    return a**b
def mo(a,b):
    return a%b
c = add(num1,num2)
d = sub(num1,num2)
e = mul(num1,num2)
f = div(num1,num2)
g = fdiv(num1,num2)
h = po(num1,num2)
i = mo(num1,num2)
print("added value:",c)
print("subracted value:",d)
print("multiplied value:",e)
print("divided value:",f)
print("floor division value:",g)
print("powered:",h)
print("moduled value:",i)



