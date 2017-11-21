from django.forms import ModelForm 
from domain.models import Activity
from django.core.validators import RegexValidator
import re
from django import forms
from datetime import datetime
from datetime import datetime, date, time, timedelta

patron_nombre = re.compile('([A-ZÁÉÍÓÚa-zñáéíóú]{1}[a-zñáéíóúA-ZÁÉÍÓÚ]+)')
patron_descripcion = re.compile('([A-ZÁÉÍÓÚa-zñáéíóú]{1}[a-zñáéíóúA-ZÁÉÍÓÚ]+[\s]*)+')

LISTA_ERROR_ACTIVITY = []
class CreateFormActivity(ModelForm):
    class Meta:
        model = Activity
        fields=['category','name','description','image_activity', 'time_activity' , 'date_activity']
        exclude=[]

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if re.match(patron_nombre,name) is None:
            if 'name' not in LISTA_ERROR_ACTIVITY:
                LISTA_ERROR_ACTIVITY.append('name')
            raise forms.ValidationError("Tienes un error en el campo nombre de actividad.")
        return name

    def clean_description(self):
    	description = self.cleaned_data.get('description')
    	if re.match(patron_descripcion,description) is None:
    		if 'description' not in LISTA_ERROR_ACTIVITY:
    			LISTA_ERROR_ACTIVITY.append('description')
    		raise forms.ValidationError("Tienes un error en el campo descripción de actividad.")
    	return description

    def clean_date_activity(self):
        date_activity = self.cleaned_data.get('date_activity')
        if date_activity < date.today():
            LISTA_ERROR_ACTIVITY.append('date_activity')
            raise forms.ValidationError("Tienes un error en el campo fecha de actividad")
        return date_activity

    def get_errors(self):
    	return LISTA_ERROR_ACTIVITY

    def clean_errors(self):
        for i in range(len(LISTA_ERROR_ACTIVITY)):
            LISTA_ERROR_ACTIVITY.pop()