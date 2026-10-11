"""
=====================================================================
 DICE ROLLING SIMULATOR  -  LEVEL 4  (FINAL COMPLETE UTILITY)
 Module 4 : NumPy and Pandas
 Module 5 : File Handling and Object Oriented Programming
---------------------------------------------------------------------
 Name : Bhavesh Vishveshwar Kawadkar | USN : CD25077 | CSE-DS (B)
---------------------------------------------------------------------
 AIM : To build the complete, industry-style Dice Rolling Simulator
       that stores every roll permanently in a CSV file, and analyses
       the collected data using NumPy and Pandas.

 CONCEPTS USED :
   Module 4 -> numpy array, mean, median, std, unique, bincount,
               pandas DataFrame, value_counts, groupby, describe,
               read_csv, to_csv
   Module 5 -> class, object, __init__, methods, inheritance,
               encapsulation, __str__, file open / read / write,
               with-statement, os module
   (all earlier modules are re-used : loops, data structures,
    functions and exception handling)

 REQUIREMENT : pip install numpy pandas
=====================================================================
"""

import os
import random
from datetime import datetime

import numpy as np
import pandas as pd

DATA_FILE = "roll_history.csv"


# =================== 1. OBJECT ORIENTED PROGRAMMING =================

class Dice:
    """A single die. Base class."""

    def __init__(self, sides=6):
        self.sides = sides            # instance variable
        self.last_value = None

    def roll(self):
        """Roll this die once and remember the value."""
        self.last_value = random.randint(1, self.sides)
        return self.last_value

    def __str__(self):                # special / dunder method
        return "Dice(%d sides, last = %s)" % (self.sides, self.last_value)


class LoadedDice(Dice):
    """INHERITANCE : a biased die that favours the number 6."""

    def __init__(self, sides=6, lucky=6, bias=0.3):
        super().__init__(sides)       # call the parent constructor
        self.lucky = lucky
        self.bias = bias

    def roll(self):                   # METHOD OVERRIDING
        if random.random() < self.bias:
            self.last_value = self.lucky
        else:
            self.last_value = random.randint(1, self.sides)
        return self.last_value


class DiceGame:
    """Controls the whole session : rolling, storing and file handling."""

    def __init__(self, player, dice_count=2, loaded=False):
        self.player = player
        self.dice_count = dice_count
        self.__records = []           # ENCAPSULATION (private attribute)
        if loaded:
            self.dice = [LoadedDice() for _ in range(dice_count)]
        else:
            self.dice = [Dice() for _ in range(dice_count)]

    def play_turn(self, turn_no):
        """Roll all dice once and store the record."""
        values = [d.roll() for d in self.dice]
        record = {
            "player": self.player,
            "turn": turn_no,
            "dice_count": self.dice_count,
            "values": "-".join(str(v) for v in values),
            "total": sum(values),
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        self.__records.append(record)
        return values, record["total"]

    def get_records(self):
        """Public method to read the private records (getter)."""
        return self.__records

    # ------------------------- FILE HANDLING ------------------------
    def save_to_csv(self, filename=DATA_FILE):
        """Append this session's records to the CSV file."""
        if not self.__records:
            print(">> Nothing to save.")
            return
        new_data = pd.DataFrame(self.__records)
        if os.path.exists(filename):
            new_data.to_csv(filename, mode="a", header=False, index=False)
        else:
            new_data.to_csv(filename, index=False)
        print(">> %d records saved to %s" % (len(self.__records), filename))
        self.__records.clear()        # avoid saving the same rows twice

    def save_text_report(self, filename="session_report.txt"):
        """Plain file handling using open() and the with-statement."""
        with open(filename, "w") as f:
            f.write("DICE ROLLING SIMULATOR - SESSION REPORT\n")
            f.write("Player : %s\n" % self.player)
            f.write("Date   : %s\n\n" % datetime.now().strftime("%d-%m-%Y"))
            for r in self.__records:
                f.write("Turn %-3d : %-12s Total = %d\n"
                        % (r["turn"], r["values"], r["total"]))
        print(">> Text report written to", filename)


# ===================== 2. NUMPY ANALYSIS ============================

def numpy_analysis(values):
    """Statistical analysis of the face values using NumPy."""
    arr = np.array(values)                       # create a NumPy array

    print("\n" + " NUMPY ANALYSIS ".center(52, "="))
    print("Array shape        :", arr.shape)
    print("Total dice rolled  :", arr.size)
    print("Sum                :", np.sum(arr))
    print("Mean               :", round(float(np.mean(arr)), 3))
    print("Median             :", float(np.median(arr)))
    print("Standard deviation :", round(float(np.std(arr)), 3))
    print("Variance           :", round(float(np.var(arr)), 3))
    print("Minimum / Maximum  :", int(arr.min()), "/", int(arr.max()))

    faces, counts = np.unique(arr, return_counts=True)
    print("\nFace  Count  Expected  Deviation")
    expected = arr.size / 6
    for f, c in zip(faces, counts):
        print("%4d  %5d  %8.1f  %+9.1f" % (f, c, expected, c - expected))

    # boolean indexing - a very common NumPy operation
    print("\nHigh rolls (>=5)   :", int(arr[arr >= 5].size))
    print("Low rolls  (<=2)   :", int(arr[arr <= 2].size))
    print("=" * 52)


# ===================== 3. PANDAS ANALYSIS ===========================

def pandas_analysis(filename=DATA_FILE):
    """Read the stored CSV file and analyse it with Pandas."""
    if not os.path.exists(filename):
        print(">> No data file found. Play a few turns first.")
        return None

    df = pd.read_csv(filename)                  # READ the CSV into a DataFrame

    print("\n" + " PANDAS ANALYSIS ".center(52, "="))
    print("Rows x Columns :", df.shape)
    print("\nFirst 5 records :")
    print(df.head())

    print("\nStatistics of the 'total' column :")
    print(df["total"].describe())

    print("\nTurns played by each player (groupby) :")
    print(df.groupby("player")["total"].agg(["count", "sum", "mean", "max"]))

    print("\nMost common turn totals (value_counts) :")
    print(df["total"].value_counts().head())

    # split the 'values' string column back into individual faces
    faces = []
    for text in df["values"]:
        faces.extend(int(x) for x in str(text).split("-"))
    print("\nFrequency of each face :")
    print(pd.Series(faces).value_counts().sort_index())

    print("=" * 52)
    return faces


# ========================= 4. MAIN MENU =============================

def main():
    print(" DICE ROLLING SIMULATOR - LEVEL 4 (FINAL) ".center(52, "="))
    name = input("Enter player name : ").strip() or "Player"

    try:
        n = int(input("Number of dice (1-5) : "))
        if n < 1 or n > 5:
            raise ValueError
    except ValueError:
        print(">> Invalid value, using 2 dice.")
        n = 2

    game = DiceGame(player=name, dice_count=n)
    session_faces = []
    turn = 0

    while True:
        print("\n1. Roll   2. NumPy analysis   3. Pandas report"
              "   4. Save   5. Exit")
        choice = input("Choice : ").strip()

        if choice == "1":
            turn += 1
            values = [d.roll() for d in game.dice]
            game.get_records().append({
                "player": name, "turn": turn, "dice_count": n,
                "values": "-".join(map(str, values)),
                "total": sum(values),
                "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            })
            session_faces.extend(values)
            print("Rolled :", values, " | Total :", sum(values))

        elif choice == "2":
            if session_faces:
                numpy_analysis(session_faces)
            else:
                print(">> Roll the dice first.")

        elif choice == "3":
            pandas_analysis()

        elif choice == "4":
            game.save_to_csv()
            game.save_text_report()

        elif choice == "5":
            game.save_to_csv()
            if session_faces:
                numpy_analysis(session_faces)
            print("\nThank you for using the Dice Rolling Simulator !")
            break

        else:
            print(">> Invalid choice, please select 1 to 5.")


if __name__ == "__main__":
    main()
