from django.urls import path
from apps.user import views as views

app_name='user'

#siempre revisar sintaxis si usamos todo plural o todo singular(users/profile > ruta del link)
urlpatterns = [
    path("users/profile", views.UserProfileView.as_view(), name='user_profile'),
    
]