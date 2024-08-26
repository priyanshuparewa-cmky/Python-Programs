a=int(input("Enter a number"))
a=0
b=1
count=0
while count< n:
    print(a, end=" ")
    a,b=b , a+b
    count +=1

print("\n--")
squares = [num**2 for num in range(1, 11)]
print(squares)
