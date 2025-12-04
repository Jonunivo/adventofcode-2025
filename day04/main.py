def parse_input_to_grid():
    with open('input.txt', 'r') as f:
        grid = []
        for line in f:
            line = line.strip()
            grid.append([char for char in line])
        return grid
    
def print_grid(grid):
    rows, cols = len(grid), len(grid[0])
    for r in range(rows):
        for c in range(cols):
            print(grid[r][c], end='')
        print()



def part1():
    result = 0
    grid = parse_input_to_grid()
    marked = parse_input_to_grid()
    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if(grid[r][c] != '@'):
                continue
            num_neighbors = 0
            for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                    num_neighbors += 1
            if num_neighbors < 4:
                result += 1
                marked[r][c] = 'x'


    print_grid(marked)

    print(f"Result: {result}")

def part2():
    result = 0
    grid = parse_input_to_grid()
    marked = parse_input_to_grid()
    rows, cols = len(grid), len(grid[0])
    changed = True

    while(changed == True):
        changed = False
        for r in range(rows):
            for c in range(cols):
                if(grid[r][c] != '@'):
                    continue
                num_neighbors = 0
                for dr, dc in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == '@':
                        num_neighbors += 1
                if num_neighbors < 4:
                    result += 1
                    marked[r][c] = 'x'
                    grid[r][c] = 'x'
                    changed = True

    print_grid(marked)

    print(f"Result: {result}")


if __name__ == "__main__":
    part1()
    part2()