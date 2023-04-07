from django.urls import path
from . import views


urlpatterns = [
    path('<int:movie_id>/', views.detail, name='detail'),
    path('<int:movie_id>/create/', views.create_review, name='create_review'),
]