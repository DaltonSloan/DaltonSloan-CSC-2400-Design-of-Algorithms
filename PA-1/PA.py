# Dalton W. Sloan
# CSC-2400-001
# PA-1
# 9/15/2024

# I Worked with Nick N on this.

import time
import matplotlib.pyplot as plt


def read_sequences(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file]


def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return True
    return False


def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return False


def main():
    sequences = read_sequences('sorted_sequences.txt')
    search_value = 500
    lengths = []
    linear_times = []
    binary_times = []
    results = []

    for seq in sequences:
        lengths.append(len(seq))

        start_time = time.perf_counter()
        linear_result = linear_search(seq, search_value)
        linear_times.append(time.perf_counter() - start_time)

        start_time = time.perf_counter()
        binary_result = binary_search(seq, search_value)
        binary_times.append(time.perf_counter() - start_time)

        results.append(f"{linear_result} {binary_result}")

    plt.plot(lengths, linear_times, label='Linear Search')
    plt.plot(lengths, binary_times, label='Binary Search')
    plt.xlabel('Sequence Length')
    plt.ylabel('Time(seconds)')
    plt.title('Time Taken by Linear and Binary Search')
    plt.legend()
    plt.show()

    with open('search_results.txt', 'w') as output_file:
        for result in results:
            output_file.write(result + '\n')


if __name__ == "__main__":
    main()
