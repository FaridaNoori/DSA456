"""
Sorting Algorithms Analysis Assignment 01
"""

import random
import time
import matplotlib.pyplot as plt
import sys

# Increase recursion limit so worst-case QuickSort (last-element pivot) can finish
sys.setrecursionlimit(15000)


# Counter for operation counting

class Counter:
    def __init__(self):
        self.steps = 0

    def add(self, amount=1):
        self.steps += amount

    def get(self):
        return self.steps


# 1. Bubble Sort

def bubble_sort(arr):
    counter = Counter()
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            counter.add()  # comparison
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                counter.add(3)  # swap cost
                swapped = True
        if not swapped:
            break
    return arr, counter.get()


# 2. Selection Sort

def selection_sort(arr):
    counter = Counter()
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            counter.add()  # comparison
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            counter.add(3)  # swap
    return arr, counter.get()


# 3. Insertion Sort (full list)

def insertion_sort(arr):
    counter = Counter()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0:
            counter.add()  # comparison
            if arr[j] > key:
                arr[j + 1] = arr[j]
                counter.add()  # shift
                j -= 1
            else:
                break
        arr[j + 1] = key
        counter.add()  # insert
    return arr, counter.get()


# 4. Quick Sort (Lomuto - last element as pivot)

def quick_sort(arr):
    counter = Counter()

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            counter.add()  # comparison
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                counter.add(3)  # swap
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        counter.add(3)  # final swap
        return i + 1

    def quicksort(low, high):
        if low < high:
            counter.add()  # condition
            pi = partition(low, high)
            quicksort(low, pi - 1)
            quicksort(pi + 1, high)

    quicksort(0, len(arr) - 1)
    return arr, counter.get()


# 5. Insertion Sort - subarray version (required by assignment)

def insertion_sort_subarray(arr, left, right):
    counter = Counter()
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left:
            counter.add()  # comparison
            if arr[j] > key:
                arr[j + 1] = arr[j]
                counter.add()  # shift
                j -= 1
            else:
                break
        arr[j + 1] = key
        counter.add()  # insert
    return arr, counter.get()


# Helper: verify correctness

def is_correctly_sorted(original, result):
    return result == sorted(original)


# Step 1 & quick check (n=100)

def step1_demo():
    print("\n" + "="*75)
    print("STEP 1  –  Implementations + correctness check  (n=100)")
    print("="*75)

    random.seed(42)
    original = [random.randint(1, 1000) for _ in range(100)]

    tests = [
        ("Bubble", bubble_sort),
        ("Selection", selection_sort),
        ("Insertion", insertion_sort),
        ("Quick", quick_sort),
        ("Insertion-subarray", lambda a: insertion_sort_subarray(a, 0, len(a)-1))
    ]

    for name, func in tests:
        arr = original.copy()
        sorted_arr, steps = func(arr)
        correct = is_correctly_sorted(original, sorted_arr)
        print(f"{name:18} | correct: {correct:5} | steps: {steps:>9,}")


# Step 2 – Best / Average / Worst case operation counts (n=1200)

def step2_demo():
    print("\n" + "="*75)
    print("STEP 2  –  Operation counts: best / avg / worst case  (n=1200)")
    print("="*75)

    n = 1200
    random.seed(43)

    best    = list(range(n))
    worst   = list(range(n-1, -1, -1))
    average = [random.randint(1, 100000) for _ in range(n)]

    cases = [("best", best), ("worst", worst), ("average", average)]

    algos = [
        ("Bubble",    bubble_sort),
        ("Selection", selection_sort),
        ("Insertion", insertion_sort),
        ("Quick",     quick_sort),
    ]

    for algo_name, func in algos:
        print(f"\n{algo_name}")
        for case_name, data in cases:
            arr = data.copy()
            _, steps = func(arr)
            print(f"  {case_name:8} → {steps:>12,}")


# Step 3 – T(n) vs n  (worst case) + plot

def step3_operation_plot():
    print("\n" + "="*75)
    print("STEP 3  –  Operation counts T(n) vs n   (worst-case input)")
    print("="*75)

    sizes = [100, 200, 400, 600, 800, 1000, 1200, 1500, 1800]

    algos = {
        "Bubble":    bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
        "Quick":     quick_sort,
    }

    results = {name: [] for name in algos}

    print(f"{'n':>6} |", end="")
    for name in algos:
        print(f" {name:>12}", end="")
    print()

    random.seed(46)

    for n in sizes:
        base = [random.randint(1, 200000) for _ in range(n)]
        worst = base[::-1]

        print(f"{n:6} |", end="")

        for name, func in algos.items():
            arr = worst.copy()
            _, steps = func(arr)
            results[name].append(steps)
            print(f" {steps:>12,}", end="")
        print()

    # Plot
    plt.figure(figsize=(10, 6))
    for name, counts in results.items():
        plt.plot(sizes, counts, marker='o', label=name)

    plt.xlabel("Input size n")
    plt.ylabel("Number of operations T(n)")
    plt.title("Worst-case Operation Counts T(n) vs Input Size")
    plt.grid(True, alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.yscale('log')
    plt.show()


# Step 4 – Timing vs n  (worst case) + plot

def step4_timing_plot():
    print("\n" + "="*75)
    print("STEP 4  –  Wall-clock time vs n   (worst-case input)")
    print("="*75)

    sizes = [200, 500, 800, 1000, 1200, 1500, 1800, 2000]

    algos = {
        "Bubble":    bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
        "Quick":     quick_sort,
    }

    results = {name: [] for name in algos}

    print(f"{'n':>6} |", end="")
    for name in algos:
        print(f" {name:>10}", end="")
    print()

    random.seed(47)

    for n in sizes:
        base = [random.randint(1, 200000) for _ in range(n)]
        worst = base[::-1]

        print(f"{n:6} |", end="")

        for name, func in algos.items():
            arr = worst.copy()
            start = time.perf_counter()
            func(arr)
            elapsed = time.perf_counter() - start
            results[name].append(elapsed)
            print(f" {elapsed:9.4f}s", end="")
        print()

    # Plot
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(sizes, times, marker='o', label=name)

    plt.xlabel("Input size n")
    plt.ylabel("Time (seconds)")
    plt.title("Worst-case Sorting Time vs Input Size")
    plt.grid(True, alpha=0.4)
    plt.legend()
    plt.tight_layout()
    plt.yscale('log')
    plt.show()


# Main – run everything

if __name__ == "__main__":
    step1_demo()
    step2_demo()
    step3_operation_plot()    # ← Step 3 plot of T(n)
    step4_timing_plot()       # ← Step 4 plot of time