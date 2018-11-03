from django.urls import path

from . import views

app_name = 'recommend'
urlpatterns = [
    path('', views.index, name='find_index'),
    path('smartphone/<int:s_id>', views.recommend_detail, name='smartphone')
]