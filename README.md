# Python Lab — Lists & Loops (with Data Structures & Scope)

In this 90-minute lab, you will combine **lists**, **`for` loops**, and **`while` loops** to store multiple values and repeat actions in Python.  
If you finish the core exercises early, Part 2 introduces **tuples**, **sets**, **dictionaries**, and **variable scope** for extra practice.

By the end of this session, you will be able to:

- Store, access, slice, and build **lists**
- Use **`for` loops** with `range()` and over items in a list
- Use **`while` loops** when you do not know in advance how many times to repeat
- Refactor your **Functions Lab** Grade Calculator (`calculate_grade`) into a multi-student tracker for homework

---

## ⏱️ Lab Structure & Suggested Time Budget (90 Minutes)

| Block | Folder / Files | Suggested Time |
| --- | --- | --- |
| Setup & Functions Recap | — | ~5 min |
| **Part 1 — Lists** | `Part1_Lists_and_Loops/1_lists.py` | ~10 min |
| **Part 1 — `for` Loops** | `Part1_Lists_and_Loops/2_for_range.py`, `3_for_list.py`, `4_for_break.py` | ~30 min |
| **Part 1 — `while` Loops** | `Part1_Lists_and_Loops/5_while_pin.py`, `6_while_sum.py` | ~25 min |
| **Part 2 — Extra (Optional in Class)** | `Part2_Data_Structures_and_Scope/7_tuples.py` – `11_for_largest.py` | ~15 min |
| **Part 3 — Homework Walkthrough** | `Part3_Homework/12_homework.py` | ~5 min |

---

## 🔧 Useful Documentation

If you get stuck, refer to these beginner-friendly W3Schools guides:

- **Lists**: https://www.w3schools.com/python/python_lists.asp
- **List Indexing & Slicing**: https://www.w3schools.com/python/python_lists_access.asp
- **Add List Items (`.append()`)**: https://www.w3schools.com/python/python_lists_add.asp
- **`for` Loops**: https://www.w3schools.com/python/python_for_loops.asp
- **`while` Loops**: https://www.w3schools.com/python/python_while_loops.asp
- **Tuples & Unpacking**: https://www.w3schools.com/python/python_tuples.asp | https://www.w3schools.com/python/python_tuples_unpack.asp
- **Sets & Adding Items**: https://www.w3schools.com/python/python_sets.asp | https://www.w3schools.com/python/python_sets_add.asp
- **Dictionaries**: https://www.w3schools.com/python/python_dictionaries.asp
- **Scope & `global`**: https://www.w3schools.com/python/python_scope.asp | https://www.w3schools.com/python/python_variables_global.asp

---

## 📝 Before You Start

Make sure you remember how to:

- Define and call functions (`def`, `return`, parameters)
- Read and convert user input (`input()`, `int()`)
- Write conditionals (`if` / `elif` / `else`)
- Format strings with f-strings (`f"..."`)

---

## 🟦 Part 1 — Core: Lists, `for` & `while` Loops

> Folder: `Part1_Lists_and_Loops/`  
> **Goal:** Complete all six exercises in Part 1 during the lab.

### 📌 Concept Box — Lists

A **list** is an ordered, changeable (mutable) collection of items:

- Items have an **index** starting at `0` (e.g. `colors[0]`), and negative indices count from the end (`colors[-1]` is the last item).
- **Slicing** (`items[start:end]`) extracts a sub-list from `start` up to (but excluding) `end`.
- You can add items to the end of a list using `.append(value)`.

---

### 🟦 Exercise 1 — Lists: Create and Print Specific List Items (`Part1_Lists_and_Loops/1_lists.py`)

**Task:**  
You are given:

```python
colors = ["red", "green", "blue", "yellow", "purple"]
```

Write a function `color_info(items)` that:

- prints the first color
- prints the last color
- prints the second and third colors using slicing

Then call `color_info(colors)`.

**Sample output:**

```text
red
purple
['green', 'blue']
```

**Hints:**

1. Think of `color_info(items)` as a function receiving any list `items`.
2. Index `0` gives the first item; index `-1` gives the last item.
3. For the second and third colors, slice from index `1` up to `3` (`items[1:3]`).
4. Print each result and call `color_info(colors)` at the bottom.

**Links:** https://www.w3schools.com/python/python_lists.asp | https://www.w3schools.com/python/python_lists_access.asp

---

### 📌 Concept Box — `for` Loops

A **`for` loop** repeats a block of code a fixed number of times or once for each item in a sequence:

- `for i in range(n):` runs `n` times (`0` through `n - 1`).
- `for i in range(start, stop):` starts at `start` and stops *before* `stop`.
- `for item in my_list:` visits each element in `my_list` one by one.
- `break` exits a loop early as soon as a condition is met.

---

### 🟦 Exercise 2 — `for` Loop: Print All Numbers Below Input (`Part1_Lists_and_Loops/2_for_range.py`)

**Task:**  
Ask the user for a positive integer `n`.  
Using a **`for` loop** and `range()`, print all positive integers greater than `0` and smaller than `n`.

**Sample interaction:**

```text
Upper limit: 5
1
2
3
4
```

**Hints:**

1. Read `n` and convert it with `int()`.
2. Use `range(1, n)` so the loop starts at `1` and stops at `n - 1`.
3. Print the loop variable inside the loop.

**Link:** https://www.w3schools.com/python/python_for_loops.asp

---

### 🟦 Exercise 3 — `for` Loop + List Processing (`Part1_Lists_and_Loops/3_for_list.py`)

**Task:**  
You are given:

```python
numbers = [3, 8, 12, 7, 9, 10, 21, 30]
```

Using a **`for` loop** (no list comprehensions), go through the list, find all **even** numbers, and:

- count how many even numbers there are
- build a **new list** containing only the even numbers (using `.append()`)
- print the list of even numbers and the total count

**Sample output:**

```text
Even numbers: [8, 12, 10, 30]
Total: 4
```

**Hints:**

1. Create an empty list (`evens = []`) and a counter (`count = 0`) before the loop.
2. Loop over each `num` in `numbers`.
3. Check if `num % 2 == 0`: if so, append `num` to `evens` and increment `count` by `1`.
4. After the loop, print `evens` and `count`.

**Links:** https://www.w3schools.com/python/python_for_loops.asp | https://www.w3schools.com/python/python_lists_add.asp

---

### 🟦 Exercise 4 — `for` Loop with `break`: Stop on a Fruit (`Part1_Lists_and_Loops/4_for_break.py`)

**Task:**  
Complete the following steps:

1. Create a list called `fruits` with: `"apple"`, `"banana"`, `"cherry"`, `"orange"`.
2. Write a **`for` loop** that prints each item in `fruits`.
3. Use **`break`** to stop the loop when the item is `"cherry"` (after printing it).

**Sample output:**

```text
apple
banana
cherry
```

**Hints:**

1. Define `fruits = ["apple", "banana", "cherry", "orange"]` at the top of your code.
2. Loop with `for fruit in fruits:` and print `fruit` inside the loop.
3. Check `if fruit == "cherry":` and run `break` right after printing so `"orange"` is not printed.

**Link:** https://www.w3schools.com/python/python_for_loops.asp

---

### 📌 Concept Box — `while` Loops

A **`while` loop** repeats as long as a condition remains `True`:

- Use `while` when you **do not know in advance** how many repetitions are needed (e.g., waiting for valid input or reaching a running total).
- Always make sure something inside the loop updates the condition so the loop can eventually stop.

---

### 🟦 Exercise 5 — `while` Loop: PIN Code Attempts (`Part1_Lists_and_Loops/5_while_pin.py`)

**Task:**  
Keep asking the user for a PIN code until they type `4321`.  
For every incorrect attempt, print `"Wrong"`.  
When they finally enter `4321`, print how many attempts it took.

**Sample interaction:**

```text
PIN: 3245
Wrong
PIN: 1234
Wrong
PIN: 0000
Wrong
PIN: 4321
Correct! It took you 4 attempts
```

**Hints:**

1. Start an `attempts` counter and read the PIN in a `while` loop until it equals `"4321"` (or `4321`).
2. Print `"Wrong"` on each incorrect try and increment `attempts`.
3. After the loop finishes, print the total number of attempts.

**Link:** https://www.w3schools.com/python/python_while_loops.asp

---

### 🟦 Exercise 6 — `while` Loop: Sum Until Target (`Part1_Lists_and_Loops/6_while_sum.py`)

**Task:**  
Ask the user for a **target number**.  
Using a **`while` loop**, repeatedly ask the user for numbers and add them to a running total.  
Stop when the total **reaches or exceeds** the target, and print the final total.

**Sample interaction:**

```text
Target: 20
Number: 5
Number: 7
Number: 4
Number: 10
Total reached: 26
```

**Hints:**

1. Ask for `target` once before the loop and initialize `total = 0`.
2. Repeat `while total < target:`.
3. Inside the loop, read an integer and add it to `total`.
4. After the loop ends, print `f"Total reached: {total}"`.

**Link:** https://www.w3schools.com/python/python_while_loops.asp

---

## 🟧 Part 2 — Extra: Tuples, Sets, Dictionaries & Scope

> Folder: `Part2_Data_Structures_and_Scope/`  
> **Complete Part 1 first.** If you have time left in class (or want extra practice at home), work through these exercises — you may use **GitHub Copilot** for extra help.

### 📌 Quick Concept Overview

- **Tuple** (`("Alice", 21)`): Ordered and **immutable** (cannot be changed after creation); great for fixed pairs that you can **unpack** (`name, age = info`).
- **Set** (`{"apple", "banana"}`): Unordered collection of **unique** items (no duplicates); add items with `.add()`.
- **Dictionary** (`{"France": "Paris"}`): Stores **key–value** pairs so you can look up values by key.
- **Scope (`global`)**: Variables defined inside a function are **local**; variables defined outside are **global** (use `global var_name` inside a function only when you specifically need to modify a global variable).

---

### ⭐ Exercise 7 — Tuples: Unpacking a Tuple (`Part2_Data_Structures_and_Scope/7_tuples.py`)

**Task:**  
Given `person = ("Alice", 21)`, write a function `print_person(info)` that unpacks the tuple into `name` and `age` and prints `"Alice is 21 years old."`. Call `print_person(person)`.

**Sample output:**

```text
Alice is 21 years old.
```

**Hints:**

1. Unpack the tuple inside the function: `name, age = info`.
2. Print using an f-string: `f"{name} is {age} years old."`.

**Links:** https://www.w3schools.com/python/python_tuples.asp | https://www.w3schools.com/python/python_tuples_unpack.asp

---

### ⭐ Exercise 8 — Sets: Add an Item to a Set (`Part2_Data_Structures_and_Scope/8_sets.py`)

**Task:**  
Given `fruits = {"apple", "banana", "orange"}`, write a function `add_fruit(fruit_set, new_fruit)` that adds `new_fruit` to the set and returns the updated set. Call it with `fruits` and `"kiwi"`, then print the result.

**Sample output (order may vary):**

```text
{'apple', 'banana', 'orange', 'kiwi'}
```

**Hints:**

1. Inside the function, call `fruit_set.add(new_fruit)`.
2. Return `fruit_set` and print the returned value in the main program.

**Links:** https://www.w3schools.com/python/python_sets.asp | https://www.w3schools.com/python/python_sets_add.asp

---

### ⭐ Exercise 9 — Dictionaries: Simple Lookup (`Part2_Data_Structures_and_Scope/9_dictionaries.py`)

**Task:**  
Given:

```python
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
    "Spain": "Madrid"
}
```

Write a function `get_capital(country, capitals_dict)` that returns the capital of `country`, or `"Unknown"` if the country is not in the dictionary. Ask the user for a country name and print the returned result.

**Sample interaction:**

```text
Country: France
Paris
```

**Hints:**

1. Check `if country in capitals_dict:` and return `capitals_dict[country]`, otherwise return `"Unknown"` (or use `.get(country, "Unknown")`).
2. Keep `input()` outside the function.

**Link:** https://www.w3schools.com/python/python_dictionaries.asp

---

### ⭐ Exercise 10 — Local vs Global Scope (`Part2_Data_Structures_and_Scope/10_scope.py`)

**Task:**  
Create a global variable `counter = 0`. Write a function `increase_counter()` that uses the `global` keyword, increases `counter` by `2` each time it is called, and prints the updated value. Call the function three times.

**Sample output:**

```text
2
4
6
```

**Hints:**

1. Define `counter = 0` at the top level (outside any function).
2. Inside `increase_counter()`, put `global counter` on the first line before `counter += 2`.
3. Call `increase_counter()` three times in a row.

**Links:** https://www.w3schools.com/python/python_variables_global.asp | https://www.w3schools.com/python/python_scope.asp

---

### ⭐ Exercise 11 — `for` Loop Challenge: Largest of N Numbers (`Part2_Data_Structures_and_Scope/11_for_largest.py`)

**Task:**  
Ask the user **how many numbers** they will enter.  
Then, using a **`for` loop**, read that many integers from the user and print out the **largest** number entered.

**Sample interaction:**

```text
How many numbers? 4
Number 1: 10
Number 2: 5
Number 3: 27
Number 4: 12
The largest number was: 27
```

**Hints:**

1. Ask for `count = int(input("How many numbers? "))` before the loop.
2. Loop with `for i in range(count):` and prompt using `i + 1` (e.g. `f"Number {i + 1}: "`).
3. Keep a `largest` variable (start with `None`, or set it on the first iteration when `i == 0`).
4. Whenever the newly entered number is greater than `largest`, update `largest`.
5. Print the largest number after the loop ends.

**Link:** https://www.w3schools.com/python/python_for_loops.asp

---

## 🏠 Part 3 — Homework: Student Grade Tracker Refactor

> File: `Part3_Homework/12_homework.py`

Last week, you built a single-student Grade Calculator (`calculate_grade(score)` and `display_report(score, grade)`).  
This week, you will refactor your homework to process **multiple students** using **`while` loops**, **lists**, and **`for` loops** (assume the user enters integer numbers for scores).

---

### ✔ Part 1 (Mandatory): Multiple Students with a `while` Loop

1. Reuse your `calculate_grade(score)` function:
   - `90+` → `A`
   - `80–89` → `B`
   - `70–79` → `C`
   - `60–69` → `D`
   - below `60` → `F`
2. Update `display_report(name, score, grade)` so it prints the student's name too:
   ```text
   Grade Report:
   Name: Alice
   Score: 85
   Grade: B
   ```
3. In the main part of your program (or a `main()` function), use a **`while` loop** to:
   - ask for the student's `name` and `score` (`int(input(...))`)
   - call `calculate_grade(score)` and `display_report(name, score, grade)`
   - update `number_of_students` and `sum_of_scores` (or append the score to a `scores` list)
   - ask `"Would you like to enter another student? (yes/no): "` (use `.lower()`) and stop the loop when the user enters `"no"`
4. After the loop ends, print the total number of students processed and the class average score (`sum_of_scores / number_of_students`).

---

### ✔ Part 2 (Recommended): Score Range Validation with a `while` Loop

Make sure every entered score is between `0` and `100`.  
Use a simple `while` loop (either directly or inside a small helper function like `get_score(name)`):

- While `score < 0 or score > 100`, print an error message and ask for the score again.

---

### ✔ Part 3 (Optional Bonus): Lists, `for` Loop Summary & Strict `yes/no` Check

- Store each valid score in a list `scores = []` using `.append()`.
- After the `while` loop ends, use a **`for` loop** over `scores` to calculate the class total/average and/or find the highest score.
- Use a small `while` loop to keep asking if the user enters anything other than `"yes"` or `"no"` when prompted to continue.

**Sample interaction:**

```text
Please enter the student's name: Alice
Please enter Alice's score (0-100): 85

Grade Report:
Name: Alice
Score: 85
Grade: B

Would you like to enter another student? (yes/no): yes

Please enter the student's name: Bob
Please enter Bob's score (0-100): 120
Score must be between 0 and 100. Please try again.
Please enter Bob's score (0-100): 92

Grade Report:
Name: Bob
Score: 92
Grade: A

Would you like to enter another student? (yes/no): no

You processed 2 students.
Class average score: 88.5
```

---

## 🎯 Final Notes

- Focus on **Part 1** first so you master lists, `for` loops, and `while` loops during class.
- Keep your functions small and focused — let helper functions compute or print, and keep loop logic clear and readable.
- Test every program with multiple inputs (including edge cases like score `0`, `100`, or first-try PIN `4321`).
- If you get stuck, check the W3Schools links at the top of this page.
