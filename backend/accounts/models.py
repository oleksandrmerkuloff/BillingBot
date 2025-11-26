from django.db import models


class TelegramUser(models.Model):
    telegram_id = models.BigIntegerField(
        unique=True,
        db_index=True,
        editable=False
    )
    first_active = models.DateTimeField(auto_now_add=True)
    last_activity = models.DateTimeField(auto_now=True)
    full_name = models.CharField(
        max_length=100,
        null=True,
        blank=True
        )

    def __str__(self) -> str:
        if self.full_name:
            return self.full_name
        return f'Unnamed user, last activity was {self.last_activity}'

    class Meta:
        verbose_name = 'Telegram User'
        verbose_name_plural = 'Telegram Users'
        ordering = ['-first_active']
