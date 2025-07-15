from django.urls import path
from apps.post import views as views

app_name='post'

#siempre revisar sintaxis si usamos todo plural o todo singular(users/profile > ruta del link)
urlpatterns = [
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name='post_detail'),
    
]