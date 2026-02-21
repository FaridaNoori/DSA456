import random
import time
import matplotlib.pyplot as plt

# ────────────────────────────────────────────────
# Sorting functions 
# ────────────────────────────────────────────────

def bubble_sort(my_list):
    n = len(my_list)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if my_list[j] > my_list[j + 1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                swapped = True
        if not swapped:
            break
    return my_list


def selection_sort(my_list):
    n = len(my_list)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if my_list[j] < my_list[min_idx]:
                min_idx = j
        my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
    return my_list


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        key = my_list[i]
        j = i - 1
        while j >= 0 and my_list[j] > key:
            my_list[j + 1] = my_list[j]
            j -= 1
        my_list[j + 1] = key
    return my_list


def quick_sort(my_list):
    def partition(arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quicksort_helper(arr, low, high):
        if low < high:
            pi = partition(arr, low, high)
            quicksort_helper(arr, low, pi - 1)
            quicksort_helper(arr, pi + 1, high)

    quicksort_helper(my_list, 0, len(my_list) - 1)
    return my_list


# ────────────────────────────────────────────────
# Benchmarking
# ────────────────────────────────────────────────

algorithms = {
    "Bubble": bubble_sort,
    "Selection": selection_sort,
    "Insertion": insertion_sort,
    "Quick": quick_sort
}

sizes = [100, 250, 500, 1000, 2000, 3000, 4000]

times = {name: [] for name in algorithms}

random.seed(42)  # reproducible

print("Measuring worst-case sorting times...\n")

for n in sizes:
    # random list, then reverse it → worst case for bubble/insertion
    base = [random.randint(0, 10000) for _ in range(n)]
    worst = base[::-1]   # or sorted(base, reverse=True)

    print(f"n = {n:5,} ", end="")
    
    for name, sort_func in algorithms.items():
        lst = worst.copy()  # fresh copy each time
        start = time.perf_counter()
        sort_func(lst)
        end = time.perf_counter()
        
        elapsed = end - start
        times[name].append(elapsed)
        
        print(f"  {name:9} {elapsed:8.4f}s", end="")
    
    print()  # new line after each size

# ────────────────────────────────────────────────
# Plotting
# ────────────────────────────────────────────────

plt.figure(figsize=(10, 6))

for name, t_list in times.items():
    plt.plot(sizes, t_list, marker='o', label=name)

plt.xlabel("List size n")
plt.ylabel("Time (seconds)")
plt.title("Worst-case Sorting Time vs Input Size n")
plt.grid(True, linestyle='--', alpha=0.7)
plt.legend()
plt.tight_layout()

# plt.yscale('log')

plt.show()