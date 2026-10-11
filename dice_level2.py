"""
=====================================================================
 DICE ROLLING SIMULATOR  -  LEVEL 2
 Module 2 : Data Structures (String, List, Tuple, Set, Dictionary)
---------------------------------------------------------------------
 Name : Bhavesh Vishveshwar Kawadkar | USN : CD25077 | CSE-DS (B)
---------------------------------------------------------------------
 AIM : To extend the Level-1 simulator so that it stores a complete
       HISTORY of every roll and produces a frequency report, using
       Python's built-in data structures.

 CONCEPTS USED (Module 2) :
   - List        -> history of all rolls (ordered, changeable)
   - Tuple       -> a single roll record (immutable)
   - Set         -> the distinct faces that have appeared
   - Dictionary  -> frequency count of each face {1:.., 2:.., ...}
   - String ops  -> formatting, slicing, join(), upper(), center()
   - List slicing, len(), max(), min(), sum(), sorted()
=====================================================================
"""

import random

FACES = (1, 2, 3, 4, 5, 6)          # TUPLE - fixed faces of a die

history = []                        # LIST  - stores every roll record
frequency = {1: 0, 2: 0, 3: 0,      # DICTIONARY - face : how many times
             4: 0, 5: 0, 6: 0}
seen_faces = set()                  # SET   - unique faces seen so far


def show_history():
    """Print the full roll history stored in the list."""
    print("\n" + " ROLL HISTORY ".center(50, "="))
    if len(history) == 0:
        print("No rolls recorded yet.")
    else:
        for record in history:                 # record is a TUPLE
            turn, values, total = record
            values_text = " + ".join(str(v) for v in values)   # STRING join
            print("Turn %-3d : %-20s = %d" % (turn, values_text, total))
    print("=" * 50)


def show_report():
    """Print the frequency table, the set of faces and basic statistics."""
    print("\n" + " FREQUENCY REPORT ".center(50, "="))

    all_values = []
    for record in history:
        all_values = all_values + list(record[1])   # flatten the list

    if len(all_values) == 0:
        print("Nothing to report.")
        print("=" * 50)
        return

    for face in FACES:                              # loop over the TUPLE
        count = frequency[face]                     # DICTIONARY lookup
        percent = (count / len(all_values)) * 100
        bar = "*" * count                           # STRING repetition
        print("Face %d : %-3d (%5.1f%%) %s" % (face, count, percent, bar))

    print("-" * 50)
    print("Total dice rolled :", len(all_values))
    print("Sum of all faces  :", sum(all_values))
    print("Highest / Lowest  :", max(all_values), "/", min(all_values))
    print("Average value     :", round(sum(all_values) / len(all_values), 2))
    print("Faces seen (set)  :", sorted(seen_faces))
    print("Faces not yet seen:", sorted(set(FACES) - seen_faces))  # SET difference

    # find the face(s) with the highest frequency
    best = max(frequency, key=frequency.get)
    print("Most frequent face:", best, "(", frequency[best], "times )")
    print("=" * 50)


# --------------------------- MAIN PROGRAM ---------------------------
print(" DICE ROLLING SIMULATOR - LEVEL 2 ".center(50, "="))

turn_number = 0
running = True

while running:
    print("\nMENU : [R]oll   [H]istory   [F]requency Report   [Q]uit")
    choice = input("Enter your choice : ").strip().upper()   # STRING methods

    if choice == "R":
        n = input("Number of dice (1-5) : ").strip()
        if not n.isdigit() or int(n) < 1 or int(n) > 5:
            print(">> Invalid number. Please enter 1 to 5.")
            continue

        n = int(n)
        turn_number = turn_number + 1

        rolled = []                                   # LIST for this turn
        for i in range(n):
            value = random.choice(FACES)              # pick from the TUPLE
            rolled.append(value)                      # list method
            frequency[value] = frequency[value] + 1   # update DICTIONARY
            seen_faces.add(value)                     # update SET

        total = sum(rolled)
        record = (turn_number, tuple(rolled), total)  # create a TUPLE
        history.append(record)                        # store in the LIST

        print("You rolled :", rolled, " -> Total =", total)

    elif choice == "H":
        show_history()

    elif choice == "F":
        show_report()

    elif choice == "Q":
        running = False

    else:
        print(">> Invalid choice. Please select R, H, F or Q.")

# ---------------------------- CLOSING -------------------------------
show_report()
print("\nLast 3 turns :", history[-3:])     # LIST SLICING
print("Thank you for using the Dice Rolling Simulator.")
