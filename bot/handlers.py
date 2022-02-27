from telegram import Update

from bot.messages import send_text_message, start_reporting_message
from bot.models import ReportAccount
from bot.state import START_REPORTING
from bot.services import TelegramUserService


def start_handler(update: Update, context) -> None:
    user_id = update.message.from_user.id
    send_text_message(
        user_id=user_id,
        text="Вітаю в боті для блокування каналів з фейковою інформацією!"
    )
    start_reporting_message(user_id=user_id)
    return START_REPORTING


def phone_handler(update: Update, context) -> None:
    user_id = update.message.from_user.id
    phone_number = update.message.text
    ReportAccount.objects.create(
        chat_id=user_id,
        phone_number=phone_number
    )
    send_text_message(user_id=user_id, text="Надішліть свій email")


def start_reporting_handler(update: Update, context) -> None:
    user_id = update.message.from_user.id
    contact = update.effective_message.contact
    telegram_user = TelegramUserService.init_from_contact(contact)
    telegram_user.save()
    send_text_message(
        user_id=user_id,
        text="Скарги на ворожі канали відправлені!"
    )
    # send_report_task() # задача для відправлення репортів
