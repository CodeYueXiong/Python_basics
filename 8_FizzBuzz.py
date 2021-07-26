# task: print from 1 to 20, and for multiples of 3 print "Fizz", 5 print "Buzz", both print "FizzBuzz"
for i in range(1, 21):
    if i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 15 == 0:
        print("FizzBuzz")
    else:
        print(i)