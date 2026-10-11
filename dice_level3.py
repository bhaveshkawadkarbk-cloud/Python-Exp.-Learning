"""
=====================================================================
 DICE ROLLING SIMULATOR  -  LEVEL 3
 Module 3 : Functions (+ Exception Handling)
---------------------------------------------------------------------
 Name : Bhavesh Vishveshwar Kawadkar | USN : CD25077 | CSE-DS (B)
---------------------------------------------------------------------
 AIM : To re-design the simulator in a fully MODULAR form, where every
       task is performed by a separate function, and all user input is
       protected using exception handling.

 CONCEPTS USED (Module 3) :
   - User defined functions, docstrings
   - Parameters, default arguments, keyword arguments
   - Return values and multiple return values
   - Variable length arguments (*args)
   - Lambda function, map(), filter()
   - Recursive function
   - Local vs global scope
   - Exception handling : try / except / else / finally, raise
=====================================================================
"""

import random

FACES = (1, 2, 3, 4, 5, 6)


# ==================== 1. CORE DICE FUNCTIONS ========================

def roll_one(sides=6):
    """Roll a single die and return the face value. Default = 6 sides."""
    return random.randint(1, sides)


def roll_many(count=1, sides=6):
    """Roll 'count' dice and return a LIST of the results."""
    if count <= 0:
        raise ValueError("Number of dice must be at least 1.")   # RAISE
    return [roll_one(sides) for _ in range(count)]


def score(*values):
    """Variable length argument (*args) - returns the sum of any dice given."""
    return sum(values)


def analyse(rolls):
    """Return MULTIPLE VALUES : total, highest, lowest and average."""
    total = sum(rolls)
    return total, max(rolls), min(rolls), round(total / len(rolls), 2)


# ==================== 2. SAFE INPUT FUNCTIONS =======================

def get_number(message, low=1, high=5):
    """Keep asking until the user types a valid integer in range.
       Demonstrates try / except / else / finally."""
    while True:
        try:
            value = int(input(message))
            if value < low or value > high:
                raise ValueError                       # RAISE our own error
        except ValueError:
            print(">> Error : please enter a whole number between",
                  low, "and", high, ".")
        except KeyboardInterrupt:
            print("\n>> Input cancelled by user.")
            return low
        else:
            return value                               # runs if no error
        finally:
            pass                                       # always executes


# ==================== 3. REPORTING FUNCTIONS ========================

def frequency_table(all_rolls):
    """Build and return a dictionary of face : count."""
    table = {}
    for face in FACES:
        table[face] = all_rolls.count(face)
    return table


def show_summary(all_rolls):
    """Print the statistics using lambda, map and filter."""
    print("\n" + " SUMMARY ".center(48, "="))

    if not all_rolls:
        print("No dice were rolled.")
        print("=" * 48)
        return

    total, high, low, avg = analyse(all_rolls)         # unpack return values

    print("Dice rolled   :", len(all_rolls))
    print("Total score   :", total)
    print("Highest / Low :", high, "/", low)
    print("Average       :", avg)

    # LAMBDA + FILTER : keep only the even faces
    is_even = lambda x: x % 2 == 0
    evens = list(filter(is_even, all_rolls))
    print("Even faces    :", len(evens), "of", len(all_rolls))

    # LAMBDA + MAP : double every face value
    doubled = list(map(lambda x: x * 2, all_rolls[:5]))
    print("First 5 x 2   :", doubled)

    print("-" * 48)
    for face, count in frequency_table(all_rolls).items():
        print("  Face", face, ":", "#" * count, count)
    print("=" * 48)


def countdown(n):
    """RECURSIVE function used as a small roll animation."""
    if n == 0:
        print("Rolling...")
        return
    print(n, "...")
    countdown(n - 1)


# ==================== 4. MAIN CONTROLLER ============================

def main():
    """Main driver function of the program."""
    all_rolls = []                        # local variable
    print(" DICE ROLLING SIMULATOR - LEVEL 3 ".center(48, "="))

    while True:
        print("\n1. Roll dice   2. Summary   3. Exit")
        choice = get_number("Choose an option (1-3) : ", 1, 3)

        if choice == 1:
            n = get_number("How many dice (1-5) ? : ", 1, 5)
            countdown(3)
            try:
                result = roll_many(count=n)            # keyword argument
            except ValueError as err:
                print(">> Error :", err)
                continue
            all_rolls.extend(result)
            print("Result :", result, " | Turn score :", score(*result))

        elif choice == 2:
            show_summary(all_rolls)

        else:
            show_summary(all_rolls)
            print("Program ended. Thank you !")
            break


# the program starts here
if __name__ == "__main__":
    main()
