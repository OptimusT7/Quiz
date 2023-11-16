from example.questions import *
from calc import *
import os
import time

def print_by_char(text):
    if slow_print:
        for char in text:
            print(char, end='', flush=True)
            time.sleep(0.02 / sp_speed)
        print()
    else:
        print(text)

sp_speed = 1
slow_print = False
life_limit = 3
lives_on = True
userquit = False
response = ""
max_points = 0

for q in ques:
    if q.calc:
        q.q += "\nYou can use the calculator to help you answer this question!"

for q in ques:
    max_points += q.points

def main():
    global userquit, response, slow_print, sp_speed, life_limit, lives_on
    userquit = False
    loop = "y"
    ques_num = 1
    points = 0
    lives = 3

    print_by_char("Welcome to Trivia Challenge!")
    print_by_char("Note: Type help to see list of useful commands and settings!")

    while loop == "y":
        if lives == 0:
            print_by_char(f"Game over! You finished with {points} out of a maximum of {max_points} points. Can you do better next time?")
            break
        try:
            print_by_char(f"\nQuestion {ques_num}:\n{ques[ques_num].q}")
        except:
            if points == max_points:
                print_by_char(f"Congrats! You completed the quiz with max points!! Well done :)")
            else:
                print_by_char(f"Well done! You completed the quiz! You finished with {points} out of a maximum of {max_points} points. Will you be able to do better next time?")
            break
        else:
            response = input("> ").lower().strip()
            while response == "":
                response = input("Please enter the answer\n\n> ").lower().strip()

        answer = ""
        answer_list = []
        incorrect = False

        try:
            response = int(response)
        except:
            try:
                response = float(response)
            except:
                response = response.lower()

        if isinstance(ques[ques_num].a, int):
            answer_list = [int(ques[ques_num].a), float(ques[ques_num].a)]
        elif isinstance(ques[ques_num].a, list):
            for a in ques[ques_num].a:
                answer_list.append(a.lower())
        else:
            answer = ques[ques_num].a.lower()

        # if answer is in list or int form
        if answer_list:
            if response in answer_list:
                if ques[ques_num].points == 1:
                    print_by_char(f"Correct! You won 1 point.")
                else:
                    print_by_char(f"Correct! You won {ques[ques_num].points} points.")
                points += ques[ques_num].points
                ques_num += 1
            else:
                incorrect = True

        # if answer is in string form
        elif answer:
            if response == answer:
                if ques[ques_num].points == 1:
                    print_by_char(f"Correct! You won 1 point.")
                else:
                    print_by_char(f"Correct! You won {ques[ques_num].points} points.")
                points += ques[ques_num].points
                ques_num += 1
            else:
                incorrect = True

        # help
        if response == 'help':
            print_by_char("""
Giving Answers:
    To answer the question, just type the answer!
    Notes when answering:
        If answer is a number, round to two decimal places when necessary, and always use digits over spelling (e.g. 1 instead of one)
        Capitalisation doesn't matter

Some possible commands:
    help - displays this screen :)
    hint - displays a hint
    calc - run a basic calculator
        (Note that you can only use the calculator for questions that allow it.)
    restart - restart the game
    quit - exit the game

Settings:
    lives - turn on/off lives, or change number of lives
    slowprint - turn slow print on/off, or change speed
""")
            incorrect = False

        # hint
        elif response == 'hint':
            print_by_char(ques[ques_num].hint)
            incorrect = False

        # calc
        elif response == 'calc':
            if ques[ques_num].calc:
                calculator()

            else:
                print_by_char("You can't use a calculator for this question!")
            incorrect = False

        # restart
        elif response == 'restart':
            print_by_char(
                "Are you really sure you want to restart the quiz? You will lose all your current progress (y/n)")  # Does not work if not running code from terminal/python!!
            response = input("> ").lower()
            while response not in ('y', 'n'):
                response = input("Please answer using y or n\n\n> ").lower()
            if response == "y":
                os.system('cls||clear')
                main()
            incorrect = False

        # quit
        elif response == 'quit':
            print_by_char(
                "Are you really sure you want to quit? You will not be able to continue on from current progress next time (y/n)")
            response = input("> ").lower()
            while response not in ('y', 'n'):
                response = input("Please answer using y or n\n\n> ").lower()
            if response == "y":
                userquit = True
                if points == 1:
                    print_by_char(f"\nCongrats! You finished with 1 point. Well done!")
                else:
                    print_by_char(f"\nCongrats! You finished with {points} points. Well done!")
                break
            incorrect = False

        elif response == 'slowprint':
            sp_response = input("Enter the speed you wish (default = 1), or on/off: ")
            try:
                float(sp_response)
            except:
                if sp_response == "off":
                    slow_print = False
                    print_by_char("Slow print turned off")
                elif sp_response == "on":
                    slow_print = True
                    print_by_char("Slow print turned on")
                else:
                    print_by_char("I don't understand that (please use a number, or on/off).")
            else:
                if 0.1 <= float(sp_response) <= 100:
                    sp_speed = float(sp_response)
                    if not slow_print:
                        slow_print = True
                        print_by_char(f"Slow print turned on, and speed changed to {sp_speed}")
                    else:
                        print_by_char(f"Slow print speed changed to {sp_speed}")
                else:
                    print_by_char("Please use a number between 0.1 and 100")
            incorrect = False

        elif response == 'lives':
            lives_response = input("Enter amount of lives (default = 3), or on/off: ")
            try:
                int(lives_response)
            except:
                if lives_response == "off":
                    lives_on = False
                    print_by_char("Lives limit turned off")
                elif lives_response == "on":
                    lives_on = True
                    print_by_char("Life limit turned on")
                else:
                    print_by_char("I don't understand that (please use a number, or on/off).")
            else:
                if 1 <= float(lives_response) <= 100:
                    lives = int(lives_response)
                    if not lives_on:
                        lives_on = True
                        print_by_char(f"Life limit turned on, and changed to {lives}")
                    else:
                        print_by_char(f"Life limit changed to {lives}")
                else:
                    print_by_char("Please use a number between 1 and 100 (inclusive of)")
            incorrect = False

        # no valid response
        if incorrect:
            if lives_on:
                print_by_char("Incorrect! You lost a life :(")
                lives -= 1
                print_by_char(f"Lives remaining: {lives}")
            else:
                print_by_char("Incorrect!")
            ques_num += 1

    if not userquit:
        print_by_char("\nDid you want to play again? (Y/N)")  # Does not work if not running code from terminal/python!!
        response = input("> ").lower()
        while response not in ('y', 'n'):
            response = input("Please answer using y or n\n\n> ").lower()
        if response == 'y':
            print_by_char("Goodbye!")
            os.system('cls||clear')
            main()

main()

input("Press enter to close this window.")
