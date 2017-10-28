from django.forms import ModelForm 
from django.contrib.auth.models import User
from domain.models import PreRegisterGraduated , PreRegisterAdmin
from django.core.validators import RegexValidator
import re
from django import forms
from datetime import datetime, date, time, timedelta
from dateutil.relativedelta import relativedelta

LIMITE = (date.today() - relativedelta(years=100))

patron_nombre_apellido = re.compile('([A-ZÁÉÍÓÚ a-zñáéíóú]{1}[a-zñáéíóú A-ZÁÉÍÓÚ ]+[\s]*)+')
patron_email = re.compile('[\w]+@{1}[\w]+(\.[\w]+)*\.[a-z]{2,3}')
patron_dni = re.compile('[\d]{10}')
patron_telefono = re.compile('[3]{1}[0|1|2]{1}[\d]{8}')

class RegisterFormGraduated(ModelForm):
    class Meta:
        model = PreRegisterGraduated
        fields=['first_name','last_name','email','dni','country','birthday','genre','career','graduation_year']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if re.match(patron_nombre_apellido,first_name) is None:
            raise forms.ValidationError("error nombre")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if re.match(patron_nombre_apellido,last_name) is None:
            raise forms.ValidationError("error apellido")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.match(patron_email,email) is None:
            raise forms.ValidationError("error email")
        return email

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if re.match(patron_dni,dni) is None:
            raise forms.ValidationError("error dni")
        return dni

    def clean_birthday(self):
        now_date = datetime.now()
        birthday = self.cleaned_data.get('birthday')
        if birthday < LIMITE:
            raise forms.ValidationError("error fecha")
        return birthday

    def clean_graduation_year(self):
        birthday = self.cleaned_data.get('birthday')
        graduation_year = self.cleaned_data.get('graduation_year')
        if graduation_year < (birthday + relativedelta(years=18)):
            raise forms.ValidationError("error fecha graduacion")
        return graduation_year

class RegisterFormAdmin(ModelForm):
    class Meta:
        model = PreRegisterAdmin
        fields=['first_name','last_name','email','dni','country','genre','cellphone']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if re.match(patron_nombre_apellido,first_name) is None:
            raise forms.ValidationError("error nombre")
        return first_name

    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if re.match(patron_nombre_apellido,last_name) is None:
            raise forms.ValidationError("error apellido")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.match(patron_email,email) is None:
            raise forms.ValidationError("error email")
        return email

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if re.match(patron_dni,dni) is None:
            raise forms.ValidationError("error dni")
        return dni