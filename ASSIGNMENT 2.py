##Task 1: Check if a Number is Even or Odd

Number=int(input('Enter the number:'))
if Number % 2 == 0:
    print(f'{Number} is even')
else:    
    print(f'{Number} is odd')


##Task 2: Sum of Integers from 1 to 50 Using a Loop

print()
print()
total_sum = 0

for i in range (1,51):
    ##print(i)
   total_sum += i

print("The sum of numbers from 1 to 50 is:", total_sum)  