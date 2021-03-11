# Print all integers from 0 to 150:

for number in range(150):
    print(number)

# Print all the multiples of 5 from 5 to 1,000:

for multof5 in range(0,1000,5):
    print(multof5)

# Print integers 1 to 100. If divisible by 5, print " Coding ". instead. If divisible by 10, print " Coding Dojo ".

for int in range(100):
    if (int%5==0):
        print(" Coding ")
    else:
        print(" Coding Dojo ")

# Add odd integers from 0 to 500,000. and print the final sum.

sum=0
for num in range(0,500,000,1):
    if (num%2!=0):
        sum+=num
print(sum)

# Print positive numbers starting at 2018, counting down by fours.

for num in range(2018,0,-4):
    print(num)

# Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, 
# print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, 
# the loop should print 3, 6, 9 (on successive lines)

lowNum=2
highNum=9
mult=3
for i in range(lowNum,highNum+1):
    if(i%mult==0):
        print(i)
