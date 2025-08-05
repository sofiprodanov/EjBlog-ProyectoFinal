from django.urls import path
from apps.post import views as views

app_name='post'

#siempre revisar sintaxis si usamos todo plural o todo singular(users/profile > ruta del link)
urlpatterns = [
    path("posts/", views.PostListView.as_view(), name='post_list'),
    path("posts/<slug:slug>", views.PostDetailView.as_view(), name='post_detail'),
    path("posts/<slug:slug>/delete", views.PostDeleteView.as_view(), name='post_delete'),
    path("posts/<slug:slug>/update", views.PostUpdateView.as_view(), name='post_update'),
    
]