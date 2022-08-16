# Try and Except
print('How many dogs do you have?')
numDogs = input()
try:
    if int(numDogs) >= 4:
        print("That's a lot of dogs")
    else:
        print('That is not that many dogs')
except ValueError:
    print('Please enter a number')
