number = 23
guess = int(input("Enter an integer: "))

if guess == number:
    # New block starts here
    print("Congratulations, you guessed it")
    print("(but you don't win any prize :p)")
    # New block ends here
elif guess < number:
    # Another block
    print("No, it is a little higher than that")
    # You can do whatever you want in the block....
else:
    print("No, it is a litlle lower than that")
    # You must have guessed > number to reach here

print("Done!")
# This last statement is always executed
# after the if statement is executed