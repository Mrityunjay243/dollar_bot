import unittest
from datetime import datetime
from unittest.mock import patch
from io import StringIO
import sys

# Import the functions you want to test
from code import calculate_total_expenses, is_overall_budget_exceeded, calculate_expenses_by_category, display_pie_chart, run

class TestExpenseTracker(unittest.TestCase):
    
    def test_calculate_total_expenses(self):
        user_history = ["18-Nov-2023,Food,10.0", "18-Nov-2023,Clothing,20.0", "19-Nov-2023,Food,15.0"]
        total_expenses = calculate_total_expenses(user_history)
        self.assertEqual(total_expenses, {'Food': 25.0, 'Clothing': 20.0})
    
    def test_is_overall_budget_exceeded(self):
        user_history = ["18-Nov-2023,Food,10.0", "18-Nov-2023,Clothing,20.0", "19-Nov-2023,Food,15.0"]
        self.assertFalse(is_overall_budget_exceeded(user_history, 100.0))
        self.assertTrue(is_overall_budget_exceeded(user_history, 30.0))
    
    def test_calculate_expenses_by_category(self):
        user_history = ["18-Nov-2023,Food,10.0", "18-Nov-2023,Clothing,20.0", "19-Nov-2023,Food,15.0"]
        from_date = datetime.strptime("18-Nov-2023", "%d-%b-%Y")
        to_date = datetime.strptime("19-Nov-2023", "%d-%b-%Y")
        expenses_by_category = calculate_expenses_by_category(user_history, from_date, to_date)
        self.assertEqual(expenses_by_category, {'Food': 25.0, 'Clothing': 20.0})
    
    @patch('matplotlib.pyplot.savefig')
    @patch('matplotlib.pyplot.close')
    @patch('telegram.Bot.send_message')
    @patch('telegram.Bot.send_document')
    def test_display_pie_chart(self, mock_send_document, mock_send_message, mock_close, mock_savefig):
        user_history = ["18-Nov-2023,Food,10.0", "18-Nov-2023,Clothing,20.0", "19-Nov-2023,Food,15.0"]
        user_budget = 100.0
        from_date = datetime.strptime("18-Nov-2023", "%d-%b-%Y")
        to_date = datetime.strptime("19-Nov-2023", "%d-%b-%Y")
        
        fig = display_pie_chart(user_history, user_budget, from_date, to_date)
        
        # Check if the necessary functions were called
        mock_savefig.assert_called_once()
        mock_close.assert_called_once()
        mock_send_message.assert_called_once()
        mock_send_document.assert_called_once()
    
    @patch('helper.read_json')
    @patch('helper.getUserHistory')
    @patch('helper.getOverallBudget')
    @patch('telegram.Bot.send_message')
    @patch('telegram.Bot.send_document')
    def test_run(self, mock_send_document, mock_send_message, mock_get_budget, mock_get_user_history, mock_read_json):
        chat_id = 123
        message_text = "/run 18-Nov-2023 19-Nov-2023"
        message = unittest.mock.Mock()
        message.chat.id = chat_id
        message.text = message_text

        with patch('builtins.open', unittest.mock.mock_open()) as mock_open:
            run(message, unittest.mock.Mock())

        # Check if the necessary functions were called
        mock_read_json.assert_called_once()
        mock_get_user_history.assert_called_once_with(chat_id)
        mock_get_budget.assert_called_once_with(chat_id)
        mock_send_message.assert_called_once()
        mock_send_document.assert_called_once()

if __name__ == '__main__':
    unittest.main()
