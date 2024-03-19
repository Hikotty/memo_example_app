from django.urls import path
from . import views

urlpatterns = [
    path('is_alive/', views.is_alive, name="is_alive"),
    path('', views.memo_list, name="memo_list"),
    path('html_test/', views.html_test, name="html_test"),
    path('<int:pk>/', views.memo_detail, name='memo_detail'),
]