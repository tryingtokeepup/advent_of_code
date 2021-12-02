"""
Given a string, return a new string with all the vowels removed.

Examples:

undefined("Lambda School is awesome!") -> "Lmbd Schl s wsm!"
Notes:

For this challenge, "y" is not considered a vowel.
[execution time limit] 4 seconds(py3)

[input] string input_str

[output] string
"""

testArray = ["Lambda School is awesome!", "Kai is cool!", "Sayo is smart!!!"]

vowelString = "aeiou"


def solution(string):

    # we need to make a new string
    output = ""
    # for character in string:
    #     if character not in vowelString:
    #         output += character
    # return output
    for character in string:
        for vowel in vowelString:
            if character == vowel:
                break
            elif vowel == vowelString[-1]:
                output += character
    return output


print(solution(testArray[0]))
# print(solution(testArray[1]))
# print(solution(testArray[2]))
