i = int(input())
j = int(input())
for n in range(i,j+1):
    
    i = 2
    f = True
    
    while(i<= n//2):
        if(n%i==0):
            f = False
            break
        i+=1

    if(f == True):
        print(n,"Prime")
