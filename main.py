import random


def main():
    play = "y"

    while play == "y":
        toss = random.randint(0, 1)
        if toss == 0:
            
            print("Heads!")
        elif toss == 1:
            print("Tails!")
        else:
            print("Error: exception caught")

        question = input('Play again? ("y" for yes, "n" for no)\n')

        if question.lower() == "y":
            play = "y"
        else:
            play = "n"


if __name__ == '__main__':
    main()
