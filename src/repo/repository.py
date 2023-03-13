import copy
import pickle
import os
import json
from json import JSONEncoder
import unittest
from src.domain.entities import Expense
FIRST_INDEX = 0
SECOND_INDEX = 1
THIRD_INDEX = 2

class Repository:
    def __init__(self):
        self.__all_expenses = []
        self.__history = []

    def get_list_of_expenses(self):
        return self.__all_expenses

    def save_expense(self, expense):
        self.__all_expenses.append(expense)
        self.__history.append(copy.deepcopy(self.__all_expenses))

    def filter_list(self, value):
        new_list_of_expenses = []
        for expense in self.__all_expenses:
            if expense.money > value:
                new_list_of_expenses.append(expense)
        self.__all_expenses.clear()
        self.__all_expenses.extend(new_list_of_expenses)
        self.__history.append(copy.deepcopy(self.__all_expenses))

    def undo(self):
        if len(self.__all_expenses) > 0:
            self.__history.pop()
            self.__all_expenses.clear()
            if len(self.__history) > 0:
                self.__all_expenses.extend(self.__history[-1])

class BinaryRepository(Repository):
    def __init__(self, file_name="expenses.bin"):
        super().__init__()
        self._file_name = file_name
        if os.stat("expenses.bin").st_size != 0:
            self._load_file()

    def _load_file(self):
        file_input = open(self._file_name, "rb")
        expenses = pickle.load(file_input)
        for expense in expenses:
            super().save_expense(expense)
        file_input.close()

    def _save_file(self):
        file_output = open(self._file_name, "wb")
        pickle.dump(self.get_list_of_expenses(), file_output)
        file_output.close()

    def save_expense(self, expense):
        super().save_expense(expense)
        self._save_file()

    def filter_list(self, value):
        super().filter_list(value)
        self._save_file()

    def undo(self):
        super().undo()
        self._save_file()

class TextFileRepository(Repository):
    def __init__(self, file_name = "expenses.txt"):
        super().__init__()
        self._file_name = file_name
        if os.stat("expenses.txt").st_size != 0:
            self._load_file()

    def _load_file(self):
        lines = []
        try:
            file_input = open(self._file_name, "rt")
            lines = file_input.readlines()
            file_input.close()
        except IOError:
            pass
        for line in lines:
            current_line = line.split(",")
            new_expense = Expense(int(current_line[FIRST_INDEX].strip()), int(current_line[SECOND_INDEX].strip()), current_line[THIRD_INDEX].strip())
            super().save_expense(new_expense)

    def _save_file(self):
        file_output = open(self._file_name, "wt")
        for expense in self.get_list_of_expenses():
            expense_string = str(expense.day) + "," + str(expense.money) + "," + str(expense.type) + "\n"
            file_output.write(expense_string)
        file_output.close()

    def save_expense(self, expense):
        super().save_expense(expense)
        self._save_file()

    def filter_list(self, value):
        super().filter_list(value)
        self._save_file()

    def undo(self):
        super().undo()
        self._save_file()

class ExpenseEncoder(JSONEncoder):
    def default(self, object):
        return object.__dict__

class JSONFileRepository(Repository):
    def __init__(self, file_name = "expenses.json"):
        super().__init__()
        self._file_name = file_name
        if os.stat("expenses.json").st_size != 0:
            self._load_file()

    def _load_file(self):
        file_input = open(self._file_name, "r")
        expenses = json.load(file_input)
        for expense in expenses:
            expense = Expense(expense['_Expense__day'], expense['_Expense__money'], expense['_Expense__type'])
            super().save_expense(expense)
        file_input.close()

    def _save_file(self):
        file_output = open(self._file_name, "w")
        json.dump(self.get_list_of_expenses(), file_output, cls=ExpenseEncoder)
        file_output.close()

    def save_expense(self, expense):
        super().save_expense(expense)
        self._save_file()

    def filter_list(self, value):
        super().filter_list(value)
        self._save_file()

    def undo(self):
        super().undo()
        self._save_file()


