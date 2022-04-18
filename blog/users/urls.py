from django.urls import path
from users.views import *

urlpatterns = [
    path('sign-up/', sign_up, name='sign-up'),
    path('sign-in/', sign_in, name='sign-in'),
    path('logout/', logout_user, name='logout')
]