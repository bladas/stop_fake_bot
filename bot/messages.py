from telegram import KeyboardButton, ReplyKeyboardMarkup

from bot.bot import bot


def send_text_message(user_id: int, text):
    bot.send_message(
        user_id,
        text=text,
    )


def start_reporting_message(user_id: int) -> None:
    report_button = KeyboardButton(
        text="Надішліть номер телефону", request_contact=True
    )
    keyboard = ReplyKeyboardMarkup([[report_button]])
    bot.send_message(
        user_id,
        reply_markup=keyboard,
        text="Натисніть на кнопку",
    )

