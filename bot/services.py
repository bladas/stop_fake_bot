from django.contrib.auth import get_user_model
from telegram import Contact
from bot.models import TelegramUser

User = get_user_model()


class TelegramUserService:

    @staticmethod
    def init_from_contact(contact: Contact):
        return TelegramUser(
            chat_id=contact.user_id,
            first_name=contact.first_name,
            last_name=contact.last_name or None,
            phone_number=contact.phone_number,
        )
