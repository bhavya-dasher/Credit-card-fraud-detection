import csv
from typing import List, Any, Tuple

def read_csv(filename: str) -> List[List[Any]]:
    with open(filename, 'r', newline='') as file:
        reader = csv.reader(file)
        return [row for row in reader]

def write_csv(filename: str, spreadsheet: List[List[Any]]) -> None:
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(spreadsheet)

def set_cell(spreadsheet: List[List[Any]], row: int, col: int, value: Any) -> None:
    if row >= len(spreadsheet):
        for _ in range(len(spreadsheet), row + 1):
            spreadsheet.append([])
    if col >= len(spreadsheet[row]):
        spreadsheet[row].extend([''] * (col - len(spreadsheet[row]) + 1))
    spreadsheet[row][col] = value

def get_cell(spreadsheet: List[List[Any]], row: int, col: int) -> Any:
    if row < len(spreadsheet) and col < len(spreadsheet[row]):
        return spreadsheet[row][col]
    return None

def display(spreadsheet: List[List[Any]]) -> None:
    for row in spreadsheet:
        print(" ".join(str(cell) for cell in row))

def sum_cells(spreadsheet: List[List[Any]], range_tuple: Tuple[Tuple[int, int], Tuple[int, int]]) -> float:
    start, end = range_tuple
    total = 0
    for row in range(start[0], end[0] + 1):
        for col in range(start[1], end[1] + 1):
            value = get_cell(spreadsheet, row, col)
            if value is not None and value != '':
                total += float(value)
    return total

def average_cells(spreadsheet: List[List[Any]], range_tuple: Tuple[Tuple[int, int], Tuple[int, int]]) -> float:
    total = sum_cells(spreadsheet, range_tuple)
    start, end = range_tuple
    count = (end[0] - start[0] + 1) * (end[1] - start[1] + 1)
    return total / count if count > 0 else 0

def min_cells(spreadsheet: List[List[Any]], range_tuple: Tuple[Tuple[int, int], Tuple[int, int]]) -> float:
    start, end = range_tuple
    values = []
    for row in range(start[0], end[0] + 1):
        for col in range(start[1], end[1] + 1):
            value = get_cell(spreadsheet, row, col)
            if value is not None and value != '':
                values.append(float(value))
    return min(values) if values else None

def max_cells(spreadsheet: List[List[Any]], range_tuple: Tuple[Tuple[int, int], Tuple[int, int]]) -> float:
    start, end = range_tuple
    values = []
    for row in range(start[0], end[0] + 1):
        for col in range(start[1], end[1] + 1):
            value = get_cell(spreadsheet, row, col)
            if value is not None and value != '':
                values.append(float(value))
    return max(values) if values else None

def sort_row(spreadsheet: List[List[Any]], row: int) -> None:
    if row < len(spreadsheet):
        spreadsheet[row] = sorted(spreadsheet[row], key=lambda x: float(x) if x != '' else float('-inf'))

def sort_column(spreadsheet: List[List[Any]], col: int) -> None:
    if spreadsheet and col < len(spreadsheet[0]):
        column = [row[col] if col < len(row) else '' for row in spreadsheet]
        sorted_column = sorted(column, key=lambda x: float(x) if x != '' else float('-inf'))
        for i, row in enumerate(spreadsheet):
            if col < len(row):
                row[col] = sorted_column[i]

def convert_to_float(spreadsheet: List[List[Any]], row: int, col: int) -> None:
    value = get_cell(spreadsheet, row, col)
    if value is not None and value != '':
        try:
            set_cell(spreadsheet, row, col, float(value))
        except ValueError:
            print(f"Warning: Cannot convert '{value}' to float.")

def convert_to_string(spreadsheet: List[List[Any]], row: int, col: int) -> None:
    value = get_cell(spreadsheet, row, col)
    if value is not None:
        set_cell(spreadsheet, row, col, str(value))

def run_cli():
    spreadsheet = []
    while True:
        print("\nSpreadsheet Operations:")
        print("1. Open CSV file")
        print("2. Write to CSV file")
        print("3. Set cell value")
        print("4. Get cell value")
        print("5. Display spreadsheet")
        print("6. Perform calculation (sum, average, min, max)")
        print("7. Sort row or column")
        print("8. Convert cell type")
        print("9. Run test script")
        print("0. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '0':
            break
        elif choice == '1':
            filename = input("Enter CSV filename to open: ")
            spreadsheet = read_csv(filename)
            print("File loaded successfully.")
        elif choice == '2':
            filename = input("Enter CSV filename to write: ")
            write_csv(filename, spreadsheet)
            print("File written successfully.")
        elif choice == '3':
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            value = input("Enter value: ")
            set_cell(spreadsheet, row, col, value)
            print("Cell updated.")
        elif choice == '4':
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            value = get_cell(spreadsheet, row, col)
            print(f"Value in cell: {value}")
        elif choice == '5':
            display(spreadsheet)
        elif choice == '6':
            calc_type = input("Enter calculation type (sum/average/min/max): ")
            start_row = int(input("Enter start row: "))
            start_col = int(input("Enter start column: "))
            end_row = int(input("Enter end row: "))
            end_col = int(input("Enter end column: "))
            range_tuple = ((start_row, start_col), (end_row, end_col))
            if calc_type == 'sum':
                result = sum_cells(spreadsheet, range_tuple)
            elif calc_type == 'average':
                result = average_cells(spreadsheet, range_tuple)
            elif calc_type == 'min':
                result = min_cells(spreadsheet, range_tuple)
            elif calc_type == 'max':
                result = max_cells(spreadsheet, range_tuple)
            else:
                print("Invalid calculation type.")
                continue
            print(f"Result: {result}")
        elif choice == '7':
            sort_type = input("Enter sort type (row/column): ")
            index = int(input("Enter row or column number to sort: "))
            if sort_type == 'row':
                sort_row(spreadsheet, index)
            elif sort_type == 'column':
                sort_column(spreadsheet, index)
            else:
                print("Invalid sort type.")
            print("Sorting complete.")
        elif choice == '8':
            row = int(input("Enter row number: "))
            col = int(input("Enter column number: "))
            conv_type = input("Enter conversion type (float/string): ")
            if conv_type == 'float':
                convert_to_float(spreadsheet, row, col)
            elif conv_type == 'string':
                convert_to_string(spreadsheet, row, col)
            else:
                print("Invalid conversion type.")
            print("Conversion complete.")
        elif choice == '9':
            run_test_script()
        else:
            print("Invalid choice. Please try again.")

def run_test_script():
    print("Running test script...")
    # Read the input CSV file
    spreadsheet = read_csv('input.csv')

    # Set cell values
    set_cell(spreadsheet, 0, 0, 5)
    set_cell(spreadsheet, 0, 1, 10)
    set_cell(spreadsheet, 0, 2, 15)
    set_cell(spreadsheet, 1, 0, 20)
    set_cell(spreadsheet, 1, 1, 25)

    # Display the spreadsheet
    print("Initial spreadsheet:")
    display(spreadsheet)

    # Perform calculations
    print("Sum:", sum_cells(spreadsheet, ((0, 0), (1, 1))))
    print("Average:", average_cells(spreadsheet, ((0, 0), (1, 1))))
    print("Min:", min_cells(spreadsheet, ((0, 0), (1, 1))))
    print("Max:", max_cells(spreadsheet, ((0, 0), (1, 1))))

    # Sort operations
    sort_row(spreadsheet, 0)
    sort_column(spreadsheet, 1)

    # Type conversions
    convert_to_float(spreadsheet, 0, 0)
    convert_to_string(spreadsheet, 0, 1)

    # Display the modified spreadsheet
    print("\nModified spreadsheet:")
    display(spreadsheet)

    # Write to output CSV file
    write_csv('output.csv', spreadsheet)
    print("Test script completed. Results written to 'output.csv'")

if __name__ == "__main__":
    run_cli()
