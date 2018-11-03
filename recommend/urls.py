from django.urls import path

from . import views

app_name = 'recommend'
urlpatterns = [
    path('', views.index, name='find_index'),
    path('smartphone/', views.smartphone, name='smartphones'),
    path('smartphone/result', views.smartphone_result, name='smartphone_result'),
    path('smartphone/<int:s_id>', views.smartphone_detail, name='smartphone_detail'),
]