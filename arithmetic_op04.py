#Create a variable called 'number' and assign it the three-digit number.

#Find the 'number' first digit and assign to x1.

#Find the 'number' second digit and assign to x2.

#Find the 'number' third digit and assign to x3.

#Create a variable called 'answer' and assign it the sum of the three digits.

#print the sum of the three digits.

number=479

x1=number%10

x2=number%100//10

x3=number//100

answer=x1+x2+x3

print(answer)