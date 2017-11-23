from django.db import models
from ..categories.categories import Category
from datetime import datetime

class Activity(models.Model):
    class Meta:
        verbose_name = u"Activity"
        verbose_name_plural = u"Activities"

    category = models.ForeignKey(Category , default=True)
    name = models.CharField(max_length=50)
    description = models.TextField()
    image_activity = models.ImageField(upload_to='activity_pictures')
    date_creation = models.DateTimeField(null=True)
    last_modification = models.DateTimeField(null=True)
    time_activity = models.TimeField(null=True)
    date_activity = models.DateField(null=True)

    def __str__(self):
        return self.name
