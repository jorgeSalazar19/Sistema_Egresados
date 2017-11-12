from django.db import models
from ..categories.categories import Category

class Activity(models.Model):
    class Meta:
        verbose_name = u"Activity"
        verbose_name_plural = u"Activities"

    category = models.ForeignKey(Category , default=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_activity = models.ImageField(upload_to='activity_pictures')

    def __str__(self):
        return self.name