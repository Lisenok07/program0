import random

class calculator:

    @staticmethod
    def abc():
        print("Press 'q' in the 'Input operation' field to quit")
        print("Press 'r' to reset")

    @staticmethod
    def result_operation(Result):
        print(Result)

    @staticmethod
    def close():
        CloseProgramm = input("Press 'q' to quit: ")
        if CloseProgramm.lower() == "q":
            print("The program will be closed")

    @staticmethod
    def exit_p():
        e = input("Do you want to exit the program? (Yes or No): ")
        if e.lower() == "yes":
            calculator.close()
        else:
            calculator.calculator()

    @staticmethod
    def reset():
        print("Numbers were reset")
        return None

    @staticmethod
    def perform_operation(num1, num2, Operation):
        if Operation == "+":
            return num1 + num2
        elif Operation == "-":
            return num1 - num2
        elif Operation == "*":
            return num1 * num2
        elif Operation == "/":
            return num1 / num2
        elif Operation == "/":
            if num2 == 0:
                print("Error: Division by zero")
                return None
            return num1 / num2

    @staticmethod
    def calculator():
        calculator.abc()
        CloseProgramm = None
        Result = None
        error = None
        l = None
        while CloseProgramm != "q":
            FirstNumber = float(input("Input number: "))
            Operation = input("Input operation: ")

            if Operation != "q" and Operation != "r":
                SecondNumber = float(input("Input number: "))
            else:
                if (Operation == "r"):
                    calculator.reset()
                    break
                if (Operation == "q"):
                    calculator.exit_p()
                    break

            while (l != "="):
                if Operation in ["+", "-", "*", "/"]:
                    Result = calculator.perform_operation(FirstNumber, SecondNumber, Operation)
                    print ("To continue write +,/,*,-")
                    l = input("To see result press =:")
                    if l == "=":
                        if Result is not None:
                            calculator.result_operation(Result)
                            break
                        else:
                            calculator.calculator()
                    elif l == "w":
                        continue
                    else:
                        error = True
                        print ("Error1")
                        break
                    if l in ["+", "-", "*", "/"]:
                        Result = calculator.perform_operation(FirstNumber, SecondNumber, Operation)
                        calculator.calculator()
                        continue
                    else:
                        error = True
                        print("Error2")
                elif Operation == "r":
                    calculator.reset()
                    break

            else:
                error = True
                print("Error3")
                break

        if CloseProgramm != "q" and error is None:
            print(Result if Result is not None else 0)
        if Operation == "q":
            calculator.exit_p()
            calculator.close()


class log_in_out:

    class log_out:
        @staticmethod
        def log_out():
            global log_out
            log_out = True
            global log_in
            log_in = False
            print('Write exit to log out')
            exitProgramm = input ()
            if exitProgramm == "exit":
                print("Programm will be closed")

    class choose:
        @staticmethod
        def choose():
            print ("To open calculator press c")
            print ("To open random press r")

    class log_in:
        @staticmethod
        def log_in():
            global log_in
            log_in = True
            userName = input("Create username: ")
            password = input ("Create your passwod: ")
            if userName == "None":
                print ("Error. Your username cannot contain this")
                log_in = False

            else:
                userName1 = userName
            if password == "None":
                print ("Your password cannot be ""None""")
            else:
                password1 = password

            @staticmethod
            def show():
                print ("Your username is: ",userName1, "and your password is: ", password1)

            @staticmethod
            def see_name_and_password():
                print ("Do you want to see password and username?")
                see_name_and_password = input ("Write """"yes """"or """"no: """)
                if see_name_and_password == "yes":
                    show()
            see_name_and_password()
    choose.choose()
class randomNumber:
    @staticmethod
    def randomNumber ():
        randomNumber = random.randint(0,100)
        print ('Your random number is: ')
        print (randomNumber)
class Operation:
    @staticmethod
    def Operation ():
        Operation = input ()
        if Operation == "c":
            log_in()
            calculator.calculator()
        elif Operation == "r":
            log_in()
            randomNumber.randomNumber()
        else:
            log_in()
Operation.Operation()

class LogOut:
    @staticmethod
    def LogOut():
        print ("Do you want log out?")
        exit_p = input()
        if exit_p == "yes":
            log_out = True
            log_in = False
            log_out.log_out()

LogOut.LogOut()