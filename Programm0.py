import random

class LogIn:
    def __init__(self):
        self.logged_in = False
        self.username = ""
        self.password = ""

    def log_in(self):
        self.username = input("Create username: ")
        self.password = input("Create your password: ")

        if self.username.lower() == "none":
            print("Error. Your username cannot contain 'None'")
            return False

        if self.password.lower() == "none":
            print("Your password cannot be 'None'")
            return False

        self.logged_in = True
        return True

    def show(self):
        print("Your username is: ", self.username, "and your password is: ", self.password)

class Calculator:
    def __init__(self):
        pass

    @staticmethod
    def information():
        print("Press 'q' in the 'Input operation' field to quit")
        print("Press 'r' to reset")

    @staticmethod
    def result_operation(result):
        print(result)

    @staticmethod
    def close():
        close_program = input("Press 'q' to quit: ")
        if close_program.lower() == "q":
            print("The program will be closed")

    @staticmethod
    def exit_program():
        user_input = input("Do you want to exit the program? (Yes or No): ")
        if user_input.lower() == "yes":
            Calculator.close()
        else:
            Calculator.calculator()

    @staticmethod
    def reset():
        print("Numbers were reset")
        return None

    @staticmethod
    def perform_operation(num1, num2, operation):
        if operation == "+":
            return num1 + num2
        elif operation == "-":
            return num1 - num2
        elif operation == "*":
            return num1 * num2
        elif operation == "/":
            if num2 == 0:
                print("Error: Division by zero")
                return None
            return num1 / num2

    @staticmethod
    def calculator():
        Calculator.information()
        result = None

        while True:
            first_number = float(input("Input number: "))
            operation = input("Input operation: ")

            if operation == "q":
                Calculator.exit_program()
                break
            elif operation == "r":
                Calculator.reset()
                break

            if operation not in ["+", "-", "*", "/"]:
                print("Invalid operation. Please enter +, -, *, / or q to quit.")
                continue

            second_number = float(input("Input number: "))
            result = Calculator.perform_operation(first_number, second_number, operation)

            l = input("To see result press '=': ")

            if l == "=":
                if result is not None:
                    Calculator.result_operation(result)
                    break
            elif l == "q":
                Calculator.exit_program()
                break

class LogOut:
    @staticmethod
    def log_out():
        print('Write "exit" to log out')
        exit_program = input()
        if exit_program.lower() == "exit":
            print("Program will be closed")

class Choose:
    @staticmethod
    def choose():
        print("To open calculator press 'c'")
        print("To open random press 'r'")

class RandomNumber:
    @staticmethod
    def random_number():
        random_number = random.randint(0, 100)
        print('Your random number is:', random_number)

class Operation:
    @staticmethod
    def operation():
        Choose.choose()
        operation_choice = input()

        if operation_choice == "c":
            log_in_instance = LogIn()
            if log_in_instance.log_in():
                Calculator.calculator()
        elif operation_choice == "r":
            log_in_instance = LogIn()
            if log_in_instance.log_in():
                RandomNumber.random_number()
        else:
            print("Invalid choice. Exiting program.")

Operation.operation()
