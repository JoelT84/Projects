def get_guess():
    guess = int(input("What is your guess? (1-10): "))
    return guess 

def main():
    guess = get_guess()
    if guess == 8:
        print("Correct!")
    else:
        print("Incorrect!")
    

main()




