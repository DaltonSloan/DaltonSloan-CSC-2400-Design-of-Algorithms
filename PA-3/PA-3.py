import time
import matplotlib.pyplot as plt

# Credit Statement
# Worked with Dalton/Nick

# Non-Recursive Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def binary_search(arr, val, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] < val:
            start = mid + 1
        else:
            end = mid - 1
    return start

# Binary Insertion Sort
def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = binary_search(arr, key, 0, i - 1)
        for k in range(i, j, -1):
            arr[k] = arr[k - 1]

        arr[j] = key
    return arr

# Doubly Linked List Node
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

# Doubly Linked List
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def insertion_sort(self):
        current = self.head
        if current is None:
            return
        while current:
            key = current.data
            prev = current.prev
            while prev and prev.data > key:
                prev.next.data = prev.data
                prev = prev.prev
            if prev:
                prev.next.data = key
            else:
                self.head.data = key
            current = current.next

    def to_list(self):
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        return result

# Read input sequences
with open('unsorted_sequences.txt', 'r') as f:
    sequences = [list(map(int, line.strip().split())) for line in f.readlines()]

non_rec_outputs = []
bin_ins_outputs = []
linked_list_outputs = []
times = []

for i, sequence in enumerate(sequences):
    # Timing Non-Recursive Insertion Sort
    start_time = time.perf_counter_ns()
    sorted_non_rec = insertion_sort(sequence.copy())
    non_rec_time = time.perf_counter_ns() - start_time

    # Timing Binary Insertion Sort
    start_time = time.perf_counter_ns()
    sorted_bin_ins = binary_insertion_sort(sequence.copy())
    bin_ins_time = time.perf_counter_ns() - start_time

    # Timing Doubly Linked List Sort
    dll = DoublyLinkedList()
    for num in sequence:
        dll.append(num)
    start_time = time.perf_counter_ns()
    dll.insertion_sort()
    sorted_linked_list = dll.to_list()
    linked_list_time = time.perf_counter_ns() - start_time

    # Collecting outputs
    non_rec_outputs.append(sorted_non_rec)
    bin_ins_outputs.append(sorted_bin_ins)
    linked_list_outputs.append(sorted_linked_list)
    times.append((non_rec_time, bin_ins_time, linked_list_time))

# Write outputs to files
with open('NonRecOutputs.txt', 'w') as f:
    for sorted_array in non_rec_outputs:
        f.write(' '.join(map(str, sorted_array)) + '\n')

with open('BinInsOutputs.txt', 'w') as f:
    for sorted_array in bin_ins_outputs:
        f.write(' '.join(map(str, sorted_array)) + '\n')

with open('LinkedListOutputs.txt', 'w') as f:
    for sorted_array in linked_list_outputs:
        f.write(' '.join(map(str, sorted_array)) + '\n')

with open('times.txt', 'w') as f:
    for time_tuple in times:
        f.write(f"{time_tuple}\n")

# (Optional) Extra Credit: Plotting
lengths = range(100, 1000)
non_rec_times, bin_ins_times, linked_list_times = zip(*times)

plt.figure(figsize=(10, 6))
plt.plot(lengths, non_rec_times, label='Non-Recursive Insertion Sort', color='blue')
plt.plot(lengths, bin_ins_times, label='Binary Insertion Sort', color='orange')
plt.plot(lengths, linked_list_times, label='Linked List Insertion Sort', color='green')
plt.xlabel('Sequence Length')
plt.ylabel('Time (nanoseconds)')
plt.title('Sorting Algorithm Time Complexity')
plt.legend()
plt.grid()
plt.savefig('sorting_times.png')  # Save the plot as an image
plt.show()
