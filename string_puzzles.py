# Name: First Last
# Date:
# Period:
# Lab: string_puzzles.py
# Description: Two string processing puzzles that use the Python string methods and for loops.
#
#     Style - Code format, whitespace and PEP-8 style is followed making code easy to read.
#     Comments - Blocks of code are well commented, every function has a descriptive comment.
#     Tests -   The program runs as described in the specifications without errors(passes all tests).
#


# Write a program that takes in a string parameter and returns the boolean value
# True if the string has the same number of occurrences of 'cat' as it does occurrences
# of 'dog' and False if it does not.
def cat_dog(mystr):
    # ++ Your code here ++

    return 0


# Given two strings, return True if either of the strings appears at the very end of the other string,
# ignoring upper/lower case differences (in other words, the computation should not be "case sensitive").
# Note: s.lower() returns the lowercase version of a string.
def other_end(str1, str2):
    # ++ your code here ++

    return 0


# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter
# for the 'd', so "cope" and "cooe" count
# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcopeco6e') → 3
def count_code(str):
    # ++ Your code here ++

    return -1


def main():
    # simple testing
    print("cat_dog Testing")
    print("Expected: True \t\tResult: ", cat_dog("adogandacat"))
    print("Expected: False \tResult: ", cat_dog("more dogs than cats because dogs are better"))
    print("Expected: True \tResult: ", cat_dog("The best dogs can catch frisbees"))

    print("\nother_end Testing")
    print("Expected: True \t\tResult: ", other_end("endthesame", "Same"))
    print("Expected: False \tResult: ", other_end("this is different", "Same"))
    print("Expected: True \tResult: ", other_end("Racecar", "car"))

    print("\ncount_code Testing")
    print("Expected: 2 \t\tResult: ", count_code("codecozecade"))
    print("Expected: 0 \t\tResult: ", count_code("asdfhjkl"))
    print("Expected: 3 \t\tResult: ", count_code("codecokecole"))
    print("Expected: 0 \t\tResult: ", count_code("abc"))


if __name__ == "__main__":
    main()
