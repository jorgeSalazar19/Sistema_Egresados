from django.db import models

from ..categories.categories import Category
from ..careers.careers import Career
from ..countries.country import Country

GENRE = (
    ('male','Masculino'),
    ('female', 'Femenino'),
    ('other', 'Otro')
)


class PreRegisterGraduated(models.Model):
    class Meta:
        verbose_name = u"PreRegisterGraduated"
        verbose_name_plural = u"PreRegistersGraduatedes"

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField()
    dni = models.CharField(max_length=15, null=False)
    country = models.ForeignKey(Country)
    birthday = models.DateField()
    genre = models.CharField(choices=GENRE, max_length=10)
    career = models.ForeignKey(Career)
    graduation_year = models.DateField()

    def __str__(self):
        return self.first_name +" " + self.last_name

class PreRegisterAdmin(models.Model):
    class Meta:
        verbose_name = u"PreRegisterAdmin"
        verbose_name_plural = u"PreRegistersAdmins"

    first_name = models.CharField(max_length=30, null=False)
    last_name = models.CharField(max_length=30, null=False)
    email = models.EmailField()
    dni = models.CharField(max_length=15, null=False)
    country = models.ForeignKey(Country)
    genre = models.CharField(choices=GENRE, max_length=10)
    cellphone = models.IntegerField()

    def __str__(self):
        return self.first_name + self.last_name