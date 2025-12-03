def parse_input_to_array():
    with open('input.txt', 'r') as f:
        arrays = []
        for line in f:
            line = line.strip()
            arrays.append([int(digit) for digit in line])
        return arrays

def part1():
    result = 0
    arrays = parse_input_to_array()

    for array in arrays:
        first_value = 0
        second_value = 0
        first_pos = 0
        pos = 0
        for digit in array:
            if(pos == len(array) - 1):
                break
            if digit > first_value:
                first_value = digit
                first_pos = pos
            pos += 1
        second_value = 0
        for i in range(first_pos+1, len(array)):
            if array[i] > second_value:
                second_value = array[i]
        result += first_value*10 + second_value
        print("HighScore: ", first_value*10 + second_value)
    print("Result: ", result)

            
            

def find_largest_joltage(sequence, length=12):
    n = len(sequence)
    dp = [[0] * (length + 1) for _ in range(n + 1)]

    # dp[i][j]: The maximum number we can form using the first i digits of the sequence and selecting j digits.
    for i in range(1, n + 1):
        digit = sequence[i - 1]
        for j in range(1, length + 1):
            # Option 1: Include the current digit
            include = dp[i - 1][j - 1] * 10 + digit if j > 0 else 0
            # Option 2: Exclude the current digit
            exclude = dp[i - 1][j]
            # Take the maximum of both options
            dp[i][j] = max(include, exclude)

    return dp[n][length]

def part2():
    arrays = parse_input_to_array()
    total_joltage = 0
    for sequence in arrays:
        largest_joltage = find_largest_joltage(sequence)
        total_joltage += largest_joltage
        print(f"Largest joltage for sequence {sequence}: {largest_joltage}")
    print(f"Total output joltage: {total_joltage}")

if __name__ == "__main__":
    arrays = parse_input_to_array()
    part2()