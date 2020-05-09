from django.urls import path
from todoapp import views

app_name = 'todoapp'

urlpatterns = [
    path('', views.login_view, name='login'),
    path('home/', views.index, name='homepage'),
    path('logout/', views.logout_view, name='logout'),
    path('complete/<int:id>', views.complete, name='complete'),
]