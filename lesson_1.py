# Use else block to display a message “Done” after successful execution of for loop.
x = [3,5,6,7,8,9]
for i in x:
    print(i)
else:
    print("Done")

# Write a program to display all prime numbers within a range.
for n in range(20):
   if n > 1:
       for i in range(2,n):
           if (n % i) == 0:
               break
       else:
           print(n)
        

# Use a loop to display elements from a given list present at odd index positions.
arr= [1,7,8,4,10,13,17]
print("Element of Given array present in Odd positions:")
    
for i in range(0, len(arr), 2):    
    print(arr[i])




# Calculate the cube of all numbers from 1 to a given number.
x = [1,2,3,4,5,6,7]
for i in x:
    print(i**3)

x = [1,2,3,4,5,6,7]
y = {}
for i in x:
    key = i
    value = i**3
    y[key] = value 
print(y)