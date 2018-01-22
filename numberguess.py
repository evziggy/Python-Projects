import random
def main():
    """Inputs the bounds of the range of numbers
    and lets the user guess the computer’s number until
    the guess is correct."""

    small = int(input("Enter the smaller number in the range:  "))
    large = int(input("Enter the larger number in the range: "))
    print("Think of a number between ", small, "and", large)
    
    play = input("Hit enter to continue...")
    guess = (large+small)//2
    print("I'm trying to guess your number. I know it is between", small, "and", large,
                  "Is your number", guess, "?")
    
    count = 0
    while True:
        count += 1
        user = input("\n Enter =, <, or >:")
        if user == "<":
            large = guess
            guess = (large+small)//2
            print("I'm trying to guess your number. I know it is between", small, "and", large,
                  "Is your number", guess, "?")
            
        elif user == '>':
            small = guess
            guess = (large+small)//2
            print("I'm trying to guess your number. I know it is between", small, "and", large,
                  "Is your number", guess, "?")
            
        elif user == '=':
            print("Hooray, I got it in", count, "tries!")
            break

if __name__ == "__main__":
    main()
