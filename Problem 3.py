#problem 3

x = int(input()) #input x

if x%2==0: #when x is even
    for i in range(1,(x*2)-1,2): #until i=x
        print(i,end=' ') #prints the pattern
        
else: #when x is odd
    x +=1 #covert to even
    for i in range(1,(x*2)-1,2): #until i=x
        print(i,end=' ')