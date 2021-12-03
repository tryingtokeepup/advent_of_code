with open('input.txt') as f:
    lines = f.readlines()

# print(lines)


class Sub():
    def __init__(self, horizontal=0, depth=0, aim=0):
        self.horizontal = horizontal
        self.depth = depth
        self.aim = aim

    def cubedDist(self):
        return abs(self.horizontal * self.depth)


def sanitizeInput(input):
    output = []
    for command in input:
        # split the command -> direction and distance
        cmdArray = command.split(" ")
        cmdArray[1] = int(cmdArray[1].strip().replace('\n', ''))
        output.append(cmdArray)
    return output


commandArray = sanitizeInput(lines)
# print(commandArray)


def solution(commands, sub):
    for command, distance in commands:
        # remember, there is no back

        if command == "up":
            sub.depth += distance
        elif command == "down":
            sub.depth -= distance
        # everything else is just forward
        else:
            sub.horizontal += distance


def solution2(commands, sub):
    for command, distance in commands:
        # remember, there is no back

        if command == "down":
            sub.aim += distance
        elif command == "up":
            sub.aim -= distance
        # everything else is just forward
        else:
            sub.horizontal += distance
            sub.depth += sub.aim * distance
    print(sub.horizontal, sub.depth)


kaiSub = Sub()
# solution(commandArray, kaiSub)
solution2(commandArray, kaiSub)
print(kaiSub.cubedDist())
