"""
fifo_bucket.py
Starter code for the FIFO variant of The Bucket Algorithm
"""

from pathlib import Path
from bucket_util import *


def fifo_bucket(graph, start_vertex):
    '''
        try to use this template code structure as much as possible
        to maintain the essence of the bucket algorithm and the step
        of checking and selecting a new vertex v which is brought next
        in the bucket
    '''
    bucket = [start_vertex]
    # YOUR CODE HERE

    edges_coming_out_of_the_bucket = True
    while edges_coming_out_of_the_bucket:
    # AND HERE

        break
    # AND HERE

    return bucket


def all_buckets(graph, start_vertex):
    n = len(graph)
    visited = [False] * n
    buckets = []
    first = True

    for i in range(n):
        if not visited[i]:
            start = i
            if first:
                start = start_vertex
                first = False
            bucket = fifo_bucket(graph, start)
            buckets.append(bucket)

            # update visited after getting the bucket
            for v in bucket:
                visited[v] = True
    return buckets


def main(input_path):
    """
    Solve one test case and return the answer as a string.
    """
    start_vertex, graph = read_input(input_path)
    buckets = all_buckets(graph, start_vertex)
    return str(buckets)


def run_cases_by_algo(algo):
    """
    Automatically read and solve all .txt files in the inputs folder.

    Calls:
    - main(input_path)
    """
    input_dir="inputs/" + algo
    results = []
    folder = Path(input_dir)

    for path in sorted(folder.glob("*.txt")):
        results.append((path.name, main(str(path))))

    return results


if __name__ == "__main__":
    algo = ALGOS[FIFO]
    for fname, ans in run_cases_by_algo(algo):
        print(f"{fname}: {ans}")
