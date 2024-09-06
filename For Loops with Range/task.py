#range function with for loops

for number in range(1,10):
    print(number)

#change step size
for number in range(1,10,2):
    print(number)

#Gauss challenge
total = 0
for number in range (1,101):
    total += number
print(total)

#FizzBuzz Challenge (if num divisible by 3 print Fizz, if divisible by 5, print Buzz
for number in range (1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)