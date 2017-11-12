from django.contrib import admin

from domain.models import (
	Graduated, 
	Category , 
	PreRegisterGraduated , 
	Career ,  
	PreRegisterAdmin , 
	Country,
	Admin,
	Activity
)
@admin.register(Graduated)
class GraduatedAdmin(admin.ModelAdmin):
    list_display = ['user','dni','country','birthday','genre','career','graduation_year']

@admin.register(Admin)
class AdminAdmin(admin.ModelAdmin):
    list_display = ['user','dni','country','genre','cellphone']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Activity)
class ActivityAdmin(admin.ModelAdmin):
    pass    

@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass

@admin.register(PreRegisterGraduated)
class PreRegisterGrduatedAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','dni','country','birthday','genre','career','graduation_year']

@admin.register(PreRegisterAdmin)
class PreRegisterAdminAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','email','dni','country','genre','cellphone']

@admin.register(Career)
class CareerAdmin(admin.ModelAdmin):
    list_display = ['name']