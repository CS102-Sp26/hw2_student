"""
fast_fibonacci.py
Student skeleton for computing Fibonacci numbers using
divide-and-conquer matrix exponentiation.

PROGRAM FLOW
------------
1. run_all_cases() scans the inputs/ folder.
2. For each file, it calls main(input_path).
3. main(input_path):
      - calls read_input(input_path)
      - calls fibonacci(n)
      - converts the final answer to string and returns it
4. fibonacci(n):
      - defines the Fibonacci transition matrix A
      - calls matrix_power(A, n)
      - extracts F(n) from the resulting matrix
5. matrix_power(A, n):
      - recursively computes A^n using divide and conquer
      - calls multiply_matrix(...) to combine subresults
6. multiply_matrix(X, Y):
      - multiplies two 2x2 matrices and returns the product

IMPORTANT
---------
- Keep main(input_path) unchanged because the pytest file imports it.
- You may run this file directly to process all test cases automatically.
- Do not use NumPy or any external matrix library.
"""

from pathlib import Path


def multiply_matrix(X, Y):
    """
    Multiply two 2x2 matrices X and Y.

    Parameters
    ----------
    X : list[list[int]]
        First 2x2 matrix.
    Y : list[list[int]]
        Second 2x2 matrix.

    Returns
    -------
    list[list[int]]
        A new 2x2 matrix equal to X * Y.

    Called By
    ---------
    matrix_power(A, n)
    """
    # TODO: implement this function
    pass


def matrix_power(A, n):
    """
    Compute A^n using recursive divide and conquer.

    Parameters
    ----------
    A : list[list[int]]
        A 2x2 matrix.
    n : int
        A non-negative exponent.

    Returns
    -------
    list[list[int]]
        The matrix A raised to the power n.

    Program Flow
    ------------
    - Base case 1: if n == 0, return the identity matrix
    - Base case 2: if n == 1, return A
    - Recursive step
                """
    # TODO: implement this function
    pass


def fibonacci(n):
    """
    Compute the n-th Fibonacci number using matrix exponentiation.

    Parameters
    ----------
    n : int
        A non-negative integer.

    Returns
    -------
    int
        The n-th Fibonacci number.

    Program Flow
    ------------
    - If n == 0, return 0
    - Otherwise:
        1. define A = [[1, 1], [1, 0]]
        2. compute result = matrix_power(A, n)
        3. return result

    Calls
    -----
    - matrix_power(A, n)
    """
    # TODO: implement this function
    pass


def read_input(input_path):
    """
    Read the value of n from the given input file.

    Parameters
    ----------
    input_path : str
        Path to a text file containing a single non-negative integer.

    Returns
    -------
    int
        The integer value n.

    Called By
    ---------
    main(input_path)
    """
    with open(input_path, "r", encoding="utf-8") as f:
        return int(f.read().strip())


def main(input_path):
    """
    Solve one test case.

    Parameters
    ----------
    input_path : str
        Path to one input file.

    Returns
    -------
    str
        The n-th Fibonacci number as a string.

    Program Flow
    ------------
    1. n = read_input(input_path)
    2. ans = fibonacci(n)
    3. return str(ans)

    Called By
    ---------
    - pytest test file
    - run_all_cases()
    """
    n = read_input(input_path)
    ans = fibonacci(n)
    return str(ans)


def run_all_cases(input_dir="inputs"):
    """
    Automatically read and solve all input files in the given folder.

    Parameters
    ----------
    input_dir : str
        Folder containing test case files.

    Returns
    -------
    list[tuple[str, str]]
        A list of (filename, answer) pairs.

    Calls
    -----
    - main(input_path)
    """
    results = []
    folder = Path(input_dir)

    for path in sorted(folder.glob("*.txt")):
        results.append((path.name, main(str(path))))

    return results


if __name__ == "__main__":
    for fname, ans in run_all_cases():
        print(f"{fname}: {ans}")
