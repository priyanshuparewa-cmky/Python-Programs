a=inp(input("Enter a no:"))
i=2
f=0
while(i<n//2):
    if(n%i==0):
        f=1
        break
    i+=1
    if(f==0):
    print("Not a prime no")
    else:
        print(n,"is a prime no")

