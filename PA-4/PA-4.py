# Dalton W. Sloan
# CSC 2400-001
# Programing Assignment 4
# Nov 5th, 2024

# I worked with Nick N on this assignment.

import time
import matplotlib.pyplot as plt



# MergeSort Implementation
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        merge(arr, left_half, right_half)


def merge(arr, left_half, right_half):
    i = j = k = 0
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1


# QuickSort with Lomuto's Partition
def quicksort_lomuto(arr, low, high):
    if low < high:
        pi = lomuto_partition(arr, low, high)
        quicksort_lomuto(arr, low, pi - 1)
        quicksort_lomuto(arr, pi + 1, high)


def lomuto_partition(arr, low, high):
    pivot = arr[low]
    i = low
    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i], arr[low] = arr[low], arr[i]
    return i


# QuickSort with Hoare's Partition
def quicksort_hoare(arr, low, high):
    if low < high:
        pi = hoare_partition(arr, low, high)
        quicksort_hoare(arr, low, pi)
        quicksort_hoare(arr, pi + 1, high)


def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while arr[i] < pivot:
            i += 1
        j -= 1
        while arr[j] > pivot:
            j -= 1
        if i >= j:
            return j
        arr[i], arr[j] = arr[j], arr[i]


# Function to read, sort, and time each sequence
def process_sequences():
    ms_times, qs_lomuto_times, qs_hoare_times = [], [], []
    ms_output, qs_lomuto_output, qs_hoare_output = [], [], []

    with open("unsorted_sequences.txt", "r") as f:
        lines = f.readlines()

    for line in lines:
        seq = list(map(int, line.strip().split()))

        # MergeSort
        ms_seq = seq[:]
        start_time = time.time_ns()
        merge_sort(ms_seq)
        ms_times.append(time.time_ns() - start_time)
        ms_output.append(" ".join(map(str, ms_seq)))

        # QuickSort Lomuto
        qs_lomuto_seq = seq[:]
        start_time = time.time_ns()
        quicksort_lomuto(qs_lomuto_seq, 0, len(qs_lomuto_seq) - 1)
        qs_lomuto_times.append(time.time_ns() - start_time)
        qs_lomuto_output.append(" ".join(map(str, qs_lomuto_seq)))

        # QuickSort Hoare
        qs_hoare_seq = seq[:]
        start_time = time.time_ns()
        quicksort_hoare(qs_hoare_seq, 0, len(qs_hoare_seq) - 1)
        qs_hoare_times.append(time.time_ns() - start_time)
        qs_hoare_output.append(" ".join(map(str, qs_hoare_seq)))

    # Writing sorted outputs to files
    with open("MSOutputs.txt", "w") as f:
        f.write("\n".join(ms_output) + "\n")
    with open("QSLomutoOutputs.txt", "w") as f:
        f.write("\n".join(qs_lomuto_output) + "\n")
    with open("QSHoareOutputs.txt", "w") as f:
        f.write("\n".join(qs_hoare_output) + "\n")

    # Writing runtimes to file
    with open("runtimes.txt", "w") as f:
        for ms, lomuto, hoare in zip(ms_times, qs_lomuto_times, qs_hoare_times):
            f.write(f"({ms}, {lomuto}, {hoare})\n")

def plot_runtimes():
    ms_times = []
    qs_lomuto_times = []
    qs_hoare_times = []

    with open("runtimes.txt", "r") as f:
        for line in f:
            ms, lomuto, hoare = map(int, line.strip().strip("()").split(", "))
            ms_times.append(ms)
            qs_lomuto_times.append(lomuto)
            qs_hoare_times.append(hoare)

    sequence_lengths = range(1, len(ms_times) + 1)

    plt.figure(figsize=(10, 6))
    plt.plot(sequence_lengths, ms_times, label="MergeSort Time", color="blue")
    plt.plot(sequence_lengths, qs_lomuto_times, label="QuickSort Lomuto Time", color="red")
    plt.plot(sequence_lengths, qs_hoare_times, label="QuickSort Hoare Time", color="green")

    plt.xlabel("Sequence Lengths")
    plt.ylabel("Clock-Times (ns)")
    plt.title("Sorting Algorithm Runtimes by Sequence Length")
    plt.legend()
    plt.grid(True)
    plt.show()

# Run the sorting and timing process
process_sequences()
plot_runtimes()