from django.forms import ModelForm 
from django.contrib.auth.models import User
from domain.models import PreRegisterGraduated , PreRegisterAdmin
from domain.models import Admin
from django.core.validators import RegexValidator
import re
from django import forms
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta
from django.contrib.auth.models import User
from django import forms

LIMITE = (date.today() - relativedelta(years=100))

patron_nombre_apellido = re.compile('([A-ZÁÉÍÓÚ a-zñáéíóú]{1}[a-zñáéíóú A-ZÁÉÍÓÚ ]+[\s]*)+')
patron_email = re.compile('[\w]+@{1}[\w]+(\.[\w]+)*\.[a-z]{2,3}')
patron_dni = re.compile('[\d]{10}')
patron_telefono = re.compile('[3]{1}[0|1|2]{1}[\d]{8}')

LISTA_ERROR_ADMIN=[]
class RegisterFormAdmin(ModelForm):
    class Meta:
        model = PreRegisterAdmin
        fields=['first_name','last_name','email','dni','country','genre','cellphone']
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if re.match(patron_nombre_apellido,first_name) is None:
            if 'first_name' not in LISTA_ERROR_ADMIN:
                LISTA_ERROR_ADMIN.append('first_name')
            raise forms.ValidationError("Tienes un error en el campo nombre")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if re.match(patron_nombre_apellido,last_name) is None:
            if 'last_name' not in LISTA_ERROR_ADMIN:
                LISTA_ERROR_ADMIN.append('last_name')
            raise forms.ValidationError("Tienes un error en el campo apellido")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.match(patron_email,email) is None:
            if 'email' not in LISTA_ERROR_ADMIN:
                LISTA_ERROR_ADMIN.append('email')
            raise forms.ValidationError("Tienes un error en el campo email")
        return email

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if re.match(patron_dni,dni) is None:
            if 'dni' not in LISTA_ERROR_ADMIN:
                LISTA_ERROR_ADMIN.append('dni')
            raise forms.ValidationError("Tienes un error en el campo dni")
        return dni

    def get_errors(self):
        return LISTA_ERROR_ADMIN