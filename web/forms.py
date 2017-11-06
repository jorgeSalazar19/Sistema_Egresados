
from django.forms import ModelForm 
from django.contrib.auth.models import User
from domain.models import PreRegisterGraduated , PreRegisterAdmin
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

LISTA_ERROR_GRADUATED = []
class RegisterFormGraduated(ModelForm):
    class Meta:
        model = PreRegisterGraduated
        fields=['first_name','last_name','email','dni','country','birthday','genre','career','graduation_year']

    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        if re.match(patron_nombre_apellido,first_name) is None:
            if 'first_name' not in LISTA_ERROR_GRADUATED:
                LISTA_ERROR_GRADUATED.append('first_name')
            raise forms.ValidationError("Tienes un error en el campo nombre")
        return first_name
    
    def clean_last_name(self):
        last_name = self.cleaned_data.get('last_name')
        if re.match(patron_nombre_apellido,last_name) is None:
            if 'last_name' not in LISTA_ERROR_GRADUATED:
                LISTA_ERROR_GRADUATED.append('last_name')
            raise forms.ValidationError("Tienes un error en el campo apellido")
        return last_name

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if re.match(patron_email,email) is None:
            if 'email' not in LISTA_ERROR_GRADUATED:
                LISTA_ERROR_GRADUATED.append('email')
            raise forms.ValidationError("Tienes un error en el campo email")
        return email

    def clean_dni(self):
        dni = self.cleaned_data.get('dni')
        if re.match(patron_dni,dni) is None:
            if 'dni' not in LISTA_ERROR_GRADUATED:
                LISTA_ERROR_GRADUATED.append('dni')
            raise forms.ValidationError("Tienes un error en el campo dni")
        return dni

    def clean_birthday(self):
        now_date = datetime.now()
        birthday = self.cleaned_data.get('birthday')
        if birthday < LIMITE:
            if 'birthday' not in LISTA_ERROR_GRADUATED:
                LISTA_ERROR_GRADUATED.append('birthday')
            raise forms.ValidationError("Tienes un error en el campo fecha de nacimiento")
        return birthday

    def clean_graduation_year(self):
        birthday = self.cleaned_data.get('birthday')
        graduation_year = self.cleaned_data.get('graduation_year')
        if graduation_year < (birthday + relativedelta(years=18)):
            if 'graduation_year' not in LISTA_ERROR_GRADUATED:
                LISTA_ERROR_GRADUATED.append('graduation_year')
            raise forms.ValidationError("Tienes un error en el campo fecha graduacion")
        return graduation_year

    def get_errors(self):
        return LISTA_ERROR_GRADUATED

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

class FormEmail(forms.ModelForm):
    class Meta:
        model = User
        exclude = [
                'username',
                'first_name',
                'last_name',
                'email',
                'password',
                'groups',
                'user_permissions',
                'is_staff',
                'is_active',
                'is_superuser',
                'last_login',
                'date_joined'
        ]
    email = forms.EmailField(label='Correo' , widget=forms.TextInput(attrs={'id':'my_id','class':'my_class','placeholder':'Ingrese su email'}))

    def clean_email(self):
        email = self.cleaned_data.get('email')
        email_exist = User.objects.filter(email=email)
        if re.match(patron_email,email) is None:
            raise forms.ValidationError("El correo no es valido")
        if len(email_exist) == 0:
            raise forms.ValidationError("El correo no esta en nuestra base datos")

