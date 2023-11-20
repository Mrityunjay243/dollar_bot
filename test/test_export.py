import unittest
from unittest.mock import patch, MagicMock
import io
import os

from code import export



@patch('builtins.open', new_callable=io.StringIO)
def test_export_to_csv(self, mock_open):
    user_history = ["18-Nov-2023,Food,10.0", "19-Nov-2023,Clothing,20.0"]
    file_path = "test_export.csv"
    export.export_to_csv(user_history, file_path)
    
    # Check if the CSV file is correctly written
    expected_csv_content = "Date,Category,Amount\n18-Nov-2023,Food,10.0\n19-Nov-2023,Clothing,20.0\n"
    self.assertEqual(mock_open.getvalue(), expected_csv_content)

    # Clean up the test file
    os.remove(file_path)

@patch('pandas.DataFrame.to_excel')
def test_export_to_excel(self, mock_to_excel):
    user_history = ["18-Nov-2023,Food,10.0", "19-Nov-2023,Clothing,20.0"]
    file_path = "test_export.xlsx"
    export.export_to_excel(user_history, file_path)

    # Check if the Excel file is correctly written
    mock_to_excel.assert_called_once_with(file_path, index=False)

    # Clean up the test file
    os.remove(file_path)

@patch('helper.getUserHistory', return_value=["18-Nov-2023,Food,10.0", "19-Nov-2023,Clothing,20.0"])
@patch('telegram.Bot.send_document')
def test_run(self, mock_send_document, mock_get_user_history):
    bot = MagicMock()
    message = MagicMock()
    message.text = "/export csv"
    message.chat.id = 123

    with patch('builtins.open', new_callable=io.StringIO) as mock_open:
        export.run(message, bot)

    # Check if the CSV file is correctly sent
    expected_csv_content = "Date,Category,Amount\n18-Nov-2023,Food,10.0\n19-Nov-2023,Clothing,20.0\n"
    mock_send_document.assert_called_once()
    self.assertEqual(mock_open.getvalue(), expected_csv_content)

if __name__ == '__main__':
    unittest.main()
