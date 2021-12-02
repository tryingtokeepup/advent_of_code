"""
Create a function that returns True if the given string has any of the following:

Only letters and no numbers.
Only numbers and no letters.
If a string has both numbers and letters or contains characters that don't fit into any category, return False.

Examples:

solution("Bold") ➞ True
solution("123454321") ➞ True
solution("H3LL0") ➞ False
Notes:

Any string that contains spaces or is empty should return False.
[execution time limit] 4 seconds (py3)

[input] string input_str

[output] boolean
"""


def solution(input):
    # check if the character in input is letter or number

    # checkLetter, checkNumber = input[0].isalpha(), input[0].isdigit()
    for i in range(len(input)):
        # check if letter
        checkLetter, checkNumber = input[i].isalpha(), input[i].isdigit()
        print(checkLetter, checkNumber)
        if checkLetter is True:
            # check the rest of the letters
            for j in range(i + 1, len(input)):
                # if input[j] == TRUE
                checkLetter = input[j].isalpha()
                if checkLetter is True:
                    continue
                elif checkLetter is False:
                    return False
        if checkNumber is True:
            for j in range(i + 1, len(input)):
                checkNumber = input[j].isdigit()
                if checkNumber is True:
                    continue
                elif checkNumber is False:
                    return False
    return True


print(solution("Bold"))
print(solution("123454321"))
print(solution("H3LL0"))
