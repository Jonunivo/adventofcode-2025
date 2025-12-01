# Part 2: Count every time the dial points at 0 during any click
def part2():
    with open('input.txt', 'r') as f:
        dialPos = 50
        zeroCount = 0
        for line in f:
            line = line.strip()
            if not line:
                continue
            direction = line[0]
            value = int(line[1:])
            step = -1 if direction == 'L' else 1
            for _ in range(value):
                dialPos = (dialPos + step) % 100
                if dialPos == 0:
                    zeroCount += 1

        print("Part 2 Solution:", zeroCount)

def part1():
    with open('sample.txt', 'r') as f:
        dialPos = 50
        solutionCount = 0
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line[0] == 'L':
                value = int(line[1:])
                dialPos -= value
                print(f"The dial is rotated L{value} to point at {dialPos}.")
            elif line[0] == 'R':
                value = int(line[1:])
                dialPos += value
                print(f"The dial is rotated R{value} to point at {dialPos}.")

            while dialPos < 0:
                dialPos += 100
            while dialPos >= 100:
                dialPos -= 100

            if dialPos == 0:
                solutionCount += 1
                print("Dial is at position 0!")

        print("Solution:", solutionCount)


if __name__ == "__main__":
    part2()
