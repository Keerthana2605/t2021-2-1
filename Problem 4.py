#Problem 4

dict= {} #an empty dictionary

arr = [int(i) for i in input().split] #input in our  case [1,2,8,9,12,46,76,82,15,20,30]

count=0 #a var to count the multiples

for i in range(1,10): #multiples of numbers from 1 to 9
    for num in arr: #for each num in the input array 
        if num%i==0: #if each element is divisible by by index 1 to 9
            count +=1 # if condition is satisfied the increment count
    dict[i] = count#stores the number of divisible numbers by each index
    count = 0 #re-intialize count for each loop to move to next number

print(dict) #print the ans