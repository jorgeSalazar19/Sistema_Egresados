from django.db import models

class Career(models.Model):
    class Meta:
        verbose_name = u"Career"
        verbose_name_plural = u"Careers"

    name = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.name