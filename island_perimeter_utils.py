# island_perimeter_utils.py

def create_grid():
    print("Welcome to Island Perimeter Calculator!")
    print("Please enter the number of rows and columns for the grid:")
    try:
        rows = int(input("Number of rows: "))
        cols = int(input("Number of columns: "))
        grid = []
        print("Enter the grid (0 for water, 1 for land):")
        for i in range(rows):
            row_input = input(f"Row {i + 1}: ")
            row = []
            for val in row_input.split():
                try:
                    cell = int(val)
                    if cell not in (0, 1):
                        raise ValueError("Invalid input. Each element must be 0 or 1.")
                    row.append(cell)
                except ValueError:
                    print("Invalid input. Please enter only integers (0 or 1) for grid elements.")
                    return None
            if len(row) != cols:
                print(f"Invalid input for row {i + 1}. Expected {cols} elements.")
                return None
            grid.append(row)
        return grid
    except ValueError:
        print("Invalid input. Please enter valid integers for rows, columns.")
        return None

def island_perimeter(grid):
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0])

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:  # Check above
                    perimeter -= 2
                if j > 0 and grid[i][j - 1] == 1:  # Check left
                    perimeter -= 2
    return perimeter