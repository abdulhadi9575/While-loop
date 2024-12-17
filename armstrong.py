a=int(input("Enter a number"))
sum = 0
tem=a
while a > 0 :
    digit = a%10
    sum=sum+digit**3
    a=a//10
if tem==sum :
    print("its a armstrong number")
else :
    print("its a armstrong number")


