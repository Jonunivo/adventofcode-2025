def part1():
    result = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            for value in line.split(','):
                from_value, to_value = map(int, value.split('-'))
                for i in range(from_value, to_value + 1):
                    num_digits_from_value = len(str(i))
                    front_part = i % (10 ** (num_digits_from_value//2))
                    back_part = i // (10 ** (num_digits_from_value//2))
                    if(front_part == back_part):
                        result += i
    print(f"Result: {result}")

def is_repeated_pattern(n):
    """Check if number n is made of a pattern repeated at least twice."""
    s = str(n)
    length = len(s)
    
    # Try all possible pattern lengths from 1 to length//2
    for pattern_len in range(1, length // 2 + 1):
        # Check if the total length is divisible by pattern length
        if length % pattern_len == 0:
            pattern = s[:pattern_len]
            repetitions = length // pattern_len
            
            # Check if repeating the pattern gives us the original number
            if pattern * repetitions == s:
                return True
    
    return False

def part2():
    result = 0
    with open('input.txt', 'r') as f:
        for line in f:
            line = line.strip()
            for value in line.split(','):
                from_value, to_value = map(int, value.split('-'))
                for i in range(from_value, to_value + 1):
                    if is_repeated_pattern(i):
                        print(f"Found repeated pattern number: {i}")
                        result += i
    print(f"Result: {result}")



if __name__ == "__main__":
    part2()
