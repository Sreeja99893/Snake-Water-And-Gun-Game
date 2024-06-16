import random
import pyttsx3
def swg(comp, mine):
    if comp == mine:
        return None
    elif comp == 'Water' and mine == 'Snake':
        return True
    elif comp == 'Snake' and mine == 'Gun':
        return True
    elif comp == 'Gun' and mine == 'Water':
        return True
    else:
        return False


def print_results(comp, mine, win):
    print(f"~~Computer Chose {comp}, You Chose {mine}.~~")
    if win is None:
        engine = pyttsx3.init()
        engine.say("It's a Draw..!")
        engine.runAndWait()
        print("It's a draw!")
    elif win:
        engine = pyttsx3.init()
        engine.say("You won the match! 👏🏼..!")
        engine.runAndWait()
        print("You won the match! 👏🏼")
    else:
        engine = pyttsx3.init()
        engine.say("You lost the match. ☹..!")
        engine.runAndWait()
        print("You lost the match. ☹️")


def main():
    choice = ('Snake', 'Water', 'Gun')

    while True:
        comp = random.choice(choice)
        mine = input("Select what you want (Snake, Water, Gun), or type 'exit' to quit: ").strip().capitalize()

        if mine == 'Exit':
            engine = pyttsx3.init()
            engine.say("Exiting the game. Goodbye!")
            engine.runAndWait()
            print("Exiting the game. Goodbye!")
            break

        if mine not in choice:
            print("Invalid choice. Please choose again.")
            continue

        win = swg(comp, mine)

        print_results(comp, mine, win)


if __name__ == "__main__":
    main()
