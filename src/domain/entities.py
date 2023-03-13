import unittest


class Expense:
    def __init__(self, day: int, money: int, type: str):
        self.__day = day
        self.__money = money
        self.__type = type

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        self.__day = value

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        self.__money = value

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def __str__(self):
        return f"{self.__day} - {self.__money} lei - {self.__type}"


def test_expense():
    new_expense = Expense(30, 23, "food")
    assert new_expense.day == 30
    assert new_expense.money == 23
    assert new_expense.type == "food"
    assert str(new_expense) == "30 - 23 lei - food"

