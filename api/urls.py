from django.urls import path

from api.views import detail, shop_list, LoginAPI
from api.views import RegisterAPI

from knox import views as knox_views


app_name = 'api'

urlpatterns = [
    path('all/', shop_list, name='all'),
    path('all/<int:id>', detail, name='allid'),
    path('auth/register/', RegisterAPI.as_view(), name='register'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('auth/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]

