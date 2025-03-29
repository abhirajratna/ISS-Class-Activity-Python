def find_cube_pairs(target):  # Added colon at the end to define the function correctly.
    solutions = []  # removed semicolon.
    max_num = round(target ** (1/3))  # Fixed variable name typo from `targ` to `target` and corrected exponentiation syntax.

    for a in range(1, max_num + 1):  # Changed `ranges` to `range` for correct function name.
        for b in range(a, max_num + 1):  # Same as above, corrected `ranges` to `range`.
            if a ** 3 + b ** 3 == target:  # Changed `***` to `**` for proper exponentiation.
                solutions.append((a, b))  # Changed `sol` to `solutions` and removed ;
    return solutions  # Corrected `sol` to `solutions` to match the variable name.

pairs = find_cube_pairs(1729) 

print("Valid cube pairs for 1729:")  # Changed `printf` to `print`. And 1728 to 1729

for a, b in pairs:  # Changed `pair` to `pairs` for correct iteration over the returned list.
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # Fixed exponentiation from `a**2` and `b**2` to `a**3` and `b**3`.
