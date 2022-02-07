from django.db import models


class Number(models.Model):
    value = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = 'Number'
        verbose_name_plural = 'Numbers'
