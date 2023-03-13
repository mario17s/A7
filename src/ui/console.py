MINIMUM_DAY = 1
MAXIMUM_DAY = 30
MINIMUM_MONEY = 1

def print_options():
    print("1. Add an expense")
    print("2. Display the list of expenses.")
    print("3. Filter the list so that it contains only expenses above a certain value read from the console.")
    print("4. Undo the last operation that modified program data.")
    print("5. Exit")

class Console:
    def __init__(self, expense_service):
        self.__expense_service = expense_service

    def __print_all_expenses(self):
        all_expenses = self.__expense_service.get_all()
        for expense in all_expenses:
            print(expense)

    def __add_expenses(self):
        day = input("enter the day ")
        money = input("enter the value ")
        type = input("enter the type ")
        try:
            day = int(day)
            money = int(money)
            if day < MINIMUM_DAY or day > MAXIMUM_DAY:
                raise ValueError("invalid day")
            if money < MINIMUM_MONEY:
                raise ValueError("invalid amount of money")
            self.__expense_service.add_expense(day, money, type)
        except ValueError as ve:
            print(ve)
        
    def __filter_list_of_expenses(self):
        value = input("enter the value ")
        try:
            value = int(value)
            if value < MINIMUM_MONEY:
                raise ValueError("invalid value")
            self.__expense_service.filter_expenses(value)
        except ValueError as ve:
            print(ve)
        
    def __undo_operation(self):
        self.__expense_service.undo()
        
    def run_console(self):
        while True:
            print_options()
            option = int(input("enter an option "))
            if option == 1:
                self.__add_expenses()
            elif option == 2:
                self.__print_all_expenses()
            elif option == 3:
                self.__filter_list_of_expenses()
            elif option == 4:
                self.__undo_operation()
            elif option == 5:
                break