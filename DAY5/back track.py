def generate_magic_square():
    # Initialize a 3x3 matrix with zeros
    magic_square = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    
    # Set initial values
    row, col = 0, 1
    
    # Fill the matrix with numbers 1 to 9
    for num in range(1, 10):
        magic_square[row][col] = num
        row -= 1
        col += 1
        
        # Check bounds and update indices
        if row < 0 and col > 2:
            row += 2
            col -= 1
        elif row < 0:
            row = 2
        elif col > 2:
            col = 0
        elif magic_square[row][col] != 0:
            row += 2
            col -= 1
    
    return magic_square

def print_matrix(matrix):
    for row in matrix:
        print(row)

def check_magic_square(matrix):
    # Check rows, columns, and diagonals
    for i in range(3):
        if sum(matrix[i]) != 15:
            return False

        col_sum = sum(matrix[j][i] for j in range(3))
        if col_sum != 15:
            return False

    main_diag_sum = sum(matrix[i][i] for i in range(3))
    anti_diag_sum = sum(matrix[i][2 - i] for i in range(3))

    if main_diag_sum != 15 or anti_diag_sum != 15:
        return False

    return True

# Generate and print the magic square
magic_square = generate_magic_square()
print("Generated Magic Square:")
print_matrix(magic_square)

# Check if it's a magic square
if check_magic_square(magic_square):
    print("It's a Magic Square!")
else:
    print("Not a Magic Square.")