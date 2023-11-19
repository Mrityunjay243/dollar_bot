import unittest
from unittest.mock import Mock, patch
from telebot import types
from code import search  # Import the module you want to test

class TestSearchFeature(unittest.TestCase):

    @patch('telebot.types.ReplyKeyboardMarkup')
    def test_run(self, mock_reply_keyboard_markup):
        # Arrange
        message = Mock()
        bot = Mock()
        mock_reply_keyboard_markup.return_value.add.side_effect = lambda category: None

        # Act
        search.run(message, bot)

        # Assert
        message.chat.id.assert_called_once()
        bot.send_message.assert_called_once_with(
            message.chat.id,
            "Select a spend category:",
            reply_markup=mock_reply_keyboard_markup.return_value
        )
        bot.register_next_step_handler.assert_called_once()

    @patch('helper.read_json')
    @patch('helper.getUserHistory')
    def test_post_select_category(self, mock_get_user_history, mock_read_json):
        # Arrange
        message = Mock()
        bot = Mock()
        mock_get_user_history.return_value = [
            "18-Nov-2023 11:16,Food,10.0",
            "18-Nov-2023 21:11,Food,10.0",
            "19-Nov-2023 15:30,Entertainment,20.0"
        ]

        # Act
        search.post_select_category(message, bot)

        # Assert
        mock_read_json.assert_called_once()
        mock_get_user_history.assert_called_once_with(message.chat.id)
        bot.send_message.assert_called_once_with(
            message.chat.id,
            "Here is your spending history by category : \nDATE, CATEGORY, AMOUNT\n----------------------\n"
            "18-Nov-2023 11:16,Food,10.0\n18-Nov-2023 21:11,Food,10.0\n"
        )

    @patch('helper.read_json', side_effect=Exception("Some error"))
    def test_post_select_category_exception(self, mock_read_json):
        # Arrange
        message = Mock()
        bot = Mock()

        # Act
        search.post_select_category(message, bot)

        # Assert
        mock_read_json.assert_called_once()
        bot.reply_to.assert_called_once_with(message, "Oops!Some error")

if __name__ == '__main__':
    unittest.main()
