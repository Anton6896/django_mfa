import uuid
from django.db import models
from django.contrib.auth import get_user_model


class VerificationCode(models.Model):
    code = models.CharField(max_length=7, blank=True)
    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                related_name='verification_code')

    def __str__(self):
        return str(self.code)

    def save(self, *args, **kwargs):
        self.code = str(uuid.uuid4())[:5]
        super().save(*args, **kwargs)
