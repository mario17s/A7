import os
import random

from src.domain.entities import Expense

MINIMUM_DAY = 1
MAXIMUM_DAY = 30
MINIMUM_MONEY = 1
MAXIMUM_MONEY = 1000
MINIMUM_INDEX = 0
MAXIMUM_INDEX = 4
MINIMUM_GENERATION_VALUE = 0
MAXIMUM_GENERATION_VALUE = 10

class ExpenseService:
    def __init__(self, repository):
        self.__repository = repository
        try:
            if os.stat(self.__repository._file_name).st_size == 0:
                for index in range(MINIMUM_GENERATION_VALUE, MAXIMUM_GENERATION_VALUE):
                    day = random.randint(MINIMUM_DAY, MAXIMUM_DAY)
                    money = random.randint(MINIMUM_MONEY, MAXIMUM_MONEY)
                    types = ["food", "transport", "internet", "shopping", "school"]
                    type = types[random.randint(MINIMUM_INDEX, MAXIMUM_INDEX)]
                    self.add_expense(day, money, type)

        except AttributeError:
            for index in range(MINIMUM_GENERATION_VALUE, MAXIMUM_GENERATION_VALUE):
                day = random.randint(MINIMUM_DAY, MAXIMUM_DAY)
                money = random.randint(MINIMUM_MONEY, MAXIMUM_MONEY)
                types = ["food", "transport", "internet", "shopping", "school"]
                type = types[random.randint(MINIMUM_INDEX, MAXIMUM_INDEX)]
                self.add_expense(day, money, type)

    def add_expense(self, day, money, type):
        new_expense = Expense(day, money, type)
        self.__repository.save_expense(new_expense)

    def get_all(self):
        return self.__repository.get_list_of_expenses()

    def filter_expenses(self, value):
        self.__repository.filter_list(value)

    def undo(self):
        self.__repository.undo()