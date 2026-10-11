"""
=====================================================================
 DICE ROLLING SIMULATOR  -  LEVEL 1
 Module 1 : Fundamentals of Python Programming / Control Structures
---------------------------------------------------------------------
 Name   : Bhavesh Vishveshwar Kawadkar
 USN    : CD25077
 Branch : CSE-DS (B)
 Course : Python Programming Lab (N-PCCCD304P)
---------------------------------------------------------------------
 AIM : To simulate the rolling of a standard six-sided die using
       Python's random module, and to allow the user to roll the
       dice repeatedly until he/she chooses to stop.

 CONCEPTS USED (Module 1 only) :
   - Variables and data types (int, str, bool)
   - Input / output statements
   - The random module (randint)
   - Arithmetic and relational operators
   - Decision making  : if / elif / else
   - Looping          : while loop, for loop
   - Loop control     : break, continue
=====================================================================
"""

import random          # built-in module used to generate random numbers

# ------------------------- CONSTANTS --------------------------------
MIN_FACE = 1           # smallest number on a die
MAX_FACE = 6           # largest number on a die


# ------------------------- 1. WELCOME -------------------------------
print("=" * 55)
print("        DICE ROLLING SIMULATOR  -  LEVEL 1")
print("=" * 55)
print("This program simulates rolling a standard six-sided die.")
print()

player_name = input("Enter your name : ")

if player_name == "":                 # decision making
    player_name = "Player"

print("Welcome,", player_name, "! Let us start rolling.")
print("-" * 55)


# ------------------------- 2. MAIN GAME LOOP ------------------------
total_rolls = 0        # counter variable
total_score = 0        # accumulator variable
highest = 0            # to store the maximum value rolled
sixes = 0              # how many times a 6 appeared

playing = True         # boolean flag that controls the while loop

while playing:                                     # WHILE LOOP

    # ---- how many dice does the user want to roll this turn? ----
    count = input("How many dice do you want to roll (1-5)? ")

    # ---- simple validation using decision making ----
    if count.isdigit() == False:
        print(">> Please type a NUMBER only. Try again.")
        continue                                   # CONTINUE statement

    count = int(count)                             # type conversion

    if count < 1 or count > 5:
        print(">> Value must be between 1 and 5. Try again.")
        continue

    # ---- roll the dice 'count' times ----
    turn_total = 0
    print()
    for i in range(1, count + 1):                  # FOR LOOP
        value = random.randint(MIN_FACE, MAX_FACE)  # random number 1-6
        turn_total = turn_total + value
        total_rolls = total_rolls + 1
        total_score = total_score + value

        if value > highest:                        # find the maximum
            highest = value

        if value == 6:                             # count the sixes
            sixes = sixes + 1

        print("  Dice", i, ":", value)

    print("  ---------------------")
    print("  Turn Total :", turn_total)

    # ---- give a message according to the score (if / elif / else) ----
    if turn_total >= 5 * count:
        print("  Result : EXCELLENT ROLL !")
    elif turn_total >= 3 * count:
        print("  Result : Good roll.")
    else:
        print("  Result : Better luck next time.")
    print()

    # ---- ask the user whether to continue ----
    again = input("Roll again? (y / n) : ")
    print("-" * 55)

    if again == "n" or again == "N":
        playing = False                            # stop the while loop
        break                                      # BREAK statement


# ------------------------- 3. FINAL SUMMARY -------------------------
print()
print("=" * 55)
print("                 SESSION SUMMARY")
print("=" * 55)
print("Player Name        :", player_name)
print("Total Dice Rolled  :", total_rolls)
print("Total Score        :", total_score)

if total_rolls > 0:
    average = total_score / total_rolls            # arithmetic operator
    print("Highest Face       :", highest)
    print("Number of Sixes    :", sixes)
    print("Average per Roll   :", round(average, 2))
else:
    print("You did not roll any dice.")

print("=" * 55)
print("Thank you for playing,", player_name, "!")
