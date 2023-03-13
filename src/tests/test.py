import unittest

from src.domain.entities import Expense
from src.repo.repository import Repository


class TestRepository(unittest.TestCase):
    def test_save_expense(self):
        repo = Repository()
        repo.save_expense(Expense(3,4,"food"))
        for expense in repo.get_list_of_expenses():
            self.assertEqual(expense.day, 3)
            self.assertEqual(expense.money, 4)
            self.assertEqual(expense.type, "food")