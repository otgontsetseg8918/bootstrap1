from django.db import models

class Subscription(models.Model):
    user_name = models.CharField(max_length = 100)
    user_email = models.CharField(max_length = 100)

    def __str__(self):
        return f"{self.user_name}: {self.user_email}"
    
    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
