# calculator-project
Simple Console Calculator

This project is a console-based calculator built in Python. It was designed to take user inputs, perform arithmetic operations, and handle errors gracefully.

Project Overview

Purpose: To create a basic, interactive calculator that runs in the terminal.
Inputs: The user enters two numbers and selects an arithmetic operation (+, -, *, /, %). The program loops until the user types "stop."
Validation: Inputs are validated to ensure they’re numeric, with error handling for invalid input or division by zero.

My Thought Process and Learning Journey

When I started this project, I had a basic idea of what a calculator should do, but I was unsure how to handle input validation, loops, and error handling in a robust way. I began by writing a straightforward input and arithmetic system, but I quickly ran into issues with non-numeric inputs and repeated code.
To work through these challenges, I researched key concepts and explored different approaches. I learned how try-except blocks can handle input conversion safely, how a while loop can keep the calculator running until the user decides to stop, and why validating input before processing it makes a program more reliable. With each step, I reflected on the logic — why loops help avoid repeated restarts, why validation matters before converting to numbers, and how error handling makes the program robust even with invalid input.

How I Built It

1.Initial Inputs: I began by taking user input as strings.
2.Validation: I used a try-except block to safely convert input to floats, ensuring any non-numeric input was caught.
3.Loop Structure: I used a while True loop to repeatedly ask for inputs, so the user could perform multiple calculations until they typed "stop."
4.Operators: I handled each arithmetic operation with conditionals and ensured special cases, like division by zero, were checked.
5.Error Handling: If invalid input was entered, the program would inform the user and prompt them again instead of crashing

How to Run

1.Ensure you have Python installed (version 3.x).
2.Save the script as a .py file (e.g., calculator.py).
3.Run the script using the terminal:
4.python calculator.py
5.Follow the prompts to enter numbers and operations

Next Steps

I plan to improve this project by:

1.Adding more operations (like exponents or parentheses).
2.Refactoring code into functions for better organization.
3.Adding a simple GUI in the future using a library like Tkinter.
