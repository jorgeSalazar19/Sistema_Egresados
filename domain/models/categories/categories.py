from django.db import models

class Category(models.Model):
    class Meta:
        verbose_name = u"Category"
        verbose_name_plural = u"Categories"

    name = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name

   