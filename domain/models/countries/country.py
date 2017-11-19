from django.db import models

class Country(models.Model):
    class Meta:
        verbose_name = u"Country"
        verbose_name_plural = u"Countries"

    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name