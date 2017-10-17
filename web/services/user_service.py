from django.contrib.auth.models import User

from domain.models import (
    Graduated, 
    Career, 
    Country, 
    PreRegisterGraduated
)

class UserService:

    def __init__(self, user_data):
        self.user = None
        self.user_data = user_data

    def _create_user(self):
        user = User.objects.create_user(username = self.user_data['dni'],
                            email = self.user_data['email'],
                            password = self.user_data['temporal_password'])
        user.first_name = self.user_data['first_name']
        user.last_name = self.user_data['last_name']
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

    def _delete_preregister(self):
        preregister = PreRegisterGraduated.objects.get(id=self.user_data['id'])
        preregister.delete()

    def register_graduated(self):
        self._create_user()
        self._create_greaduated()
        self._delete_preregister()
        
        
        
        
        
        
        
        
        
        