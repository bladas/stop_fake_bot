from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class TelegramUser(models.Model):
    chat_id = models.CharField(max_length=50)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255, null=True, default="")
    phone_number = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.first_name} {self.last_name}'


class TelegramChanel(models.Model):
    chanel_name = models.CharField(max_length=255, blank=True, null=True)
    chanel_url = models.CharField(max_length=255, unique=True)


class ReportAccount(models.Model):
    chat_id = models.CharField(max_length=255, unique=True)
    phone_number = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, blank=True, null=True)


class Report(models.Model):
    telegram_chanel = models.ForeignKey(TelegramChanel, on_delete=models.PROTECT)
    report_account = models.ForeignKey(ReportAccount, on_delete=models.PROTECT)
    text = models.TextField()

