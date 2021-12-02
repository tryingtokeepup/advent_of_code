"""
Create a function that given an integer, returns an integer where every digit in the input integer is squared.

Examples:

solution(9119) -> 811181 because 9^2 = 81, 1^2 = 1, 1^2 = 1, and 9^2 = 81
solution(2483) -> 416649 because 2^2 = 4, 4^2 = 16, 8^2 = 64, and 3^2 = 9
[execution time limit] 4 seconds (py3)

[input] integer n

[output] integer
"""


def solution(integer):
    # first we need to change the number to string
    # because we want to loop over the number (input)
    intString = str(integer)

    outputString = ""
    # loop over string
    for character in intString:
        # we need to change the character to number/int
        # because we want to calculate the square
        charInt = int(character)
        # square the int
        squared = charInt ** 2
        # outputString = outputString + squared
        outputString += str(squared)
    return outputString


print(solution(9119))

# so, first change number to string
# sayoNumber = 912121
# sayoNumberString = str(sayoNumber)

# outputString = ""
# for char in sayoNumberString:
#     charNumber = int(char)

#     squared = charNumber ** 2
#     # print(squared)
#     outputString += str(squared)

# print(int(outputString))


# print(f"Hey this is sayoNumber: {sayoNumber}")
# print(
#     f"Hey this is sayoNumberString: {sayoNumberString}, and its a string? {isinstance(sayoNumberString, str)}")

# print(sayoNumberString[0])  # should be "2"
