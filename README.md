# Python-Exp.-Learning
Building an project for making Dice Simulator using Python for an Python Experential Learning Project
# Dice Rolling Simulator — Python Experiential Learning Utility

**Name:** Bhavesh Vishveshwar Kawadkar  
**USN:** CD25077  
**Branch / Section:** CSE-DS (B), Semester III  
**Course:** Python Programming Lab (N-PCCCD304P)  
**Institute:** S. B. Jain Institute of Technology, Management & Research, Nagpur  
**Course Coordinator:** Ms. Ashwini Yerlekar

---

## 1. Utility Overview

A Dice Rolling Simulator built in Python that mimics the rolling of one or more
standard six-sided dice. The program generates random values between 1 and 6,
lets the user roll repeatedly, shows the outcome of every roll, keeps a complete
history of previous rolls, and finally analyses that history statistically.

The utility has been developed in **four levels**, so that each level maps
directly onto one module of the Python Programming Lab syllabus and grows from a
very basic program into a complete, industry-style application.

---

## 2. Level-wise Development Plan

| Level | Syllabus Module | What is added at this level | File |
|---|---|---|---|
| **Level 1** | Module 1 — Fundamentals & Control Structures | Basic dice roll using `random`, user input, `if/elif/else`, `while` and `for` loops, `break`/`continue`, running score and summary | `level1_module1/dice_level1.py` |
| **Level 2** | Module 2 — Data Structures | Roll history in a **list**, each roll stored as a **tuple**, frequency count in a **dictionary**, unique faces in a **set**, string formatting and slicing, menu-driven design | `level2_module2/dice_level2.py` |
| **Level 3** | Module 3 — Functions | Complete modular rewrite — user-defined functions, default and keyword arguments, multiple return values, `*args`, `lambda`, `map()`, `filter()`, recursion, and full **exception handling** (`try/except/else/finally`, `raise`) | `level3_module3/dice_level3.py` |
| **Level 4** | Module 4 — NumPy & Pandas (+ Module 5 — File Handling & OOP) | `Dice`, `LoadedDice` and `DiceGame` **classes** with inheritance and encapsulation, permanent storage in a **CSV file**, statistical analysis with **NumPy**, and reporting with **Pandas** | `level4_module4/dice_level4.py` |

Every level is a complete, runnable program on its own. Level 4 is the final
submitted utility.

---

## 3. Installation and Execution

**Requirements:** Python 3.8 or above.

```bash
# clone the repository
git clone https://github.com/<your-username>/dice-rolling-simulator.git
cd dice-rolling-simulator

# Levels 1 to 3 need no external library
python level1_module1/dice_level1.py
python level2_module2/dice_level2.py
python level3_module3/dice_level3.py

# Level 4 needs NumPy and Pandas
pip install numpy pandas
python level4_module4/dice_level4.py
```

---

## 4. Summary of the Logic Used

1. **Random generation** — `random.randint(1, 6)` (and `random.choice()` in
   Level 2) produces a uniformly distributed face value for each die.
2. **Input validation** — every value typed by the user is checked before it is
   used. Levels 1–2 use `isdigit()` and range checks; Level 3 onward wraps the
   conversion in `try / except ValueError` and re-prompts until the input is
   valid, so the program can never crash on bad input.
3. **Control flow** — a `while` loop keeps the session alive until the user
   chooses to quit; an inner `for` loop rolls the required number of dice for
   that turn.
4. **History storage** — each turn is stored as `(turn_number, (faces...), total)`.
   A dictionary keeps a running count of how many times each face appeared, and a
   set records which faces have been seen at least once.
5. **Modularity** — from Level 3 the program is split into small single-purpose
   functions (`roll_one`, `roll_many`, `analyse`, `get_number`, `show_summary`),
   which makes the code readable, reusable and easy to test.
6. **Object model** — Level 4 models a die as a `Dice` object. `LoadedDice`
   inherits from it and overrides `roll()` to demonstrate polymorphism, while
   `DiceGame` holds the dice, the player and the private record list.
7. **Persistence** — records are appended to `roll_history.csv`, so data from
   earlier sessions is never lost, and a plain-text session report is written
   using `open()` with the `with` statement.
8. **Analysis** — NumPy computes mean, median, standard deviation, variance and
   the deviation of each face from its expected frequency (n/6), which shows
   whether the simulated die is fair. Pandas reads the CSV back and produces
   `describe()`, `groupby()` and `value_counts()` reports.

---

## 5. Repository Structure

```
dice-rolling-simulator/
├── README.md
├── level1_module1/dice_level1.py
├── level2_module2/dice_level2.py
├── level3_module3/dice_level3.py
├── level4_module4/dice_level4.py
└── Consolidated_Report.pdf
```

---

## 6. Assessment Mapping

| Assessment | Week | Deliverable from this repository |
|---|---|---|
| Utility Assessment-I | Week 4 | Level 1 working, repo initialised, first commits, README started |
| Utility Assessment-II | Week 8 | Levels 2 and 3 complete, feature branches merged, meaningful commit history |
| Utility Assessment-III | Week 12 | Level 4 complete, tested, README finalised, final demonstration |
| Utility Report | — | `Consolidated_Report.pdf` uploaded to this repository |
