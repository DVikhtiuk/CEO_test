import unittest
from unittest import TestCase
from unittest.mock import patch, call
from functionality import Functionality


class TestFunctionality(TestCase):

    @patch("sqlite3.connect")
    def test_valid_check_float(self, mock_con):
        func = Functionality(mock_con)
        result = func.check_float("123.5")
        self.assertEqual(True, result)

    @patch("sqlite3.connect")
    def test_invalid_check_float(self, mock_con):
        func = Functionality(mock_con)
        result = func.check_float("invalid_expense")
        self.assertEqual(False, result)

    @patch("sqlite3.connect")
    def test_check_date(self, mock_con):
        func = Functionality(mock_con)
        result = func.check_date("2022-08-17")
        self.assertEqual(True, result)

    @patch("sqlite3.connect")
    def test_invalid_check_date(self, mock_con):
        func = Functionality(mock_con)
        result = func.check_date("invalid_date")
        self.assertEqual(False, result)

    @patch("builtins.print")
    @patch("builtins.input")
    @patch("functionality.Functionality.check_float")
    @patch("sqlite3.connect")
    def test_add_expense(self, mock_con, mock_float, mock_input, mock_print):
        func = Functionality(mock_con)
        mock_float.return_value = True
        mock_input.side_effect = ["Food", "123.5"]
        func.add_expense("login", "2022-08-17")
        self.assertEqual(mock_print.mock_calls, [call("Thank You! Expense '123.5' was added by category 'food'")])

    @patch("builtins.print")
    @patch("builtins.input")
    @patch("sqlite3.connect")
    def test_get_stat_for_category(self, mock_con, mock_input, mock_print):
        func = Functionality(mock_con)
        mock_input.return_value = "Food"
        mock_con.cursor().execute().fetchone().__getitem__.return_value = '235'
        func.get_stat()
        self.assertEqual(mock_print.mock_calls, [call("Expenses: 235 hrn.")])

    @patch("builtins.print")
    @patch("builtins.input")
    @patch("sqlite3.connect")
    def test_get_stat_for_all(self, mock_con, mock_input, mock_print):
        func = Functionality(mock_con)
        mock_input.return_value = "all"
        mock_con.cursor().execute().fetchone().__getitem__.return_value = '1000'
        func.get_stat()
        self.assertEqual(mock_print.mock_calls, [call('---------------------------------'),
                                                 call('All Expenses: 1000 hrn.')])

    @patch("builtins.print")
    @patch("builtins.input")
    @patch("sqlite3.connect")
    def test_day_stat(self, mock_con, mock_input, mock_print):
        func = Functionality(mock_con)
        mock_input.return_value = '2022-08-13'
        mock_con.cursor().execute().fetchone().__getitem__.return_value = '100'
        func.d_m_y_stat("day")
        self.assertEqual(mock_print.mock_calls, [call("Expense for 2022-08-13: 100 hrn.")])

    @patch("builtins.print")
    @patch("builtins.input")
    @patch("sqlite3.connect")
    def test_month_stat(self, mock_con, mock_input, mock_print):
        func = Functionality(mock_con)
        mock_input.return_value = '2022-08-13'
        mock_con.cursor().execute().fetchone().__getitem__.return_value = '2375'
        func.d_m_y_stat("month")
        self.assertEqual(mock_print.mock_calls, [call('---------------------------------'),
                                                 call('All expenses between 2022-08-13 and 2022-09-12: 2375 hrn.')])

    @patch("builtins.print")
    @patch("builtins.input")
    @patch("sqlite3.connect")
    def test_year_stat(self, mock_con, mock_input, mock_print):
        func = Functionality(mock_con)
        mock_input.return_value = '2021-08-13'
        mock_con.cursor().execute().fetchone().__getitem__.return_value = '1730'
        func.d_m_y_stat("year")
        self.assertEqual(mock_print.mock_calls, [call('---------------------------------'),
                                                 call('All expenses between 2021-08-13 and 2022-08-13: 1730 hrn.')])

    @patch("builtins.print")
    @patch("functionality.Functionality.check_float")
    @patch("functionality.Functionality.check_date")
    @patch("builtins.input")
    @patch("sqlite3.connect")
    def test_awd(self, mock_con, mock_input, mock_date, mock_float, mock_print):
        func = Functionality(mock_con)
        mock_input.side_effect = ['2022-08-12', 'Food', '-1709']
        mock_date.return_value = True
        mock_float.return_value = True
        func.add_with_date('login')
        self.assertEqual(mock_print.mock_calls, [call("Thank You! Expense '1709' was added by \
category 'food' with date '2022-08-12'")])


if __name__ == '__main__':
    unittest.main()
