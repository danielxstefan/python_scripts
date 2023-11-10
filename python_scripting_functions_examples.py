Creating an Instance of the Other Class:
Instantiate an object of the other class and call its methods.


class ClassA:
    def method_a(self):
        print("Method A")

class ClassB:
    def method_b(self):
        # Creating an instance of ClassA
        instance_a = ClassA()
        # Calling method_a using the instance
        instance_a.method_a()

# Example usage
b = ClassB()
b.method_b()  # This will print "Method A"
Inheritance:
One class inherits from another, thus gaining access to the parent class's methods.

----------------------------------------------------------------------------------------------------
class ClassA:
    def method_a(self):
        print("Method A")

class ClassB(ClassA):
    def method_b(self):
        # Directly call method_a because ClassB inherits from ClassA
        self.method_a()

# Example usage
b = ClassB()
b.method_b()  # This will print "Method A"
Passing an Instance of the Other Class:
You pass an instance of one class to the method of another class.

----------------------------------------------------------------------------------------------------
class ClassA:
    def method_a(self):
        print("Method A")

class ClassB:
    def method_b(self, instance_a):
        # Calling method_a using the passed instance
        instance_a.method_a()

# Example usage
a = ClassA()
b = ClassB()
b.method_b(a)  # This will print "Method A"
Class Methods and Static Methods:
If the method in the other class doesn't need to access instance-specific data, 
you can define it as either a class method or a static method, which can then be called without instantiating the class.

----------------------------------------------------------------------------------------------------
class ClassA:
    @staticmethod
    def static_method_a():
        print("Static Method A")

class ClassB:
    def method_b(self):
        # Directly calling the static method of ClassA
        ClassA.static_method_a()

# Example usage
b = ClassB()
b.method_b()  # This will print "Static Method A"


----------------------------------------------------------------------------------------------------

Instantiation and Basic Method Calls:


class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# Instantiating and using the class
calc = Calculator()
print(calc.add(5, 3))  # 8
print(calc.subtract(5, 3))  # 2
Inheritance and Method Overriding:

----------------------------------------------------------------------------------------------------
class AdvancedCalculator(Calculator):
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b != 0:
            return a / b
        return "Division by zero error"

# Using the inherited and new methods
adv_calc = AdvancedCalculator()
print(adv_calc.multiply(6, 2))  # 12
print(adv_calc.divide(10, 0))  # Division by zero error
Composition (Using One Class Inside Another):

----------------------------------------------------------------------------------------------------
class Engineer:
    def __init__(self):
        self.calculator = AdvancedCalculator()

    def perform_calculation(self, operation, a, b):
        if operation == "add":
            return self.calculator.add(a, b)
        elif operation == "multiply":
            return self.calculator.multiply(a, b)
        # Add more operations as needed

# Using composition
eng = Engineer()
print(eng.perform_calculation("add", 10, 5))  # 15
print(eng.perform_calculation("multiply", 3, 4))  # 12
Class Methods and Static Methods:

----------------------------------------------------------------------------------------------------
class Utility:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @classmethod
    def create_zero_matrix(cls, rows, columns):
        return [[0 for _ in range(columns)] for _ in range(rows)]

# Using static and class methods
print(Utility.is_even(42))  # True
print(Utility.create_zero_matrix(2, 3))  # [[0, 0, 0], [0, 0, 0]]
Basic Sorting Algorithm (Bubble Sort as a Method):

----------------------------------------------------------------------------------------------------
class Sorting:
    def bubble_sort(self, arr):
        n = len(arr)
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
        return arr

# Using the sorting method
sort_instance = Sorting()
unsorted_array = [64, 34, 25, 12, 22, 11, 90]
print(sort_instance.bubble_sort(unsorted_array))  # Sorted array

----------------------------------------------------------------------------------------------------
Using Private Methods and Attributes:

class Account:
    def __init__(self, initial_balance):
        self.__balance = initial_balance  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            return True
        return False

    def __update_balance(self, amount):  # Private method
        self.__balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__update_balance(-amount)
            return True
        return False

    def get_balance(self):
        return self.__balance

# Using the Account class
acc = Account(100)
acc.deposit(50)
print(acc.get_balance())  # 150
acc.withdraw(70)
print(acc.get_balance())  # 80
Polymorphism and Abstract Classes:

----------------------------------------------------------------------------------------------------
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)

# Using polymorphism with abstract classes
rect = Rectangle(4, 5)
print(rect.area())  # 20
print(rect.perimeter())  # 18
Factory Method Pattern:

----------------------------------------------------------------------------------------------------
class Button:
    def click(self):
        raise NotImplementedError("Subclasses should implement this!")

class WindowsButton(Button):
    def click(self):
        return "Windows Button Clicked!"

class MacOSButton(Button):
    def click(self):
        return "MacOS Button Clicked!"

class ButtonFactory:
    @staticmethod
    def create_button(os_type):
        if os_type == "Windows":
            return WindowsButton()
        elif os_type == "MacOS":
            return MacOSButton()
        raise ValueError("Unknown OS type")

# Using the Factory Method
button = ButtonFactory.create_button("Windows")
print(button.click())  # Windows Button Clicked!
Decorator Pattern:

----------------------------------------------------------------------------------------------------
def uppercase_decorator(func):
    def wrapper(text):
        original_result = func(text)
        modified_result = original_result.upper()
        return modified_result
    return wrapper

class Greeting:
    @uppercase_decorator
    def say_hello(self, name):
        return f"Hello, {name}"

# Using the decorator pattern
greet = Greeting()
print(greet.say_hello("Alice"))  # HELLO, ALICE
Strategy Pattern:

----------------------------------------------------------------------------------------------------
from typing import List

class SortStrategy(ABC):
    @abstractmethod
    def sort(self, dataset: List[int]) -> List[int]:
        pass

class BubbleSortStrategy(SortStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        # Implementation of bubble sort
        # ...

class QuickSortStrategy(SortStrategy):
    def sort(self, dataset: List[int]) -> List[int]:
        # Implementation of quick sort
        # ...

class SortedList:
    def __init__(self, strategy: SortStrategy):
        self._strategy = strategy
        self._elements = []

    def add(self, value: int):
        self._elements.append(value)

    def sort(self):
        return self._strategy.sort(self._elements)

# Using the Strategy Pattern
sorted_list = SortedList(BubbleSortStrategy())
sorted_list.add(3)
sorted_list.add(1)
sorted_list.add(4)
print(sorted_list.sort())  # Sorted using Bubble Sort
----------------------------------------------------------------------------------------------------
