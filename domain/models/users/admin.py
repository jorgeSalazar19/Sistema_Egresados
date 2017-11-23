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
    profile_picture = models.ImageField(default=True , upload_to='profile_pictures', null=True)
    dni = models.CharField(max_length=15, null=False , primary_key=True)
    country = models.ForeignKey(Country)
    genre = models.CharField(choices=GENRE, max_length=10)
    cellphone = models.BigIntegerField(null=True)
    first_login = models.IntegerField(default=0)
    last_login = models.DateTimeField(null=True)
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return "%s %s"%(self.user.first_name, self.user.last_name)