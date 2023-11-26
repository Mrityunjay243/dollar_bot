def run(message, bot):
    chat_id = message.chat.id
    support_message = (
        "The best way to contact our support team is to send a message to this bot.\n"
        "Frequently Asked Questions: /faq\n"

        "We'll reply right here as soon as we can.\n"
        "Phone: +19195597611\n"
        "Email: divitkalathil@gmail.com\n"
        "Create Issues: https://github.com/Mrityunjay243/dollar_bot/issues\n"
    )
    bot.send_message(chat_id, support_message)
