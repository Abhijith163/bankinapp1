# mybankingapp/urls.py
from django.urls import path
from .views import index, district_wikipedia, login_view, register,user_profile
from .views import login_view
from .views import welcome_view
from . import views
urlpatterns = [
    path('', index, name='index'),
    
    path('branches/<str:district>/', district_wikipedia, name='district_wikipedia'),
    path('login/', login_view, name='login'),
    path('register/', register, name='register'),
    path('user_profile/', user_profile, name='user_profile'),
    path('get-branches', views.get_branches),
    path('welcome/', welcome_view, name='welcome'),
    # Add any other URLs you need
]


