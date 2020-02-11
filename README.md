# StringPuzzles
Python String Processing puzzles

## Cat Dog
Write a function that takes in a string parameter and returns a boolean value. ```True``` if the paramater has the same number of occurences of 'cat' as it does 'dog' and ```False``` otherwise.

| Function call | Result | 
| ------------- | ------ |
| cat_dog('adogandacat') | True |
| cat_dog('dogocatodog') | False |
| cat_dog('catcatdogcat') | False |


##  Other End
Write a function that takes in two string parameters and returns a boolean value representing whether or not one of the strings appears at the end of the the other string (case-insensitive).

| Function call | Result | 
| :-----------: | :----: |
| other_end('cherrybomb', 'bomb') | True |
| other_end('Eat', 'threat') | True |
| other_end('Same or different', 'same') | False |

## Count Code
Write a function that takes in a single string parameter and counts the number of occurrences of the string "code", except that you should accept any letter for the 'd', so "cope", and "cooe" count as occurences.

| Function call | Result | 
| :----------: | :----: |
| count_code("aaacodebbb") | 1 |
| count_code("code is coke") | 2 |
| count_code("The cozeco6e can't cope") | 3 |
