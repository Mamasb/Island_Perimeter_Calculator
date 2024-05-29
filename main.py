# main.py
from island_perimeter_utils import create_grid, island_perimeter

def main():
    grid = create_grid()
    if grid:
        perimeter = island_perimeter(grid)
        if perimeter is not None:
            print("Perimeter of the island:", perimeter)

if __name__ == "__main__":
    main()