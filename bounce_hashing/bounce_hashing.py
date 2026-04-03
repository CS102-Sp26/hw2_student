def h1(key, m):
    """Hash function 1: key mod m"""
    # TODO: Implement this
    pass

def h2(key, m):
    """Hash function 2: (key // 7 + 3) mod m"""
    # TODO: Implement this
    pass

def insert(key, m, table1, table2):
    """
    Insert a key into the bounce hash table.

    - First try Table1 at position h1(key).
    - If occupied, evict the existing key and try to place it in Table2 using h2.
    - Continue alternating until the key is placed or a cycle is detected.
    - Cycle detection: if the number of evictions exceeds 2*m, print:
        "Cycle detected! Cannot insert key: <key>"
      and restore both tables to their state before this insertion.

    Returns: None (modifies table1 and table2 in place)
    """
    # TODO: Implement this
    pass

def delete(key, m, table1, table2):
    """
    Delete a key from the bounce hash table.

    - Check Table1 at h1(key). If found, set to None.
    - Otherwise check Table2 at h2(key). If found, set to None.
    - If not found in either, do nothing.

    Returns: None (modifies table1 and table2 in place)
    """
    # TODO: Implement this
    pass

def lookup(key, m, table1, table2):
    """
    Look up a key in the bounce hash table.

    - Check Table1 at h1(key).
    - Check Table2 at h2(key).

    Returns: True if found, False otherwise
    """
    # TODO: Implement this
    pass

def main(filename):
    """
    Read operations from the input file and execute them.

    Input format:
        First line: m Op
        Next Op lines: INSERT <key> / DELETE <key> / LOOKUP <key>

    Returns: (Table1, Table2, lookup_results)
        - Table1: list of size m
        - Table2: list of size m
        - lookup_results: list of True/False for each LOOKUP operation
    """
    with open(filename) as f:
        lines = f.readlines()

    first_line = lines[0].strip().split()
    m = int(first_line[0])
    op_count = int(first_line[1])
    

    # TODO: Initialize table1, table2, and lookup_results

    # TODO: Loop through operations, parse each line,
    #       and call the appropriate function (insert/delete/lookup).
    #       For LOOKUP, append the result to lookup_results.

    # TODO: Return (table1, table2, lookup_results)
    pass


if __name__ == "__main__":
    import sys
    result = main(sys.argv[1])
    print(result)
