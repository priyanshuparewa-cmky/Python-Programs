for i in range (10 ,0 , -1):
    print(i)
print("-------------")
for i in range(2,51):
    for num in range (2,i):
        if i % num ==0:
            break
    else:
            print(i,end = "  ")
            
              
