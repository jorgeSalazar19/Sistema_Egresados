from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

from ..categories.categories import Category
from ..careers.careers import Career
from ..countries.country import Country

GENRE = (
    ('male','Hombre'),
    ('female', 'Mujer')
)

class Graduated(models.Model):
    
    class Meta:
        verbose_name = u"Graduated"
        verbose_name_plural = u"Graduates"

    user = models.ForeignKey(User)
    dni = models.CharField(max_length=15, null=False , primary_key=True)
    profile_picture = models.ImageField(default=True , upload_to='profile_pictures', null=True)
    country = models.ForeignKey(Country)
    birthday = models.DateField()
    genre = models.CharField(choices=GENRE, max_length=10)
    career = models.ForeignKey(Career)
    graduation_year = models.DateField()
    preferences = models.ManyToManyField(Category)
    friends = models.ManyToManyField("Graduated")
    first_login = models.IntegerField(default=0 , null=True)


    def __str__(self):
        return "%s %s"%(self.user.first_name, self.user.last_name)