"""
Write a function that takes a string as input and returns that string in reverse order, with the opposite casing for each character within the string.

Examples:

solution("Hello World") ➞ "DLROw OLLEh"
solution("ReVeRsE") ➞ "eSrEvEr"
solution("Radar") ➞ "RADAr"
Notes:

The input string will only contain alpha characters.
[execution time limit] 4 seconds (py3)

[input] string txt

[output] string
"""


def solution(input):
	reversed = input[::-1]
	output = []
	# now we have to change the case => upper to lower, lower to upper
	for char in reversed:
		
		if char.islower() is True:
			output.append(char.upper())
			
		else:
			output.append(char.lower())
	outputString = "".join(output)
	return outputString
	
def coolSolution(input):
	cool = [x.lower() if x.isupper() == True else x.upper() for x in input[::-1]]
	return "".join(cool)
	
# print(solution("Hello World"))
# print(solution("ReVeRsE"))
# print(solution("Radar"))

print(coolSolution("Radar"))
