# FizzBuzz logic challenge
# Print 1-100
# If number is divisible by 3, print "Fizz"
# If number is divisible by 5, print "Buzz"
# If number is divisible by BOTH 3 and 5, print "FizzBuzz"

i = 0
while i < 100:
    i += 1
    if i % 3 == 0 and i % 5 == 0:
        print "FizzBuzz"
    elif i % 3 == 0:
        print "Fizz"
    elif i % 5 == 0:
        print "Buzz"
    else:
        print i