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

import unittest
# from lab1 import wins_rock_scissors_paper, factorial, fibonacci, sum_to_goal,UpCounter,DownCounter
#from lab1another import wins_rock_scissors_paper, factorial, fibonacci, sum_to_goal,UpCounter,DownCounter

class Lab1TestCase(unittest.TestCase):
    """These are the test cases for functions and classes of lab1"""
    
    def test_win_rock_scissors_paper(self):
        self.assertEqual(wins_rock_scissors_paper("rock","scissors"),True)
        self.assertEqual(wins_rock_scissors_paper("rock","paper"),False)
        self.assertEqual(wins_rock_scissors_paper("scissors".upper(),"paper"),True)
        self.assertEqual(wins_rock_scissors_paper("Scissors","Rock"),False)
        self.assertEqual(wins_rock_scissors_paper("paper","sCiSsOrs"),False)
        self.assertEqual(wins_rock_scissors_paper("paper".title(),"ROCK"),True)
        self.assertEqual(wins_rock_scissors_paper("paper","PaPeR"),False)
        self.assertEqual(wins_rock_scissors_paper("rock","ROCK"),False)
        self.assertEqual(wins_rock_scissors_paper("SCISSORS","scissors"),False)


    def test_factorial(self):
        self.assertEqual(factorial(0),1)
        self.assertEqual(factorial(1),1)
        self.assertEqual(factorial(19),121645100408832000)
        self.assertEqual(factorial(8),40320)


    def test_fibonacci(self):
        self.assertEqual(fibonacci(0),0)
        self.assertEqual(fibonacci(1),1)
        self.assertEqual(fibonacci(2),1)
        self.assertEqual(fibonacci(3),2)