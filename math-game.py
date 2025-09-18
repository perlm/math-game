# important program for math practice

from random import randint, choice
from math import factorial
from time import sleep
from os import system
from sys import exit

# TODO(): Move problem definitions to one place. Make it easier to add new types.


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


class Game:
    def __init__(self):
        self.PROBLEMS = 10
        self.TYPE = 0
        self.DIFFICULTY = 0
        self.STATUS = 0

        self.bcolors = [
            "filler" "\033[95m",
            "\033[94m",
            "\033[96m",
            "\033[92m",
            "\033[93m",
            "\033[91m",
            "\033[3m",
            "\033[1m",
            "\033[4m",
            "\033[5m",
            "\033[6m",
        ]
        self.ENDC = "\033[0m"
        self.choose_type()
        self.play_game()

    def print_format(self, message):
        if self.STATUS:
            if self.STATUS < len(self.bcolors):
                message = self.bcolors[self.STATUS] + message + self.ENDC
        print(message)

    def choose_type(self):
        while True:
            message = """
                        What type of game?
                        0  - Random!
                        1  - Addition
                        2  - Subtraction
                        3  - Multiplication
                        4  - Division
                        5  - Squares
                        6  - Factorial
                        7  - Square Perimeter
                        8  - Cube
                        9  - Primes
                        10 - Rectangle Perimeter
                        11 - Power of Ten
                        12 - Square Root
                        13 - Algebra
                        14 - Statistics
                        15 - Fibonaci
                        16 - Big Number Party
                        """
            self.print_format(message)
            entry = input()

            try:
                entry = int(entry)
                if entry not in [i for i in range(17)]:
                    self.print_format("0 - 16 only")
                else:
                    self.TYPE = entry
                    break
            except:
                self.print_format("Not Valid")

        while True:
            message = """
                        Who is playing?
                        1 - Livy
                        2 - Hazel
                        """
            self.print_format(message)
            entry = input()
            try:
                entry = int(entry)
                if entry not in [1, 2]:
                    self.print_format("1 or 2 only")
                else:
                    #self.DIFFICULTY = entry
                    self.DIFFICULTY = 2
                    break
            except:
                self.print_format("Not Valid")

    def define_problem(self):
        if self.TYPE == 0:
            self.problem_type = choice([i+1 for i in range(16)])
        else:
            self.problem_type = self.TYPE

        if self.problem_type == 1:
            # addition
            #self.num1 = randint(0, 10 ** self.DIFFICULTY)
            #self.num2 = randint(0, 10 ** self.DIFFICULTY)
            self.num1 = randint(0, 10 ** 2)
            self.num2 = randint(0, 10 ** 2)
            self.solution = self.num1 + self.num2
        elif self.problem_type == 2:
            # subtraction
            #self.num1 = randint(0, 10 ** self.DIFFICULTY)
            #self.num2 = randint(0, 10 ** self.DIFFICULTY)
            self.num1 = randint(0, 10 ** 2)
            self.num2 = randint(0, 10 ** 2)
            if self.num2 > self.num1:
                _ = self.num1
                self.num1 = self.num2
                self.num2 = _
            self.solution = self.num1 - self.num2
        elif self.problem_type == 3:
            # multiplication
            self.num1 = randint(1, 10 ** 1)
            self.num2 = randint(1, 10 ** 1)
            self.solution = self.num1 * self.num2
        elif self.problem_type == 4:
            # division
            x1 = randint(1, 10 ** 1)
            x2 = randint(1, 10 ** 1)
            x3 = x1 * x2
            self.solution = x1
            self.num1 = x3
            self.num2 = x2
        elif self.problem_type == 5:
            # squares
            self.num1 = randint(1, 13)
            self.num2 = 2
            self.solution = self.num1 ** self.num2
        elif self.problem_type == 6:
            # Factorial
            self.num1 = randint(0, 5)
            self.num2 = 0
            self.solution = factorial(self.num1)
        elif self.problem_type == 7:
            # square perimeter
            self.num1 = randint(1, 10 ** 1)
            self.num2 = 0
            self.solution = self.num1 * 4
        elif self.problem_type == 8:
            # cubes
            self.num1 = randint(1, 5)
            self.num2 = 3
            self.solution = self.num1 ** self.num2
        elif self.problem_type == 9:
            # next prime
            self.num2 = 0
            self.num1 = randint(4, 10 ** self.DIFFICULTY)
            if self.num1 % 2 == 1:
                self.num1 += 3
            i = self.num1
            while True:
                if is_prime(i):
                    self.solution = i
                    break
                else:
                    i += 1
        elif self.problem_type == 10:
            # perimeter of rectangle
            #self.num1 = randint(0, 10 ** self.DIFFICULTY)
            self.num1 = randint(0, 10 ** 2)
            self.num2 = randint(0, 10 ** 1)
            self.solution = self.num1 + self.num1 + self.num2 + self.num2
        elif self.problem_type == 11:
            # powers of ten
            self.num1 = 10
            self.num2 = randint(0, 6)
            self.solution = self.num1 ** self.num2
        elif self.problem_type == 12:
            # square root
            self.solution = randint(1, 13)
            self.num2 = 2
            self.num1 = self.solution ** self.num2
        elif self.problem_type == 13:
            # algebra
            self.solution = randint(1, 10)
            self.num1 = randint(1, 10)
            self.num2 = randint(1, 10 ** 1)
            self.num3 = self.solution * self.num1 + self.num2
        elif self.problem_type == 14:
            # statistics
            length = 5
            self.solution = randint(length, length * 2)
            nums = []
            total = self.solution * length
            for i in range(length-1):
                n = randint(0,total-length)
                total = total - n
                nums.append(n)
            nums.append(total)
            self.nums = nums
        elif self.problem_type == 15:
            # Fibonaci
            # I copied this
            fib = lambda n: n if n < 2 else fib(n-1) + fib(n-2)
            self.num = randint(6,15)
            self.solution = fib(self.num)
        elif self.problem_type == 16:
            index = randint(0,7)
            self.val = ['hundred','thousand', 'ten thousand','hundred thousand','million','ten million','hundred million','billion'][index]
            self.solution = 10**(index+2)
        else:
            # triangle-> a2+b2=c3. diameter=2x radius. rounding?
            # log(billion). meters-km-cm.
            # square roots
            pass

    def print_problem(self):
        if self.problem_type == 1:
            message = f"{self.num1} + {self.num2} = ?"
        elif self.problem_type == 2:
            message = f"{self.num1} - {self.num2} = ?"
        elif self.problem_type == 3:
            c = choice([1, 2, 3])
            if c == 1:
                message = f"{self.num1} * {self.num2} = ?"
            elif c == 2:
                message = f"Area of a rectangle with sides of length {self.num1} and {self.num2} = ?"
            else:
                message = f"If a car has a speed of {self.num1} miles per hour, how many miles will it travel in {self.num2} hours?"
        elif self.problem_type == 4:
            message = f"{self.num1} / {self.num2} = ?"
        elif self.problem_type == 5:
            if choice([1, 2]) == 1:
                message = f"{self.num1} \N{SUPERSCRIPT TWO} = ?"
            else:
                message = f"Area of a square with sides of length {self.num1} = ?"
        elif self.problem_type == 6:
            message = f"{self.num1}! = ?"
        elif self.problem_type == 7:
            message = f"Perimeter of a square with sides of length {self.num1} = ?"
        elif self.problem_type == 8:
            if choice([1, 2]) == 1:
                message = f"{self.num1} \N{SUPERSCRIPT THREE} = ?"
            else:
                message = f"Volume of a cube with sides of length {self.num1} = ?"
        elif self.problem_type == 9:
            message = f"What is the next prime number after {self.num1} = ?"
        elif self.problem_type == 10:
            message = f"Perimeter of a rectangle with sides of length {self.num1} and {self.num2} = ?"
        elif self.problem_type == 11:
            if self.num2 == 1:
                message = f"{self.num1}" + chr(0x00B9)
            elif 2 <= self.num2 <= 3:
                message = f"{self.num1}" + chr(0x00B0 + self.num2)
            else:
                message = f"{self.num1}" + chr(0x2070 + self.num2)
        elif self.problem_type == 12:
            if choice([1, 2]) == 1:
                message = f"x \N{SUPERSCRIPT TWO} = {self.num1}\nWhat is x?"
            else:
                message = f"Side length of a square with area {self.num1} = ?"
        elif self.problem_type == 13:
            message = f"x*{self.num1} + {self.num2} = {self.num3}\nWhat is x?"
        elif self.problem_type == 14:
            message = f"What is the average (mean) of {str(self.nums)}?"
        elif self.problem_type == 15:
            message = f"The Fibonaci sequence starts 1,1,2,3,5... What is number {self.num} in the sequence?"
        elif self.problem_type == 16:
            message = f"How big is {self.val}?"
        else:
            message = f"Problem type {self.problem_type} not found."
        self.print_format(message)

    def play_game(self):
        for x in range(self.PROBLEMS):
            self.define_problem()
            guess_count = 0
            while True:
                system("clear")
                message = f"Problem {x+1} of {self.PROBLEMS}!"
                self.print_format(message)

                self.print_problem()

                guess = input()

                try:
                    guess = int(guess)
                except:
                    message = "numbers only1"
                    self.print_format(message)
                    self.STATUS = 0
                    sleep(2)

                if guess == self.solution and guess_count == 0:
                    self.STATUS += 1
                    message = "FIRST TRY! :-D"
                    self.print_format(message)
                    sleep(2)
                    break
                elif guess == self.solution:
                    self.print_format("Good Job!")
                    sleep(2)
                    break
                else:
                    self.STATUS = 0
                    message = "Nope. Try again!"
                    self.print_format(message)
                    guess_count += 1
                    sleep(2)
        self.print_format("All done!!!")
        sleep(3)


if __name__ == "__main__":
    Game()
