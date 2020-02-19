

# generate random integer values
from random import seed
from random import randint
# seed random number generator
seed()
# generate some integers

value = randint(0, 10)
#print(value)
guess = input ("guess a number zero through ten \n")
print(guess)
#print(type(value))
#print(type(guess))
def string_integer ():
    print(guess)
    integer_guess = int(guess)
    return integer_guess
integer_guess = string_integer ()


while integer_guess != value:
    print("incorrect, try again")
    guess = input ("guess a number zero through ten \n")
    integer_guess = string_integer ()

print("correct!")
print("good game!")

