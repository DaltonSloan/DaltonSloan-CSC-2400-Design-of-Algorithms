# Dalton W. Sloan
# CSC-2400-001
# PA-2
# 10/01/2024

# I worked with Nick on this assignment.

import time
import matplotlib.pyplot as plt

def read_sequences(file_path):
    with open(file_path, 'r') as file:
        return [list(map(int, line.strip().split())) for line in file.readlines()]

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[cur_min_idx]:
                cur_min_idx = j
        arr[i], arr[cur_min_idx] = arr[cur_min_idx], arr[i]
    return arr

def bubble_sort(arr):
    for i in range(0, len(arr) - 1):
        did_swap = False
        for j in range(0, len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                did_swap = True
        if not did_swap:
            return arr
    return arr

def measure_time(sort_func, arr):
    start_time = time.perf_counter()
    sort_func(arr)
    end_time = time.perf_counter()
    return (end_time - start_time)

def main():
    file_path = 'unsorted_sequences.txt'
    sequences = read_sequences(file_path)
    sorted_arrays = []
    time_results = []

    # Sort each sequence using the three sorting algorithms
    # and measure the time taken for each
    # Using copies of the sequences to avoid modifying the original
    for seq in sequences:
        seq_copy = seq.copy()
        selection_sort_time = measure_time(selection_sort, seq_copy)
        sorted_arrays.append(seq_copy)

        seq_copy = seq.copy()
        bubble_sort_time = measure_time(bubble_sort, seq_copy)

        seq_copy = seq.copy()
        py_sort_time = measure_time(sorted, seq_copy)

        # Store the timing results for each sequence
        time_results.append((selection_sort_time, bubble_sort_time, py_sort_time))

    with open('sorted_arrays.txt', 'w') as sorted_file:
        for sorted_seq in sorted_arrays:
            sorted_file.write(' '.join(map(str, sorted_seq)) + '\n')

    # Write timing results to output file
    with open('sort_times.txt', 'w') as time_file:
        for times in time_results:
            time_file.write(f"{times}\n")

    # Plot the results
    plt.figure(figsize=(10, 5))
    x = range(1, len(sequences) + 1)  # X-axis values representing the sequence index

    # Extract times for plotting
    selection_sort_times = [t[0] for t in time_results]
    bubble_sort_times = [t[1] for t in time_results]
    py_sort_times = [t[2] for t in time_results]

    plt.plot(x, selection_sort_times, label="Selection Sort Time", marker='o')
    plt.plot(x, bubble_sort_times, label="Bubble Sort Time", marker='s')
    plt.plot(x, py_sort_times, label="Python Sort Time", marker='x')

    plt.xlabel('Sequence Index')
    plt.ylabel('Time (seconds)')
    plt.title('Sorting Algorithm Performance')
    plt.legend()
    plt.grid(True)
    plt.savefig('sort_times_plot.png')

    plt.show()

if __name__ == "__main__":
    main()