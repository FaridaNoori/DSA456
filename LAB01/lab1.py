print("Hello, world!")

# Function 1
def wins_rock_scissors_paper(player, opponent):
    p = player.lower()
    o = opponent.lower()

    if p == o:
        return False

    if p == "rock" and o == "scissors":
        return True
    if p == "paper" and o == "rock":
        return True
    if p == "scissors" and o == "paper":
        return True

    return False


# Function 2
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


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


class UpCounter:
    def __init__(self, stepsize=1):
        self.stepsize = stepsize
        self.value = 0

    def count(self):
        return self.value

    def update(self):
        self.value += self.stepsize


class DownCounter(UpCounter):
    def update(self):
        self.value -= self.stepsize


"""Working on this lab helped me get more comfortable with Python. One thing I liked about Python is how simple and readable the syntax is. I was able to focus more on the logic of the functions instead of worrying about things like data types or memory management. Writing loops and working with strings and lists felt much easier than in other languages.
One thing I didn’t like is that Python is dynamically typed, so some mistakes only show up when the program runs. This can make debugging harder compared to languages that catch errors at compile time. Something that also surprised me at first was how Python handles loops and formatting without braces or semicolons, which is very different from what I’m used to.
Compared to C/C++, Python is much faster to write and easier to read, but it offers less control over memory and performance. The overall program structure is similar, but Python allows me to write cleaner code with fewer lines. This changes how I approach programming, since I can focus more on solving the problem rather than managing low-level details."""