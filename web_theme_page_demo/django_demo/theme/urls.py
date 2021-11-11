from django.urls import path, re_path
from theme import views

app_name = 'theme'

urlpatterns = [
    #example = /theme/1/
    path('theme/<int:pk>/', views.ThemeDV.as_view(), name='theme_detail'),

    path('place/<int:pk>/', views.PlaceDV.as_view(), name='place_detail'),

]