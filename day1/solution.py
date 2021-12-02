from typing import Counter


with open('input.txt') as f:
    lines = f.readlines()

# print(lines)

input = []
for num in lines:
    # print(num)
    integer = int(num.strip().replace('\n', ''))
    input.append(integer)

# print(input)


def solve(nums):
    if len(nums) == 1:
        return None

    count = 0
    # Counter
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            count += 1
    return count


def solveSlidingWindow(nums, k):
    slidingArray = []

    # for i in range(k, len(nums)):
    #     # sum(i-2,i)
    #     currentWindow = sum(nums[i-k:i])
    #     slidingArray.append(currentWindow)
    # # print(slidingArray)

    for i in range(len(nums)):
        currentWindow = sum(nums[i:i+k])
        slidingArray.append(currentWindow)
    return solve(slidingArray)


print(solveSlidingWindow(input, 3))
