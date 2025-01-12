import unittest
from unittest.mock import patch
from io import StringIO
import sys


import bank_app

class TestBankApp(unittest.TestCase):
    def setUp(self):
        # Reset balance before each test
        bank_app.balance = 0.0

    def test_initial_balance(self):
        self.assertEqual(bank_app.balance, 0.0)

    @patch('sys.stdout', new_callable=StringIO)
    def test_show_balance(self, mock_stdout):
        bank_app.balance = 100.0
        bank_app.show_balance()
        self.assertEqual(mock_stdout.getvalue().strip(), "Your balance as of today is $100.00")

    @patch('builtins.input', side_effect=['50.0'])
    def test_valid_deposit(self, mock_input):
        result = bank_app.deposit()
        self.assertEqual(result, 50.0)

    @patch('builtins.input', side_effect=['-50.0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_deposit(self, mock_stdout, mock_input):
        result = bank_app.deposit()
        self.assertEqual(result, 0)
        self.assertEqual(mock_stdout.getvalue().strip(), "Not a valid amount")

    @patch('builtins.input', side_effect=['30.0'])
    def test_valid_withdrawal(self, mock_input):
        bank_app.balance = 50.0
        result = bank_app.withdrawl()
        self.assertEqual(result, 30.0)

    @patch('builtins.input', side_effect=['100.0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_insufficient_funds_withdrawal(self, mock_stdout, mock_input):
        bank_app.balance = 50.0
        result = bank_app.withdrawl()
        self.assertEqual(result, 0)
        self.assertEqual(mock_stdout.getvalue().strip(), "Insufficient funds")

    @patch('builtins.input', side_effect=['-30.0'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_negative_withdrawal(self, mock_stdout, mock_input):
        bank_app.balance = 50.0
        result = bank_app.withdrawl()
        self.assertEqual(result, 0)
        self.assertEqual(mock_stdout.getvalue().strip(), "Amount must be more than 0")

    @patch('builtins.input', side_effect=['1', '4'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_main_show_balance_and_exit(self, mock_stdout, mock_input):
        bank_app.balance = 100.0
        bank_app.main()
        output = mock_stdout.getvalue()
        self.assertIn("Your balance as of today is $100.00", output)
        self.assertIn("Thank you for trying my custom bank app", output)

if __name__ == '__main__':
    unittest.main()