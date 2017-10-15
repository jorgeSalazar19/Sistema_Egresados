from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ..categories.categories import Category
from ..careers.careers import Career

GENRE = (
    ('male','Hombre'),
    ('female', 'Mujer')
)

COUNTRIES = (
    ('colombia','Colombia'),
)

class Graduated(models.Model):
    
    class Meta:
        verbose_name = u"Graduated"
        verbose_name_plural = u"Graduates"

    user = models.ForeignKey(User)
    dni = models.CharField(max_length=15, null=False , primary_key=True)
    country = models.CharField(max_length=30, null=False, choices=COUNTRIES)
    birthday = models.DateField()
    genre = models.CharField(choices=GENRE, max_length=10)
    career = models.ForeignKey(Career)
    graduation_year = models.DateField()
    categories  = models.ManyToManyField(Category)


    def __str__(self):
    	return "%s %s"%(self.user.first_name, self.user.last_name)