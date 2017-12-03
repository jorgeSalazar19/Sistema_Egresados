from django.db import models

class Historial(models.Model):
    class Meta:
        verbose_name = u"Historial"
        verbose_name_plural = u"Historiales"

    from_email = models.CharField(max_length=1000)
    to_email = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)
    date_email = models.DateField()

    def __str__(self):
        return self.from_email