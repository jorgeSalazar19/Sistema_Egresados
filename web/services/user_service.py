from django.contrib.auth.models import User

from domain.models import (
    Graduated,
    Admin, 
    Career, 
    Country, 
    PreRegisterGraduated,
    PreRegisterAdmin
)

class UserService:

    def __init__(self, user_data):
        self.user = None
        self.user_data = user_data

    def _create_user_graduated(self):
        user = User.objects.create_user(username = self.user_data['dni'],
                            email = self.user_data['email'],
                            password = self.user_data['temporal_password'])
        user.first_name = self.user_data['first_name']
        user.last_name = self.user_data['last_name']
        user.save()
        self.user = user

    def _create_user_admin(self):
        user = User.objects.create_user(username = self.user_data['dni'],
                            email = self.user_data['email'],
                            password = self.user_data['temporal_password'])
        user.first_name = self.user_data['first_name']
        user.last_name = self.user_data['last_name']
        user.is_staff = True
        user.save()
        self.user = user

    def _create_greaduated(self):
        career = Career.objects.get(id= self.user_data['career_id'])
        country = Country.objects.get(id=self.user_data['country_id'])
        Graduated.objects.create(
                            user = self.user,
                            dni = self.user_data['dni'],
                            country = country,
                            birthday = self.user_data['birthday'],
                            genre = self.user_data['genre'],
                            career = career,
                            graduation_year = self.user_data['graduation_year']
                        )
    def _create_admin(self):
        country = Country.objects.get(id=self.user_data['country_id'])
        Admin.objects.create(
                            user = self.user,
                            dni = self.user_data['dni'],
                            country = country,
                            genre = self.user_data['genre'],
                            cellphone = self.user_data['cellphone'],
                            profile_picture = None
                        )

    def _delete_preregister_graduated(self):
        preregister = PreRegisterGraduated.objects.get(id=self.user_data['id'])
        preregister.delete()

    def _delete_preregister_admin(self):
        preregister = PreRegisterAdmin.objects.get(id=self.user_data['id'])
        preregister.delete()

    def _validate_account_admin(self):
        user = User.objects.filter(username=self.user_data['dni'])
        if user.count() == 0:
            self._create_user_graduated()
        else:
            user = user[0]
            if user.is_staff:
                self.user = user
            else:
                raise Exception("El usuario ya existe")

    def _validate_account_graduated(self):
        user = User.objects.filter(username=self.user_data['dni'])
        if user.count() == 0:
            self._create_user_admin()
        else:
            user = user[0]
            if user.is_staff:
                raise Exception("El usuario ya existe")    
            else:
                self.user = user
                self.user.is_staff = True
                self.user.save()

    def register_graduated(self):
        self._validate_account_admin()
        self._create_greaduated()
        self._delete_preregister_graduated()

    def register_admin(self):
        self._validate_account_graduated()
        self._create_admin()
        self._delete_preregister_admin()
        
        
        
        
        
        
        
        
        
        