""" 

Function 1
def function1(number):
    total = 0
    for i in range(number):
        x = i + 1
        total += x * x
    return total

Input size: Let n = number (assume n ≥ 0).
Analysis:

The loop runs exactly n times (i = 0 to n-1).
Inside the loop there are a constant number of basic operations:
1 addition (i + 1)
1 multiplication (x * x)
1 addition and assignment (total += ...)

All these are O(1) per iteration.

Total operations ≈ c × n for some constant c (roughly 3–4 primitive operations per loop iteration)
→ T(n) = Θ(n)
Final complexity: O(n) (linear)
Note: This function actually computes the sum of squares formula result: 1² + 2² + … + n².



Function 2
def function2(number):
    return (number * (number + 1) * (2 * number + 1)) // 6


Input size: Let n = number.
Analysis:

Only a fixed number of arithmetic operations appear: 4 multiplications, 2 additions, 1 integer division, and 1 subtraction (inside 2*number+1).
No loops or recursion.
All operations are performed exactly once, regardless of how large n is.

Total operations = constant (e.g. ≈ 7–8 primitive arithmetic steps)
→ T(n) = Θ(1)
Final complexity: O(1) (constant time)
Note: This is the closed-form formula for the sum of squares: 1² + 2² + … + n² — exactly what function1 computes, but very efficiently.


Function 3
def function3(list):
    n = len(list)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if list[j] > list[j+1]:
                tmp = list[j]
                list[j] = list[j+1]
                list[j + 1] = tmp


Input size: Let n = len(list) (assume n ≥ 1).
Analysis — this is bubble sort (without the early termination optimization):
Outer loop: runs n−1 times (i = 0 to n-2)
Inner loop: for each i, runs n−1−i times
Number of comparisons (and potential swaps):

When i=0: n−1 comparisons
When i=1: n−2 comparisons
...
When i=n-2: 1 comparison

Total number of comparisons = (n−1) + (n−2) + … + 1 = n(n−1)/2
Each comparison is followed by at most 3 assignments (in the worst case when a swap occurs).
Total operations ≈ 3 × n(n−1)/2 + lower order terms ≈ (3/2) n² − (3/2) n
Dominant term is clearly n².
→ T(n) = Θ(n²) in the worst and average case
Final complexity: O(n²) (quadratic)


Function 4
def function4(number):
    total = 1
    for i in range(1, number):
        total *= i + 1
    return total


Input size: Let n = number (assume n ≥ 1).
Analysis:

The loop runs from i=1 to i=n−1 → exactly n−1 iterations.
In each iteration: one multiplication (total *= i + 1) and one addition (i + 1).
Both are O(1) per iteration (assuming standard integer multiplication cost; note that for very large n the numbers become huge and multiplication cost grows, but in basic analysis we treat arithmetic as O(1)).

Total operations ≈ c × (n−1) for some constant c
→ T(n) = Θ(n)
Final complexity: O(n) (linear)
Note: This function computes n! (n factorial), starting from 1 and multiplying by 2, 3, …, n.



"""

"PART B"

# Function 3
def Fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    a = 0
    b = 1
    for _ in range(2, n + 1):
        c = a + b
        a = b
        b = c
    return b


# Function 4
def sum_to_goal(numbers, goal):
    length = len(numbers)
    for i in range(length):
        for j in range(i + 1, length):
            if numbers[i] + numbers[j] == goal:
                return numbers[i] * numbers[j]
    return 0


"""Reflection

Considering the solutions you saw in the lab 1 code, what differences did you see between the fastest and slowest versions?
For sum_to_number (or sum_to_goal)
The fastest version (e.g. ~0.003 seconds in our group) used a closed-form mathematical formula:
return goal * (goal + 1) // 2 (Gauss's formula for the sum of first n natural numbers).
This runs in constant time O(1) — only a few arithmetic operations, no matter how large the input is.The slowest version (e.g. ~0.614 seconds) used a loop that adds numbers one by one:Pythontotal = 0
for i in range(1, goal + 1):
    total += i
return totalThis is linear time O(n) — the loop runs goal times, so larger inputs take proportionally longer.The key difference was not syntax or small optimizations, but the algorithmic approach: formula (O(1)) vs. iterative accumulation (O(n)).
For fibonacci
The fastest version in our group (~2.805 seconds) was an iterative (bottom-up) approach using a loop with two variables:Pythona, b = 0, 1
for _ in range(n):
    a, b = b, a + b
return aThis runs in linear time O(n) and avoids repeated work.The slowest version (~5.659 seconds) was the classic naive recursive implementation:Pythondef fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)This has exponential time complexity O(φⁿ) (where φ ≈ 1.618), because it recomputes the same Fibonacci numbers many times (creating an enormous call tree with massive redundancy).The dominant difference was the choice of algorithm: iteration (efficient, no redundancy) vs. naive recursion (extremely redundant computation).

Was there a difference in terms of the usage of space resources? Did one algorithm use more/less space (memory)?
sum_to_number / sum_to_goal
Both the formula version and the loop version use O(1) space (constant memory).
Only a few variables are needed (total, maybe loop counter).
No difference in space usage — the huge time difference comes purely from time complexity, not memory.

fibonacci
Iterative version: O(1) space — only uses a constant number of variables (two or three integers), regardless of n.
Naive recursive version: O(n) space in the call stack (worst-case depth is n when it goes down the leftmost path: fib(n) → fib(n-1) → … → fib(1)).
For large n (e.g. n > 1000–5000 depending on system stack size), it can cause stack overflow errors.
→ The recursive version uses significantly more space (linear in n) compared to the iterative version (constant space).


What sort of conclusions can you draw based on your observations?
Choosing the right algorithm matters far more than small coding style differences (e.g. using += vs = x + 1, list comprehensions vs loops, etc.). A change from exponential → linear or linear → constant can improve performance by orders of magnitude.
Naive recursion looks elegant and matches the mathematical definition, but it is usually impractical for anything beyond small inputs due to both terrible time (exponential) and extra space (call stack) costs. Iteration or dynamic programming is almost always better for sequences like Fibonacci.
Mathematical closed-form solutions (when they exist) are ideal — they give O(1) time with O(1) space, as seen in the sum formula.
Time vs. space trade-offs exist, but in these examples the fastest solutions also used the least (or equal) space — there was no need to sacrifice memory to gain speed.
Writing efficient code early helps: even moderate inputs (e.g. n = 40 for Fibonacci) can make an exponential algorithm unusable, while linear or constant versions finish instantly.
These labs show why we study Big-O notation — real performance differences between O(1), O(n), and O(φⁿ) are dramatic and easy to observe even on student machines."""