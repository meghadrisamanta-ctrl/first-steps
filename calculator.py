a=int(input("enter number a:"))
b=int(input("enter number b:"))
c=input("enter oprrator:")
if c=="+":
    print(a+b)
elif c=="-":
    print(a-b)
elif c=="*":
    print(a*b)
elif c=="/":
    if b==0:
        print("division with zero is not allowed")
    else:
        print(a/b)
else:
    print("invalid operator")
