def find_cube_pairs(target):  # Added colon at the end to define the function correctly.
    solutions = []  # Proper list initialization.
    max_num = round(target ** (1/3))  # Fixed variable name typo and corrected exponentiation syntax.

    for a in range(1, max_num + 1):  # Changed 'ranges' to 'range'.
        for b in range(a, max_num + 1):  # Changed 'ranges' to 'range'.
            if a ** 3 + b ** 3 == target:  # Fixed exponentiation syntax.
                solutions.append((a, b))  # Appending tuple of valid pairs to the list.
    return solutions  # Returning the list of solutions.

pairs = find_cube_pairs(1729)  # Checking for cube pairs that sum to 1729. 

print("Valid cube pairs for 1729:")  # Changed 'printf' to 'print'. Changed 1728 to 1729

for a, b in pairs:  # Looping through the list of valid pairs.
    print(f" → {a}^3 + {b}^3 = {a**3} + {b**3} = 1729")  # Printing the pairs in the desired format. Same as Line 13
