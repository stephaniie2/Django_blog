from django.urls import path
from . import views

app_name = 'blog'
# URL patterns allow you to map URLs to views.
urlpatterns = [
    # post views
    path('', views.post_list, name='post_list'),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/',
         views.post_detail,
         name='post_detail'),
]
