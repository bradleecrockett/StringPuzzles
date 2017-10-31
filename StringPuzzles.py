# Name: First Last
# Date:
# Period:
# Lab: StringPuzzles.py
# Description: Two string procesing puzzles that use the Python string methods and for loops.
#
#     Style - Code format, whitespace and PEP-8 style is followed making code easy to read.
#     Comments - Blocks of code are well commented, every function has a descriptive comment.
#     Tests -   The program runs as described in the specifications without errors(passes all tests).
#


# Write a program that takes in a string parameter and returns the boolean value
# True if the string has the same number of occurrences of 'cat' as it does occurrences
# of 'dog' and False if it does not.
def cat_dog(str):
    # Enter your code here

    return 0

# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
def other_end(str1, str2):
    # ++ your code here ++
    return 0


def main():
    # simple testing
    print("Expected: True \t\tresult: ", cat_dog("adogandacat"))
    print("Expected: False \tresult: ", cat_dog("moredogshthancatsbecausedogsarebetter"))

    print("Expected: True \t\tresult: ", other_end("endthesame", "Same"))
    print("Expected: False \tresult: ", other_end("this is different", "Same"))

main()