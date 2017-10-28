from django.db import models
from django.contrib.auth.models import User
from ..countries.country import Country

GENRE = (
    ('male','Hombre'),
    ('female', 'Mujer')
)

class Admin(models.Model):
    
    class Meta:
        verbose_name = u"Admin"
        verbose_name_plural = u"Admins"

    user = models.ForeignKey(User)
    dni = models.CharField(max_length=15, null=False , primary_key=True)
    country = models.ForeignKey(Country)
    genre = models.CharField(choices=GENRE, max_length=10)
    cellphone = models.BigIntegerField()
    first_login = models.IntegerField(default=0)


    def __str__(self):
        return "%s %s"%(self.user.first_name, self.user.last_name)