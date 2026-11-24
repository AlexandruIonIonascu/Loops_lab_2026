# Homework — Refactor the Grade Calculator with Loops and Lists
#
# In the Functions lab, you wrote calculate_grade(score) and display_report(score, grade)
# for a single score. Now refactor your solution so it can process multiple students!
# (Assume the user types integer numbers for scores.)
#
# 1. (Mandatory) Multiple Students with a while Loop:
#    - Reuse your calculate_grade(score) function:
#         90+   -> A
#         80-89 -> B
#         70-79 -> C
#         60-69 -> D
#         < 60  -> F
#    - Update display_report(name, score, grade) to also print the student's name:
#         Grade Report:
#         Name: Alice
#         Score: 85
#         Grade: B
#    - In your main program (or a main() function), use a while loop to:
#         * ask for the student's name and score (using int(input(...)))
#         * call calculate_grade(score) and display_report(name, score, grade)
#         * keep track of number_of_students and sum_of_scores (or store scores in a list)
#         * ask "Would you like to enter another student? (yes/no): " (use .lower())
#           and stop the loop when the user enters "no"
#    - After the loop ends, print how many students were processed and the
#      class average score (sum_of_scores / number_of_students).
#
# 2. (Recommended) Score Range Validation with a while Loop:
#    - Make sure the score is between 0 and 100.
#    - Use a while loop (either directly or in a small helper function get_score(name)):
#      while score < 0 or score > 100: print a warning and ask again.
#
# 3. (Optional Bonus) Lists, for Loop Summary & Strict yes/no Check:
#    - Store every entered score in a list: scores = [] (using .append()).
#    - After the while loop finishes, use a for loop over scores to compute the
#      total/average and/or find the highest score.
#    - Use a small while loop to keep asking if the user types anything other than
#      "yes" or "no" when asked to continue.
#
# Sample interaction:
# Please enter the student's name: Alice
# Please enter Alice's score (0-100): 85
#
# Grade Report:
# Name: Alice
# Score: 85
# Grade: B
#
# Would you like to enter another student? (yes/no): yes
#
# Please enter the student's name: Bob
# Please enter Bob's score (0-100): 120
# Score must be between 0 and 100. Please try again.
# Please enter Bob's score (0-100): 92
#
# Grade Report:
# Name: Bob
# Score: 92
# Grade: A
#
# Would you like to enter another student? (yes/no): no
#
# You processed 2 students.
# Class average score: 88.5

# Write your code here:
